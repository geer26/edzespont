A project skeleton lényegében azt jelenti, hogy hogyan szervezed a kódot mappákba, hogy 3 hónap múlva se legyen káosz.
A legtöbb tutorial így indul:
main.pymodels.pydatabase.pyauth.py
Ez 5-10 endpointig rendben van.
A SzakiApp viszont várhatóan tartalmazni fog:


Auth


Ügyfelek


Munkák


Árajánlatok


Számlák


Naptár


Riportok


Felhasználók


Cégek


Itt már gyorsan 50-100 endpoint lesz.

Egy lehetséges FastAPI skeleton
app/│├── api/│   ├── auth.py│   ├── customers.py│   ├── jobs.py│   ├── quotes.py│   └── invoices.py│├── models/│   ├── user.py│   ├── customer.py│   ├── job.py│   └── quote.py│├── schemas/│   ├── customer.py│   ├── job.py│   └── quote.py│├── services/│   ├── customer_service.py│   ├── quote_service.py│   └── invoice_service.py│├── repositories/│   ├── customer_repository.py│   ├── job_repository.py│   └── quote_repository.py│├── db/│   ├── database.py│   └── session.py│├── core/│   ├── config.py│   ├── security.py│   └── exceptions.py│└── main.py

Mi van az api mappában?
Ez a HTTP réteg.
Például:
@router.post("/customers")async def create_customer(    data: CustomerCreate):    return customer_service.create(data)
Itt csak azt mondod:


jött egy kérés


validáld


add tovább


Semmi üzleti logika.

Mi van a models mappában?
Itt vannak az adatbázis táblák.
class Customer(SQLModel, table=True):    id: int | None = Field(default=None, primary_key=True)    name: str    phone: str
Ez lesz a PostgreSQL:
customers
tábla.

Mi van a schemas mappában?
Ez nagyon fontos.
Sokan összekeverik a modellekkel.
Példa:
Adatbázis:
class Customer(...)
API kérés:
class CustomerCreate(SQLModel):    name: str    phone: str
API válasz:
class CustomerResponse(SQLModel):    id: int    name: str    phone: str
Nem mindig akarod ugyanazokat a mezőket visszaküldeni.

Mi van a repository-ban?
Ez kommunikál az adatbázissal.
Például:
class CustomerRepository:    def get_by_id(        self,        session,        customer_id    ):        return session.get(            Customer,            customer_id        )
Ő tud SQL-t.
Más nem.

Mi van a service-ben?
Itt van az üzleti logika.
Példa:
A szakember elfogad egy árajánlatot.
Nem csak annyi történik, hogy:
status = accepted
Hanem:


státusz váltás


email küldés


naptár esemény létrehozás


logolás


Ez már üzleti logika.
class QuoteService:    def accept_quote(        self,        quote_id    ):        quote.status = "accepted"        email_service.send(...)        calendar_service.create(...)        return quote

Miért kell külön repository és service?
Kezdők gyakran ezt írják:
@router.post(...)def create_customer():    customer = Customer(...)    db.add(customer)    db.commit()    send_email()    generate_pdf()    return customer
Elsőre működik.
6 hónap múlva:
500 soros endpoint
és senki nem tudja karbantartani.

Mi van a core mappában?
Közös dolgok.
Például:
JWT titok
DATABASE_URL
SMTP beállítások
Stripe kulcs
Példa:
class Settings(BaseSettings):    DATABASE_URL: str    JWT_SECRET: str

Hogyan nézne ki egy kérés útja?
Mondjuk a szakember létrehoz egy ügyfelet.
Frontend    ↓API endpoint    ↓Service    ↓Repository    ↓PostgreSQL
Konkrétan:
POST /customers
↓
api/customers.py
↓
customer_service.create()
↓
customer_repository.save()
↓
INSERT INTO customers ...

A SzakiAppnál én még hozzáadnék egy mappát
tasks/
Ide mennének a Celery feladatok:
tasks/├── email_tasks.py├── sms_tasks.py└── invoice_tasks.py
Például:
send_invoice_email.delay(...)
Így az API nem várja meg az email kiküldését.

A lényeg: a skeleton célja nem a "szép mappastruktúra", hanem hogy amikor a SzakiApp 20 endpoint helyett 120-at, 8 adatmodell helyett 25-öt és 500 helyett 5000 felhasználót kezel, akkor is átlásd a kódot és tudj új funkciókat hozzáadni anélkül, hogy mindenhez hozzá kellene nyúlni. Ezért különítjük el az API → Service → Repository → Database rétegeket.