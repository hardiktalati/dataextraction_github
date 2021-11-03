import requests
from pandas.io.json import json_normalize
from src.data_engineering.config import config

github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)

url = github_api + '/repos/apache/spark/commits'
url1 = github_api + '/repos/apache/spark/pulls'
commits = gh_session.get(url=url)
commits_json = commits.json()


def repo_github(repo, owner, api, extract):
    """
     This function reads from github api, it iterates over the pages and can bring the information about
     pull requests, commits, gist and much more.

    :param repo: The repo we want to extract the information for e.g. spark , pandas
    :param owner: Owner of the repo e.g apache, pydata.
    :param api: Credentials to acess the github api
    :param extract: Information we need to extract pulls, commits etc
    :return: Extracted information in a dictionary format
    """
    gh_session = requests.Session()
    gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)
    commits = []
    next = True
    i = 1
    while next == True:
        url = api + '/repos/{}/{}/{}?page={}&per_page=100'.format(owner, repo, extract, i)
        commit_pg = gh_session.get(url=url)

        commit_pg_list = [dict(item, **{'repo_name': '{}'.format(repo)}) for item in commit_pg.json()]

        commit_pg_list = [dict(item, **{'owner': '{}'.format(owner)}) for item in commit_pg_list]

        commits = commits + commit_pg_list

        if 'Link' in commit_pg.headers:
            if 'rel="next"' not in commit_pg.headers['Link']:
                next = False
        i = i + 1
    return commits


def create_commits_df(repo, owner, api, extract):
    """
    Once the data is extracted from the git, it gets normalised and gets converted as a dataframe.

    :param repo: Repo which data needs to be extracted
    :param owner: Owner of the repo e.g. apache , pydata
    :param api: Your github credentials
    :param function: Function to extract the pull, commits etc
    :param extract:
    :return: pandas dataframe which is further used to write to big query
    """
    commits_list = repo_github(repo, owner, api, extract)
    commits = json_normalize(commits_list)
    commits.columns = commits.columns.str.replace(".", "_")
    return commits

#
#
# def commits_of_repo_github(repo, owner, api):
#     commits = []
#     next = True
#     i = 1
#     while next == True:
#         url = api + '/repos/{}/{}/commits?page={}&per_page=100'.format(owner, repo, i)
#         commit_pg = gh_session.get(url=url)
#
#         commit_pg_list = [dict(item, **{'repo_name': '{}'.format(repo)}) for item in commit_pg.json()]
#
#         commit_pg_list = [dict(item, **{'owner': '{}'.format(owner)}) for item in commit_pg_list]
#
#         commits = commits + commit_pg_list
#
#         if 'Link' in commit_pg.headers:
#             if 'rel="next"' not in commit_pg.headers['Link']:
#                 next = False
#         i = i + 1
#     return commits
#
#
# def pulls_of_repo(repo, owner, api):
#     pulls = []
#     next = True
#     i = 1
#     while next == True:
#         url = api + '/repos/{}/{}/pulls?page={}&per_page=100'.format(owner, repo, i)
#         pull_pg = gh_session.get(url=url)
#         pull_pg_list = [dict(item, **{'repo_name': '{}'.format(repo)}) for item in pull_pg.json()]
#         pull_pg_list = [dict(item, **{'owner': '{}'.format(owner)}) for item in pull_pg_list]
#         pulls = pulls + pull_pg_list
#         if 'Link' in pull_pg.headers:
#             if 'rel="next"' not in pull_pg.headers['Link']:
#                 next = False
#         i = i + 1
#     return pulls
