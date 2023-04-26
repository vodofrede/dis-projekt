# DIS Projekt

## Installation / kørsel

Kræver Python 3+ installeret og tilgængelig på PATH.

For at installere requirements og køre appen:  
**Windows**: `start.bat`.  
**Unix**: `./start.sh` (kræver bash).

## Database

Til debugging laves der en `test.db` fil i projektroden. 
Når databaseskemaet ændres, bør `flask --app src/app.py db migrate` køres for at opdatere databasen.

## Ideer

- Bank
- Stock exchange / crypto
- Twitter
- Webshop
- Musik/Spil ratings
- Gambling/Betting
- Statistik i esport spil
