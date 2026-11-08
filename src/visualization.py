import pandas as pd
import matplotlib.pyplot as plt

SALARY_FILE = "data/processed/salaries_clean.csv"
AI_FILE = "data/raw/ai_layoffs.csv"


def create_visualizations():

    # ==========================
    # SALAIRES
    # ==========================

    salaries_df = pd.read_csv(SALARY_FILE)

    top_jobs = (
        salaries_df.groupby("job_title")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    top_jobs.plot(kind="bar")
    plt.title("Top 10 Highest Paying Tech Jobs")
    plt.ylabel("Average Salary (USD)")
    plt.tight_layout()
    plt.savefig("visualizations/top_jobs.png")
    plt.close()

    top_countries = (
        salaries_df.groupby("company_location")["salary_in_usd"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    top_countries.plot(kind="bar")
    plt.title("Top 10 Highest Paying Countries")
    plt.ylabel("Average Salary (USD)")
    plt.tight_layout()
    plt.savefig("visualizations/top_countries.png")
    plt.close()

    experience = (
        salaries_df.groupby("experience_level")["salary_in_usd"]
        .mean()
    )

    plt.figure(figsize=(8, 5))
    experience.plot(kind="bar")
    plt.title("Average Salary by Experience Level")
    plt.ylabel("Average Salary (USD)")
    plt.tight_layout()
    plt.savefig("visualizations/experience_salary.png")
    plt.close()

    # ==========================
    # IA & LICENCIEMENTS
    # ==========================

    ai_df = pd.read_csv(AI_FILE)

    ai_df["Roles counted"] = pd.to_numeric(
        ai_df["Roles counted"],
        errors="coerce"
    )

    ai_df = ai_df.dropna(subset=["Roles counted"])

    # Top entreprises
    top_ai_companies = (
        ai_df.groupby("Company")["Roles counted"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))
    top_ai_companies.plot(kind="bar")
    plt.title("Top 10 Companies Most Impacted by AI Layoffs")
    plt.ylabel("Jobs Eliminated")
    plt.tight_layout()
    plt.savefig("visualizations/ai_top_companies.png")
    plt.close()

    # Top pays
    top_ai_countries = (
        ai_df.groupby("Country")["Roles counted"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))
    top_ai_countries.plot(kind="bar")
    plt.title("Top 10 Countries Impacted by AI Layoffs")
    plt.ylabel("Jobs Eliminated")
    plt.tight_layout()
    plt.savefig("visualizations/ai_top_countries.png")
    plt.close()

    # Top secteurs
    top_ai_sectors = (
        ai_df.groupby("Sector")["Roles counted"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(12, 6))
    top_ai_sectors.plot(kind="bar")
    plt.title("Top 10 Sectors Impacted by AI Layoffs")
    plt.ylabel("Jobs Eliminated")
    plt.tight_layout()
    plt.savefig("visualizations/ai_top_sectors.png")
    plt.close()

    print("Visualisations créées avec succès")


if __name__ == "__main__":
    create_visualizations()