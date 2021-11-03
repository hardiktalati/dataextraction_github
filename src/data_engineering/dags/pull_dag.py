from src.data_engineering.constants import GITHUB_API, APACHE, SPARK, PULLS, PROJECT_ID, GITHUB_PULL
from src.data_engineering.consolidated.data_extraction import create_commits_df
from src.data_engineering.utils.utils import upload_df_to_bq


def get_pulls_to_gcp():
    """

    :return:
    """
    PULL_DF = create_commits_df(SPARK, APACHE, GITHUB_API, PULLS)

    return upload_df_to_bq(PULL_DF, PROJECT_ID, GITHUB_PULL)
