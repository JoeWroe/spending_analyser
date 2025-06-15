# Spending Analyser

## :chart_with_upwards_trend: Project Overview
**Spending Analyser** is a personal finance tool which helps you better understand your finances, especially your spending. It works by ingesting a `.csv` of your bank statement, writting it to a database and exposing the data as an API. The future goal of the project will be to use that API to perform analysis, create views and charts, catagorise, filter and understand your spending.

### Currently Supported Bank Statements
Monzo

---

## :wrench: Current Features
- `.csv` ingestion for Monzo bank statements
- Parsing of the stements into transactions
- Storage of transactions in a local database
- ReSTful API to access transactions

## :building_construction: Future Features
- Support for more bank statements

---

## :open_file_folder: Project Structure
```plaintext
│
├── app/                                # Core application logic
│   ├── models/                         # Database models
│   │   └── transaction.py              # Transaction model
│   ├── api.py                          # API endpoints
│   ├── database.py                     # Database connection
│   └── ingest.py                       # Ingestion logic
│
├── test
│   └── unit/
│       ├── model/
│       │    └── test_transaction.py    # Unit tests for Transaction model
│       ├── test_api.py                 # Unit tests for API
│       ├── test_database.py            # Unit tests for Database
│       └── test_ingest.py              # Unit tests for Ingestion
│
├── .gitignore                          # Files to ignore in git
├── README.md                           # Project documentation
├── main.py                             # Entry point for the application
├── pytest.ini                          # Pytest configuration
├── requirements.txt                    # Python dependencies
└── setup.py                            # Setup script for packaging

```

---

