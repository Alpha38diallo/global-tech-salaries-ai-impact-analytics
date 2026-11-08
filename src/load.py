import sqlite3
import pandas as pd

DB_FILE = "database/salaries.db"
SALARIES_FILE = "data/processed/salaries_clean.csv"
AI_FILE = "data/raw/ai_layoffs.csv"


def load_data():

    conn = sqlite3.connect(DB_FILE)

    # Chargement des salaires
    salaries_df = pd.read_csv(SALARIES_FILE)

    salaries_df.to_sql(
        "salaries",
        conn,
        if_exists="replace",
        index=False
    )

    print("Table salaries créée")

    # Chargement des licenciements IA
    ai_df = pd.read_csv(AI_FILE)

    ai_df.to_sql(
        "ai_layoffs",
        conn,
        if_exists="replace",
        index=False
    )

    print("Table ai_layoffs créée")

    conn.close()

    print("Chargement SQLite terminé avec succès")


if __name__ == "__main__":
    load_data()