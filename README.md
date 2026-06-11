# edzespont
1. Felhasználói szerepkörök
Vendég


Termek böngészése


Órarend megtekintése


Regisztráció


Tag


Bejelentkezés


Órákra jelentkezés


Jelentkezés lemondása


Saját foglalások megtekintése


Várólistára feliratkozás


Értesítések fogadása


Edző


Saját órák kezelése


Résztvevők listájának megtekintése


Jelenlét rögzítése


Óra lemondása


Teremvezető


Edzők kezelése


Óratípusok kezelése


Termek kezelése


Órarend szerkesztése


Statisztikák


Rendszergazda


Minden terem kezelése


Jogosultságok kezelése


Platformbeállítások



2. Alapfunkciók (MVP)
Felhasználókezelés


Regisztráció


Bejelentkezés


Jelszó-visszaállítás


Profil szerkesztése


Profil:


Név


E-mail


Telefonszám


Profilkép



Órarend
Minden órához:


Név


Leírás


Edző


Kezdés


Befejezés


Terem


Maximum létszám


Aktuális létszám


Példa:
SpinningEdző: Kiss Anna2026.06.15.18:00–19:00Szabad helyek: 4

Foglalás
Jelentkezés
Gomb:
Jelentkezem
Rendszer:


ellenőrzi a szabad helyeket


létrehozza a foglalást


értesítést küld



Lemondás
Szabályok:


például 2 órával kezdés előtt ingyenes


utána figyelmeztetés vagy büntetőpont



Várólista
Ha betelt:
Várólistára jelentkezem
Lemondás esetén:


első várólistás automatikusan bekerül


értesítést kap



3. Teremkezelés
Egy teremhez:


Név


Cím


Leírás


Kapcsolatok


Nyitvatartás


Példa:
EdzésPont Debrecen

4. Edzőkezelés
Edző profil:


Név


Fotó


Bemutatkozás


Szakterület


Példák:


Crossfit


Jóga


TRX


Spinning



5. Értesítések
E-mail


Foglalás sikeres


Lemondás


Várólistáról bekerülés


Push értesítés (mobilnál)


Az óra 1 órán belül kezdődik


Felszabadult hely



6. Statisztikák
Teremvezető számára:


Legnépszerűbb órák


Kihasználtság


Lemondások száma


Edzőnkénti látogatottság


Grafikonok:


napi


heti


havi



7. Későbbi prémium funkciók
Bérletkezelés


10 alkalmas bérlet


Havi bérlet


Napijegy


Automatikus levonás foglaláskor.

Online fizetés
Integráció:


Stripe


Barion


SimplePay



QR-kódos beléptetés
Érkezéskor:
QR-kód beolvasása
Automatikus jelenlét.

Mobilalkalmazás


Android


iPhone


Főképernyő:


Következő foglalás


Mai órák


Gyors foglalás



8. Javasolt technológia
Ha egyedül fejleszted:
Backend


Golang


PostgreSQL


REST API


Frontend


React


TypeScript


Mobil


React Native


Hoszting


Hetzner vagy DigitalOcean



Adatbázis első verziója
Táblák:

users
roles

gyms
rooms

trainers

class_types
classes

bookings
waitlists

notifications

Ezzel már elkészíthető egy teljes értékű első verzió, amellyel több fitneszterem tudja kezelni az órarendjeit és a foglalásokat. A legfontosabb kérdés most az, hogy az EdzésPont egyetlen terem saját rendszere lesz, vagy országos platform több terem számára. Ez alapjaiban meghatározza az adatmodellt és az architektúrát.

A választott stack
Backend: Rust

Előnyök:

Nagyon gyors
Kevés memóriahasználat
Típusbiztos
Nagy terhelést is jól bír
Kiváló tanulási projekt

Hátrányok:

Lassabb fejlesztés
Meredekebb tanulási görbe
Kevesebb kész példa, mint Node.js vagy Go esetén

Ajánlott keretrendszer:

Axum

Alternatívák:

Actix Web
Rocket

Én ma új projekt esetén Axumot választanék.

Frontend: Vue 3

Az EdzésPontnak szerintem kifejezetten jó választás.

Ajánlott:

Vue.js
Pinia
Vue Router
Vuetify vagy PrimeVue
MongoDB

Itt már árnyaltabb a kép.

A legtöbb fitnesz-foglaló rendszer adatmodellje valójában relációs:

Felhasználó
   ↓
Foglalás
   ↓
Óra
   ↓
Terem
   ↓
Edző

Ez klasszikus SQL-terület.

Miért működhet mégis MongoDB-vel?

A legtöbb lekérdezés egyszerű:

Mai órák
Következő órák
Saját foglalások
Óra résztvevői

MongoDB ezt gond nélkül kezeli.

Javasolt dokumentumok
users
{
  "_id": "...",
  "email": "teszt@edzespont.hu",
  "name": "Kiss Péter",
  "role": "member"
}
trainers
{
  "_id": "...",
  "name": "Kiss Anna",
  "bio": "...",
  "specialties": [
    "jóga",
    "trx"
  ]
}
classes
{
  "_id": "...",
  "title": "Spinning",
  "trainerId": "...",
  "startAt": "2026-06-20T18:00:00Z",
  "endAt": "2026-06-20T19:00:00Z",
  "capacity": 20,
  "booked": 14
}
bookings
{
  "_id": "...",
  "userId": "...",
  "classId": "...",
  "status": "confirmed",
  "createdAt": "..."
}
Amit már az elején tervezz bele
Audit log

Nagyon hasznos.

{
  "userId": "...",
  "action": "BOOKING_CANCELLED",
  "timestamp": "..."
}

Később rengeteg problémát megold.

Soft delete

Ne törölj órákat.

Inkább:

{
  "deleted": true
}
Több terem támogatása

Akkor is, ha most csak egy terem lesz.

Minden dokumentumban legyen:

{
  "gymId": "..."
}

Később hálás leszel magadnak.

MVP funkciók
1. verzió
Regisztráció
Bejelentkezés
Órarend
Foglalás
Lemondás
Admin felület
Edzők kezelése
Termek kezelése

Semmi más.

2. verzió
Várólista
E-mail értesítés
Push értesítés
Bérletkezelés
3. verzió
Online fizetés
QR beléptetés
Mobilapp
Amit én másképp csinálnék

Ha most indulna a projekt, Rust mellett inkább egy relációs adatbázist választanék:

PostgreSQL

mert az EdzésPont központi entitása a foglalás, ami erősen kapcsolódik:

felhasználóhoz
órához
edzőhöz
teremhez

és ezekre sok összetett lekérdezés, egyediségi szabály és tranzakció kell.

Például garantálni akarod, hogy ugyanaz a felhasználó ne tudjon kétszer ugyanarra az órára jelentkezni, illetve hogy egy 20 fős órára ne kerüljön be a 21. ember. Ezek SQL-ben és tranzakciókkal természetesebben kezelhetők.

Ha viszont a célod részben az, hogy Rustot és MongoDB-t gyakorolj, akkor az Axum + MongoDB + Vue 3 + Pinia stack teljesen alkalmas egy professzionális EdzésPont MVP megépítésére. A legfontosabb tervezési döntés most szerintem az adatmodell és a foglalási folyamat (jelentkezés, lemondás, várólista) részletes kidolgozása lenne, mert ez lesz az egész rendszer magja.