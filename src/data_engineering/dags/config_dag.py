from src.data_engineering.dags.pull_dag import get_pulls_to_gcp

PROCESSES = {"GITHUB_PULL": (get_pulls_to_gcp)}
