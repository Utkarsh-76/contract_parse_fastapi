# Contract Parse

This is a python application that is used to extract contracts from a website, parse the data and save/send it in tabular data

## 1. Clone the repo:

```bash
git clone https://github.com/Utkarsh-76/contract_parse_fastapi.git
```

## 2. Install packages from requirements.txt:

```bash
pip3 install -r requirements.txt
```

## 3. Setup database:

Setup a Postgres database in local and update "SQLALCHEMY_DATABASE_URL" in database.py file

## 4. Run the application

```bash
uvicorn app:app
```

## Functionality

- Data extraction and pdf extraction from a website
- Parsing the extracted pdf/data
- Saving the data in excel and send it via email
- Stripe integration for payment support

## Technical Highlights

- FastAPI used for Application development
- Data validation done using Pydantic
- ORM(Database management) is SQLAlchemy
- Modular structure for easy development
- Database - Postgres
- Data Scrapping - selenium

## Support

Use [this link](https://calendly.com/agarwal-ut76/30min) if you need any support for this repo or python in general
