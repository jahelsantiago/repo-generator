from repo_generator.config_loader import config
from repo_generator.source_cotrol import GitClient, GithubClient
from repo_generator.io import temporary_directory
import os

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

    # create remote repo
    candidate_challenge_repo = github_client.create_github_repo(
        f"{CHALLENGE_NAME}-{participant_github_username}"
        )

    # clone the repo and remove git history and tracking
    git_client.clone_and_reset_git_repo(CHALLENGE_REPOSITORY_URL)

    # add remote
    git_client.set_remote(candidate_challenge_repo.clone_url)

    # push
    git_client.push()

    # add participant as collaborator
    github_client.add_collaborator_to_repo(
        candidate_challenge_repo,
        participant_github_username
        )

    # add reviewer as collaborator
    for reviewer in REVIEWERS:
        github_client.add_collaborator_to_repo(
            candidate_challenge_repo,
            reviewer
            )
