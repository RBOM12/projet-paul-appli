import sqlite3
from config import DATABASE_PATH

def create_tables():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS flex_calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DHIV REAL,
            Compensation REAL,
            K1 REAL,
            K2 REAL,
            Excentricité REAL,
            DlA REAL,
            DFLRGP REAL,
            R0 REAL,
            Flexibility REAL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS lunette_lentilles_calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            DHIV REAL,
            Compensation REAL,
            K1 REAL,
            K2 REAL,
            Excentricité REAL,
            DlA REAL,
            DFLRGP REAL,
            R0 REAL,
            Flexibility REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(DHIV, Compensation, K1, K2, Excentricité, DlA, DFLRGP, R0, Flexibility):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO flex_calculations (DHIV, Compensation, K1, K2, Excentricité, DlA, DFLRGP, R0, Flexibility)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (DHIV, Compensation, K1, K2, Excentricité, DlA, DFLRGP, R0, Flexibility))

    c.execute('''
        INSERT INTO lunette_lentilles_calculations (DHIV, Compensation, K1, K2, Excentricité, DlA, DFLRGP, R0, Flexibility)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (DHIV, Compensation, K1, K2, Excentricité, DlA, DFLRGP, R0, Flexibility))

    conn.commit()
    conn.close()

# Crée les tables à l'initialisation du module
create_tables()
