PULLS = "pulls"
GITHUB_API = "https://api.github.com"
SPARK = "spark"
APACHE = "apache"
TOKEN = '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'
PROJECT_ID = 'chrome-ability-329607'
DATABASE = "github_exercise"
GITHUB_PULL = "github_exercise.github_pull"
PROJECT_NAME = "github_sample"

PULLS_SCHEMA = {'url': 'string', 'id': 'int64', 'node_id': 'string', 'html_url': 'string', 'diff_url': 'string',
                'patch_url': 'string', 'issue_url': 'string', 'number': 'int64', 'state': 'string', 'locked': 'bool',
                'title': 'string', 'body': 'string', 'created_at': 'string', 'updated_at': 'string',
                'closed_at': 'string', 'merged_at': 'string', 'merge_commit_sha': 'string', 'assignee': 'string',
                'assignees': 'string', 'requested_reviewers': 'string', 'requested_teams': 'string', 'labels': 'string',
                'milestone': 'string', 'draft': 'bool', 'commits_url': 'string', 'review_comments_url': 'string',
                'review_comment_url': 'string', 'comments_url': 'string', 'statuses_url': 'string',
                'author_association': 'string', 'auto_merge': 'string', 'active_lock_reason': 'string',
                'repo_name': 'string', 'owner': 'string', 'user_login': 'string', 'user_id': 'int64',
                'user_node_id': 'string', 'user_avatar_url': 'string', 'user_gravatar_id': 'string',
                'user_url': 'string', 'user_html_url': 'string', 'user_followers_url': 'string',
                'user_following_url': 'string', 'user_gists_url': 'string', 'user_starred_url': 'string',
                'user_subscriptions_url': 'string', 'user_organizations_url': 'string', 'user_repos_url': 'string',
                'user_events_url': 'string', 'user_received_events_url': 'string', 'user_type': 'string',
                'user_site_admin': 'bool', 'head_label': 'string', 'head_ref': 'string', 'head_sha': 'string',
                'head_user_login': 'string', 'head_user_id': 'int64', 'head_user_node_id': 'string',
                'head_user_avatar_url': 'string', 'head_user_gravatar_id': 'string', 'head_user_url': 'string',
                'head_user_html_url': 'string', 'head_user_followers_url': 'string',
                'head_user_following_url': 'string', 'head_user_gists_url': 'string', 'head_user_starred_url': 'string',
                'head_user_subscriptions_url': 'string', 'head_user_organizations_url': 'string',
                'head_user_repos_url': 'string', 'head_user_events_url': 'string',
                'head_user_received_events_url': 'string', 'head_user_type': 'string', 'head_user_site_admin': 'bool',
                'head_repo_id': 'float64', 'head_repo_node_id': 'string', 'head_repo_name': 'string',
                'head_repo_full_name': 'string', 'head_repo_private': 'string', 'head_repo_owner_login': 'string',
                'head_repo_owner_id': 'float64', 'head_repo_owner_node_id': 'string',
                'head_repo_owner_avatar_url': 'string', 'head_repo_owner_gravatar_id': 'string',
                'head_repo_owner_url': 'string', 'head_repo_owner_html_url': 'string',
                'head_repo_owner_followers_url': 'string', 'head_repo_owner_following_url': 'string',
                'head_repo_owner_gists_url': 'string', 'head_repo_owner_starred_url': 'string',
                'head_repo_owner_subscriptions_url': 'string', 'head_repo_owner_organizations_url': 'string',
                'head_repo_owner_repos_url': 'string', 'head_repo_owner_events_url': 'string',
                'head_repo_owner_received_events_url': 'string', 'head_repo_owner_type': 'string',
                'head_repo_owner_site_admin': 'string', 'head_repo_html_url': 'string',
                'head_repo_description': 'string', 'head_repo_fork': 'string', 'head_repo_url': 'string',
                'head_repo_forks_url': 'string', 'head_repo_keys_url': 'string',
                'head_repo_collaborators_url': 'string', 'head_repo_teams_url': 'string',
                'head_repo_hooks_url': 'string', 'head_repo_issue_events_url': 'string',
                'head_repo_events_url': 'string', 'head_repo_assignees_url': 'string',
                'head_repo_branches_url': 'string', 'head_repo_tags_url': 'string', 'head_repo_blobs_url': 'string',
                'head_repo_git_tags_url': 'string', 'head_repo_git_refs_url': 'string', 'head_repo_trees_url': 'string',
                'head_repo_statuses_url': 'string', 'head_repo_languages_url': 'string',
                'head_repo_stargazers_url': 'string', 'head_repo_contributors_url': 'string',
                'head_repo_subscribers_url': 'string', 'head_repo_subscription_url': 'string',
                'head_repo_commits_url': 'string', 'head_repo_git_commits_url': 'string',
                'head_repo_comments_url': 'string', 'head_repo_issue_comment_url': 'string',
                'head_repo_contents_url': 'string', 'head_repo_compare_url': 'string', 'head_repo_merges_url': 'string',
                'head_repo_archive_url': 'string', 'head_repo_downloads_url': 'string',
                'head_repo_issues_url': 'string', 'head_repo_pulls_url': 'string', 'head_repo_milestones_url': 'string',
                'head_repo_notifications_url': 'string', 'head_repo_labels_url': 'string',
                'head_repo_releases_url': 'string', 'head_repo_deployments_url': 'string',
                'head_repo_created_at': 'string', 'head_repo_updated_at': 'string', 'head_repo_pushed_at': 'string',
                'head_repo_git_url': 'string', 'head_repo_ssh_url': 'string', 'head_repo_clone_url': 'string',
                'head_repo_svn_url': 'string', 'head_repo_homepage': 'string', 'head_repo_size': 'float64',
                'head_repo_stargazers_count': 'float64', 'head_repo_watchers_count': 'float64',
                'head_repo_language': 'string', 'head_repo_has_issues': 'string', 'head_repo_has_projects': 'string',
                'head_repo_has_downloads': 'string', 'head_repo_has_wiki': 'string', 'head_repo_has_pages': 'string',
                'head_repo_forks_count': 'float64', 'head_repo_mirror_url': 'float64', 'head_repo_archived': 'string',
                'head_repo_disabled': 'string', 'head_repo_open_issues_count': 'float64',
                'head_repo_license_key': 'string', 'head_repo_license_name': 'string',
                'head_repo_license_spdx_id': 'string', 'head_repo_license_url': 'string',
                'head_repo_license_node_id': 'string', 'head_repo_allow_forking': 'string',
                'head_repo_is_template': 'string', 'head_repo_topics': 'string', 'head_repo_visibility': 'string',
                'head_repo_forks': 'float64', 'head_repo_open_issues': 'float64', 'head_repo_watchers': 'float64',
                'head_repo_default_branch': 'string', 'base_label': 'string', 'base_ref': 'string',
                'base_sha': 'string', 'base_user_login': 'string', 'base_user_id': 'int64',
                'base_user_node_id': 'string', 'base_user_avatar_url': 'string', 'base_user_gravatar_id': 'string',
                'base_user_url': 'string', 'base_user_html_url': 'string', 'base_user_followers_url': 'string',
                'base_user_following_url': 'string', 'base_user_gists_url': 'string', 'base_user_starred_url': 'string',
                'base_user_subscriptions_url': 'string', 'base_user_organizations_url': 'string',
                'base_user_repos_url': 'string', 'base_user_events_url': 'string',
                'base_user_received_events_url': 'string', 'base_user_type': 'string', 'base_user_site_admin': 'bool',
                'base_repo_id': 'int64', 'base_repo_node_id': 'string', 'base_repo_name': 'string',
                'base_repo_full_name': 'string', 'base_repo_private': 'bool', 'base_repo_owner_login': 'string',
                'base_repo_owner_id': 'int64', 'base_repo_owner_node_id': 'string',
                'base_repo_owner_avatar_url': 'string', 'base_repo_owner_gravatar_id': 'string',
                'base_repo_owner_url': 'string', 'base_repo_owner_html_url': 'string',
                'base_repo_owner_followers_url': 'string', 'base_repo_owner_following_url': 'string',
                'base_repo_owner_gists_url': 'string', 'base_repo_owner_starred_url': 'string',
                'base_repo_owner_subscriptions_url': 'string', 'base_repo_owner_organizations_url': 'string',
                'base_repo_owner_repos_url': 'string', 'base_repo_owner_events_url': 'string',
                'base_repo_owner_received_events_url': 'string', 'base_repo_owner_type': 'string',
                'base_repo_owner_site_admin': 'bool', 'base_repo_html_url': 'string', 'base_repo_description': 'string',
                'base_repo_fork': 'bool', 'base_repo_url': 'string', 'base_repo_forks_url': 'string',
                'base_repo_keys_url': 'string', 'base_repo_collaborators_url': 'string',
                'base_repo_teams_url': 'string', 'base_repo_hooks_url': 'string',
                'base_repo_issue_events_url': 'string', 'base_repo_events_url': 'string',
                'base_repo_assignees_url': 'string', 'base_repo_branches_url': 'string', 'base_repo_tags_url': 'string',
                'base_repo_blobs_url': 'string', 'base_repo_git_tags_url': 'string', 'base_repo_git_refs_url': 'string',
                'base_repo_trees_url': 'string', 'base_repo_statuses_url': 'string',
                'base_repo_languages_url': 'string', 'base_repo_stargazers_url': 'string',
                'base_repo_contributors_url': 'string', 'base_repo_subscribers_url': 'string',
                'base_repo_subscription_url': 'string', 'base_repo_commits_url': 'string',
                'base_repo_git_commits_url': 'string', 'base_repo_comments_url': 'string',
                'base_repo_issue_comment_url': 'string', 'base_repo_contents_url': 'string',
                'base_repo_compare_url': 'string', 'base_repo_merges_url': 'string', 'base_repo_archive_url': 'string',
                'base_repo_downloads_url': 'string', 'base_repo_issues_url': 'string', 'base_repo_pulls_url': 'string',
                'base_repo_milestones_url': 'string', 'base_repo_notifications_url': 'string',
                'base_repo_labels_url': 'string', 'base_repo_releases_url': 'string',
                'base_repo_deployments_url': 'string', 'base_repo_created_at': 'string',
                'base_repo_updated_at': 'string', 'base_repo_pushed_at': 'string', 'base_repo_git_url': 'string',
                'base_repo_ssh_url': 'string', 'base_repo_clone_url': 'string', 'base_repo_svn_url': 'string',
                'base_repo_homepage': 'string', 'base_repo_size': 'int64', 'base_repo_stargazers_count': 'int64',
                'base_repo_watchers_count': 'int64', 'base_repo_language': 'string', 'base_repo_has_issues': 'bool',
                'base_repo_has_projects': 'bool', 'base_repo_has_downloads': 'bool', 'base_repo_has_wiki': 'bool',
                'base_repo_has_pages': 'bool', 'base_repo_forks_count': 'int64', 'base_repo_mirror_url': 'string',
                'base_repo_archived': 'bool', 'base_repo_disabled': 'bool', 'base_repo_open_issues_count': 'int64',
                'base_repo_license_key': 'string', 'base_repo_license_name': 'string',
                'base_repo_license_spdx_id': 'string', 'base_repo_license_url': 'string',
                'base_repo_license_node_id': 'string', 'base_repo_allow_forking': 'bool',
                'base_repo_is_template': 'bool', 'base_repo_topics': 'string', 'base_repo_visibility': 'string',
                'base_repo_forks': 'int64', 'base_repo_open_issues': 'int64', 'base_repo_watchers': 'int64',
                'base_repo_default_branch': 'string', '_links_self_href': 'string', '_links_html_href': 'string',
                '_links_issue_href': 'string', '_links_comments_href': 'string',
                '_links_review_comments_href': 'string', '_links_review_comment_href': 'string',
                '_links_commits_href': 'string', '_links_statuses_href': 'string', 'head_repo': 'float64'}
