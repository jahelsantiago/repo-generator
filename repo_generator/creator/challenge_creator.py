from repo_generator.config_loader import config
from repo_generator.source_cotrol import GitClient, GithubClient
from repo_generator.io import temporary_directory
import os
from tests.utils import remove_repo_if_exist

CHALLENGE_REPOSITORY_URL = config["challenge"]["repository_url"]
CHALLENGE_NAME = config["challenge"]["name"]
REVIEWERS = config["challenge"]["reviewers"]


@temporary_directory
def create_challenge(participant_github_username: str):
    github_client = GithubClient()

    # check if the user exists
    if not github_client.user_exists(participant_github_username):
        print("User does not exist, please check the username")
        return

    git_client = GitClient(os.getcwd())
    print("successfully created git client")

    # clone the repo and remove git history and tracking
    git_client.clone_and_reset_git_repo(CHALLENGE_REPOSITORY_URL)
    print("successfully cloned and reset git repo")

    # create remote repo
    repo_name = f"{CHALLENGE_NAME}-{participant_github_username}"
    remove_repo_if_exist(repo_name)
    candidate_challenge_repo = github_client.create_github_repo(
        repo_name=repo_name,
    )
    print("successfully created remote repo")

    # add remote
    git_client.set_remote(candidate_challenge_repo.clone_url)
    print("successfully set remote", candidate_challenge_repo.clone_url)

    # push
    git_client.push()
    print("successfully pushed")

    # add participant as collaborator
    github_client.add_collaborator_to_repo(
        candidate_challenge_repo,
        participant_github_username
        )
    print("successfully added participant as collaborator")

    # add reviewer as collaborator
    for reviewer in REVIEWERS:
        github_client.add_collaborator_to_repo(
            candidate_challenge_repo,
            reviewer
        )
    print("successfully added reviewers as collaborators")
