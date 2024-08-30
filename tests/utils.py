from repo_generator.source_cotrol import GithubClient


def remove_repo_if_exist(repo_name: str):
    github_client = GithubClient()
    repo = github_client.get_repo(repo_name)
    if repo is not None:
        repo.delete()
