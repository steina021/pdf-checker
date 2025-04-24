# PDFChecker – API for validering av PDF-filer

Dette prosjektet tilbyr et API for håndtering og validering av PDF-filer, inkludert logging av valideringer. Du kan teste tjenesten både lokalt og via den deployede versjonen på Railway.

---

## Produksjons-URL

API-et er tilgjengelig her:

```
https://pdf-checker.up.railway.app/pdfchecker/
```

---

## Kjør prosjektet lokalt

Følg disse stegene i terminalen:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## API-endepunkter

- `POST /pdfchecker/api/loggers/create` – Oppretter ny logg for en PDF
- `GET /pdfchecker/api/loggers` – Returnerer eksisterende logger

Disse finnes både lokalt (`http://localhost:8000`) og i produksjon (`https://pdf-checker.up.railway.app`).

---

## Hvordan sjekke en PDF med URL

Du kan sjekke en PDF både lokalt og i produksjon. Her er fremgangsmåten:

### 1. Velg hvilken URL du vil bruke

| Miljø        | Base-URL                                    |
|--------------|----------------------------------------------|
| Lokalt       | `http://localhost:8000/pdfchecker/`         |
| Produksjon   | `https://pdf-checker.up.railway.app/pdfchecker/` |

### 2. Send en POST-request til `/api/loggers/create`

Bruk et API-verktøy som [Postman](https://www.postman.com/) eller [Thunder Client](https://www.thunderclient.com/).

Body/Content-type: `application/json`

Eksempel på JSON:

```json
{
    "pdf_url": "https://example.com/din-fil.pdf",
    "password": ""
}
```

- `"pdf_url"`: Lenken til PDF-en du ønsker å validere.
- `"password"`: Valgfritt – kun nødvendig om PDF-en er passordbeskyttet.

### 3. Se responsen

Du vil få en respons som bekrefter om PDF-en kunne åpnes, og eventuell tilleggsinformasjon logges.

---

## Avhengigheter

Alle nødvendige pakker er listet i `requirements.txt`. Installer dem slik:

```bash
pip install -r requirements.txt
```

---

## Tips

- Test både GET og POST-endepunktene.
- Bruk faktiske offentlige PDF-er for å teste funksjonaliteten.
- Husk å aktivere virtuelt miljø før du starter prosjektet lokalt.
