from transform import clean_salaries_data
from analysis import run_analysis
from load import load_data
from visualization import create_visualizations
from ai_analysis import analyze_ai_impact


def run_pipeline():

    print("=== TRANSFORMATION ===")
    clean_salaries_data()

    print("\n=== ANALYSE ===")
    run_analysis()

    print("\n=== IMPACT DE L'IA ===")
    analyze_ai_impact()

    print("\n=== VISUALISATIONS ===")
    create_visualizations()

    print("\n=== CHARGEMENT SQLITE ===")
    load_data()

    print("\nPipeline terminé avec succès")


if __name__ == "__main__":
    run_pipeline()