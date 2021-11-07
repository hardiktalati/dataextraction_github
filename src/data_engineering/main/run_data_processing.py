from src.data_engineering.dags.config_dag import PROCESSES
from src.data_engineering.utils.utils import create_database


def run_data_processing(process_name: str, write_database: str, environment: str):
    """
    EXECUTION SCRIPT

    This is the entry point of the project, all different dags gets executed from this function.
    Whilst building the pipeline, this script gets copied at shared location in databricks and
    and it can be scheduled using databricks scheduler. Parameters from this notebook would be passed
    to another runscript to accommodate the dbutils library specific to datbaricks. Argparse can also
    be used instead of dbutils.

    When the script gets executed below steps takes place

    1). Creates dataset (database if it does not exist).
    2). Executes the pipeline or multiple pipelines.
    3). Writes the data to the google big query.

    :param process_name: name of the process - i.e. feature layer, consolidated layer etc. It gets picked up from the dags_config and is passed as a parameter.
    :param write_database: Name of the dataset where it needs to write.
    :param environment: Project ID details.
    :return: This function returns None- as it is executes dag and writes data to
    the google big query. Further information could be found in the relevant sections.
    """
    # LOG.info("running data processing")
    process_dict = PROCESSES

    create_database(environment, write_database)
    # assign functions
    function_to_run = process_dict[process_name]
    function_to_run()
    # function_to_create_tables(spark, environment, write_database)
    # read the data for the process


if __name__ == "__main__":
    # args = parser.ArgumentParser()
    # rdp_args = {
    #     "process_name": args.process_name,
    #     "write_database": args.write_database,
    #     "enviornment": args.enviornment}
    # run_data_processing(**rdp_args)
    run_data_processing(process_name="GITHUB_PULL", write_database="github_exercise", environment='chrome-ability-329607')
