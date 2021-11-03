from src.data_engineering.dags.config_dag import PROCESSES
from src.data_engineering.utils.utils import create_database


def run_data_processing(process_name: str, write_database: str, environment: str):
    """
    EXECUTION SCRIPT

    This is the entry point of the project, all different dags gets executed from this function.
    Whilst building the pipeline, this script gets copied at shared location in databricks and
    it is called in datafactory jobs with relevant parameters.

    Data is divided in below fashion

    - raw - apply schema to files
    - historic - apply schema to files ( one off historic load , e.g. sap bw data)
    - consolidated - makes reusable table with some amount of transformation which can be common among business
    - feature - IPM specific transformation i.e. data that goes into reporting or modelling

    Currently it calls below parameters (i.e. different processes)

    - Raw manual files
    - Historic layer
    - Daily view consolidated
    - Weekly stock consolidated
    - Capacity control feature
    - Finance planner feature
    - Prophet feature
    - Supply planner consolidated (DOS and actuals)
    - supply planner Feature (DOS and actuals)

    All above processes gets called by a function, and written to hive table via the list of tables
    passed from constant files. All hive tables have schema and they get overwritten on every run.

    :param process_name: name of the process - i.e. feature layer, consolidated layer etc
    :return: This function returns None- as it is executes dag and writes data to
    the hive tables. Further information could be found in the relevant sections.
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
    run_data_processing("GITHUB_PULL", "github_exercise", 'chrome-ability-329607')
