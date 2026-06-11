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