from src.data_engineering.dags.pull_dag import get_pulls_to_gcp
# This is the dictionary of parameters to be called.

PROCESSES = {"GITHUB_PULL": (get_pulls_to_gcp)}
