import pandas as pd
from pathlib import Path

RAW_FILE = "data/raw/salaries_raw.csv"
OUTPUT_FILE = "data/processed/salaries_clean.csv"


def clean_salaries_data():
    print("Chargement des données...")

    df = pd.read_csv(RAW_FILE)

    # Uniformiser les noms de colonnes
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )

    # Supprimer doublons
    df = df.drop_duplicates()

    # Supprimer lignes sans salaire
    df = df.dropna(subset=["salary_in_usd"])

    # Supprimer colonnes entièrement vides
    df = df.dropna(axis=1, how="all")

    # Supprimer valeurs aberrantes
    df = df[df["salary_in_usd"] > 1000]

    # Sauvegarde
    Path("data/processed").mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"{len(df)} lignes nettoyées sauvegardées dans {OUTPUT_FILE}")


if __name__ == "__main__":
    clean_salaries_data()