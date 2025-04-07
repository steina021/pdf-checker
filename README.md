## Hvordan kjøre prosjektet lokalt:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 

### API-testing så langt
- gå til /pdfchecker/api/loggers/create
- /pdfchecker/api/loggers returnerer det som er lagret.
- du vil få opp en POST content side, her må du gjøre følgende:

```json
{
    "test": "SKRIV NOE HER"
}
```

skriv det i content-boksen for å teste API-et, viktig at dere prøver ut dette slik at dere skjønner dette.