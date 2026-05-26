[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Domen - Sistem online kurseva  
Aplikacija sluzi za kreiranje,pregled kurseva,prijavu studenata i pracenje napretka  

Sastoji se od dva entiteta : Course i Enrollment  


Student A je zaduzen za same kurseve.  
Student B je zaduzen za aktivnost - proces prijave i   pracenje kako student napreduje na tim kursevima.  


Resurs A : Course

Sastoji se od auto generisanog id,naziva kursa,kategorije,trajanja u satima,cijene,pocetnog i krajnjeg datuma kada je dostupan

Resurs B : Enrollment

Spaja studenta sa kursom i prati njegov status.
Sadrzi id,ime studenta,email,napredak,is_completed boolean ako je student zavrsio kurs,datum i vrijeme prijave i strani kljuc na resurs Course.


## Tim

- **Student A**: Emir Mahmutović - resurs: `/resursi_a`
- **Student B**: Amar Ašćić - resurs: `/resursi_b`

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi

### Resurs A: `/resursi_a`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/resursi_a` | Lista svih resursa (sa query filterom) |
| GET | `/resursi_a/{id}` | Dohvatanje resursa po ID-u |
| POST | `/resursi_a` | Kreiranje novog resursa |
| PUT | `/resursi_a/{id}` | Potpuna zamjena resursa |
| PATCH | `/resursi_a/{id}` | Djelimično ažuriranje resursa |
| DELETE | `/resursi_a/{id}` | Brisanje resursa |

**Primjer zahtjeva:**
```bash
# Kreiranje novog resursa
curl -X POST "http://localhost:8000/resursi_a" \
  -H "Content-Type: application/json" \
  -d '{"polje1": "vrijednost", "polje2": 123}'
```

### Resurs B: `/resursi_b`

[Analogno kao za Resurs A]

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]

**Student A: Emir Mahmutovic**

**Model:** ChatGpt i Github Copilot

- **Prompt:** Kreiraj klasu course sa id title category duration itd.
- **Kako je pomoglo:** Pomoglo mi je skontati tačko kakvu klasu hoću i kakvo je hoču postaviti
- **Prilagodbe:** U nekim slučajevima sam morao mijenjati kod koji je AI generisao


**Student B: Amar Ascic** 

**Model:** Google Gemini
- **Prompt:** Dobijam gresku 422 Unprocessable Entity kad apokusam uraditi PATCH. Evo slike greske i mog JSON-a, sta nije u redu?
- **Prompt:** Moj kolega je vec zavrsio svoj rad na grani Student_a. Kako da ja kreiram svoju granu Student_b tako da ona naslijedi njegov kod (jer mi trebaju njegovi modeli),ali da moji commitovi ostanu odvojeni kako ne bismo jedan drugom gazili po kodu ?

**Pomoc i prilagodbe:**
AI mi je razjasnio nedoumicu oko grananja u zajednickom repozitoriju. Koristen je kao real-time asistent i alat koji je brzo generisao CRUD operacije kako bih ustedio vrijeme pisajuci redundantan kod. Takodje, pomogao mi je u otklanjanju gresaka. Morao sam naravno prilagodjavati kod kolegi,da se odrzi konzistentnost projekta i da postavljam dodatna pitanja kako bih se naucio "npr. sta je router..." 
## Napomene

Nikakve dodatne napomene,kod je u skladu sa zahtjevima u zadaci.

## Zadatak na lab-u overview

Dodana stroza kontrola unosa podataka pomocu field_validator metoda:
-Vremenski okvir end_date mora biti nakon start_date
-Polje progress mora biti unutar raspona od 0 do 100
Ako nije ispunjen zahtjev,vraca se ValueError

Novi Endpoint-ovi
URL /statistika metod GET
Opis: Izracunava prosjecnu cijenu kurseva
Ispisuje ukupan broj upisanih studenata
U slucaju praznog .db ispisuje se 0 . 

Dodani field_validatori metodi za:
duration_hours da ne mogu biti 0 ili negativan broj. Poruka "duration_hours must be a positive number"
student_name da duzina imena ne moze imat 1 ili manje karaktera. Poruka "student_name cannot be empty"

U POST Endpoint-e su dodani HTTPException:
U Course da cijena ne smije biti vise od 1000
U Enrollment je dodano da ne smije biti student sa istim email-om koji vec postoji u bazi

Novi POST Endpoint-i:
URL /search 
Ovi Endpoint pretrazuju bazu za Course pod oderdenom imenu i Enrollment pod odredenom email-u