from repo_generator.config_loader import config
from repo_generator.source_cotrol import GitClient, GithubClient
from repo_generator.io import temporary_directory
from .utils import remove_repo_if_exist
from repo_generator.creator import create_challenge


import os

USERNAME = config["github"]["username"]
CHALLENGE_REPOSITORY_URL = config["challenge"]["repository_url"]
CHALLENGE_NAME = config["challenge"]["name"]

participant_github_username = "jahelleon"

@temporary_directory
def _test_integration():
    github_client = GithubClient()

    #check if the user exists
    if not github_client.user_exists(participant_github_username):
        print("User does not exist, please check the username")
        return
    

    git_client = GitClient(os.getcwd())

    #create remote repo
    REPOSITORY_CHALLENGE_NAME = f"{CHALLENGE_NAME}-{participant_github_username}"
    remove_repo_if_exist(f"{USERNAME}/{REPOSITORY_CHALLENGE_NAME}")
    candidate_challenge_repo = github_client.create_github_repo(REPOSITORY_CHALLENGE_NAME)

    #clone the repo
    git_client.clone_repo(CHALLENGE_REPOSITORY_URL)
    git_client.remove_git_history()
    git_client.init_git()
    git_client.commmit_all("Initial commit")

    #add remote
    git_client.set_remote(candidate_challenge_repo.clone_url)

    #push
    git_client.push()

    #add collaborator
    github_client.add_collaborator_to_repo(candidate_challenge_repo, participant_github_username)


def test_challenge_creation():
    participant_github_username = "jahelleon"

    remove_repo_if_exist(f"{USERNAME}/{CHALLENGE_NAME}-{participant_github_username}")

    create_challenge(participant_github_username)

    github_client = GithubClient()

    remote_repo = github_client.get_repo(f"{USERNAME}/{CHALLENGE_NAME}-{participant_github_username}")

    assert remote_repo is not None

    remote_repo.delete()


