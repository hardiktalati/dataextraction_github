from src.data_engineering.constants import GITHUB_API, APACHE, SPARK, PULLS, PROJECT_ID, GITHUB_PULL
from src.data_engineering.consolidated.data_extraction import create_commits_df
from src.data_engineering.utils.utils import upload_df_to_bq


def get_pulls_to_gcp():
    """
    This function gets called in main script. It is the collection of activity that needs to happen in a cyclic manner to achieve
    desired result. Ideally the write part should be handled seperately. However it is out of scope for this exercise.

    :return: None - Writes the final output to Big query. It overwrites every time it runs. As the data is of small size it
    carries out full extraction. In a real life scenario it would be handled acid transaction for efficient storage and
    processing.
    """
    PULL_DF = create_commits_df(SPARK, APACHE, GITHUB_API, PULLS)

    return upload_df_to_bq(PULL_DF, PROJECT_ID, GITHUB_PULL)
