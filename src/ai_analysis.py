import pandas as pd

INPUT_FILE = "data/raw/ai_layoffs.csv"


def analyze_ai_impact():

    df = pd.read_csv(INPUT_FILE)

    print("\n=== AI LAYOFFS ANALYSIS ===")

    print(f"Nombre total d'événements : {len(df)}")

    # Conversion en numérique
    df["Roles counted"] = pd.to_numeric(
        df["Roles counted"],
        errors="coerce"
    )

    # Suppression des valeurs manquantes
    df = df.dropna(subset=["Roles counted"])

    print("\n=== Top 10 entreprises les plus touchées ===")

    top_companies = (
        df.groupby("Company")["Roles counted"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_companies)

    print("\n=== Top 10 pays les plus touchés ===")

    top_countries = (
        df.groupby("Country")["Roles counted"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_countries)

    print("\n=== Top 10 secteurs les plus touchés ===")

    top_sectors = (
        df.groupby("Sector")["Roles counted"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print(top_sectors)

    print("\n=== Impact moyen sur les effectifs (%) ===")

    if "% of workforce" in df.columns:

        workforce = (
            df["% of workforce"]
            .astype(str)
            .str.replace("%", "", regex=False)
        )

        workforce = pd.to_numeric(
            workforce,
            errors="coerce"
        )

        print(
        f"{workforce.mean():.2f}% des effectifs touchés en moyenne"
        )


if __name__ == "__main__":
    analyze_ai_impact()