import os

from google.cloud import bigquery

credentials_path = '../config/chrome-ability-329607-a80ecc183be3.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
table_id = 'chrome-ability-329607.temp.temp1'


def dataset_exists(project, database):
    from google.cloud import bigquery
    from google.cloud.exceptions import NotFound
    client = bigquery.Client()

    dataset_id = "{0}.{1}".format(project, database)
    print(dataset_id)
    try:
        client.get_dataset(dataset_id)  # Make an API request.
        print("database {} already exists.".format(dataset_id))
        return True
    except NotFound:
        print("database {} is not found.".format(dataset_id))
        return False
    # [END bigquery_table_exists]


def create_database(project, dataset_id):
    # [START bigquery_create_dataset]
    from google.cloud import bigquery

    credentials_path = '../config/chrome-ability-329607-a80ecc183be3.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
    client = bigquery.Client()
    if dataset_exists(project, dataset_id) == False:
        # Construct a BigQuery client object.

        # TODO(developer): Set dataset_id to the ID of the dataset to create.
        dataset_id = "{}.{}".format(project, dataset_id)

        # Construct a full Dataset object to send to the API.
        dataset = bigquery.Dataset(dataset_id)

        # TODO(developer): Specify the geographic location where the dataset should reside.
        dataset.location = "EU"

        # Send the dataset to the API for creation, with an explicit timeout.
        # Raises google.api_core.exceptions.Conflict if the Dataset already
        # exists within the project.
        dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
        return print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
    else:
        return print("Dataset exist {}.{}".format(client.project, dataset_id))


#
# def create_database(dataset_id):
#     # [START bigquery_create_dataset]
#     from google.cloud import bigquery
#
#     # Construct a BigQuery client object.
#     client = bigquery.Client()
#
#     # TODO(developer): Set dataset_id to the ID of the dataset to create.
#     # dataset_id = "{}.your_dataset".format(client.project)
#
#     # Construct a full Dataset object to send to the API.
#     dataset = bigquery.Dataset(dataset_id)
#
#     # TODO(developer): Specify the geographic location where the dataset should reside.
#     dataset.location = "EU"
#
#     # Send the dataset to the API for creation, with an explicit timeout.
#     # Raises google.api_core.exceptions.Conflict if the Dataset already
#     # exists within the project.
#     dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
#     return print("Created dataset {}.{}".format(client.project, dataset.dataset_id))


def make_schema():
    schema = [
        bigquery.SchemaField(name="string", field_type="STRING", description="This is my string."),
        bigquery.SchemaField(name="numeric", field_type="FLOAT", description="This is my float."),
    ]

    return schema


def table_exists(project, database, table):
    # [START bigquery_table_exists]
    from google.cloud import bigquery
    from google.cloud.exceptions import NotFound

    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to determine existence.
    table_id = "{0}.{1}.{2}".format(project, database, table)

    try:
        client.get_table(table_id)  # Make an API request.
        print("Table {} already exists.".format(table_id))
        return True
    except NotFound:
        print("Table {} is not found.".format(table_id))
        return False
    # [END bigquery_table_exists]


def create_external_tables(schema, database: str, table_name: str, file_format: str, project: str):
    """
    This function creates external tables in big query. Before creating table it checks
    if table exist, and in a scenario if it exist then it does not recreate the table.

    :param schema: Schema for creating the table
    :param database: Dataset in big query where table gets stored
    :param table_name: Name of the table also location in cloud storage for storing table
    :param file_format: Format in which data is saved
    :param location: Google cloud storage location
    :param project: Project id
    :return: Print statement on if the table has been created or there is no need of creating the table.
    """
    table_check = table_exists(project, database, table_name)
    if table_check == False:
        print("table not present")
        client = bigquery.Client()
        dataset_ref = client.dataset(database)
        table_ref = bigquery.TableReference(dataset_ref, table_name)
        table = bigquery.Table(table_ref, schema)
        external_config = bigquery.ExternalConfig(file_format)
        source_uris = ['gs://bucket/ht_temp/{0}'.format(table_name)]
        external_config.source_uris = source_uris
        table.external_data_configuration = external_config
        client.create_table(table)
        return print('table_created')
    else:
        return print("not created")


def create_schema(dictionary_of_variables):
    schema = []
    for k, v in dictionary_of_variables.items():
        print((bigquery.SchemaField(k, v)))
        a = (bigquery.SchemaField(k, v))
        schema.append(a)
    return schema


def upload_df_to_bq(df, project, bq_table):
    df.to_gbq(bq_table, project_id=project, if_exists='replace')
