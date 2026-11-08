import pandas as pd

INPUT_FILE = "data/processed/salaries_clean.csv"


def run_analysis():
    df = pd.read_csv(INPUT_FILE)

    print("\n=== Top 10 métiers les mieux payés ===")

    top_jobs = (
        df.groupby("job_title")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .round(0)
    )

    print(top_jobs)

    print("\n=== Top 10 pays les mieux payés ===")

    top_countries = (
        df.groupby("company_location")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .round(0)
    )

    print(top_countries)

    print("\n=== Salaire moyen par niveau d'expérience ===")

    experience_salary = (
        df.groupby("experience_level")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .round(0)
    )

    print(experience_salary)

    print("\n=== Salaire moyen par taille d'entreprise ===")

    company_size_salary = (
        df.groupby("company_size")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .round(0)
    )

    print(company_size_salary)


if __name__ == "__main__":
    run_analysis()