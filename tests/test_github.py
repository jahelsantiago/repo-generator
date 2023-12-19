from repo_generator.source_cotrol import GithubClient
from repo_generator.config_loader import config
from .utils import remove_repo_if_exist
import pytest


USERNAME = config["github"]["username"]
TEST_REPO_NAME = "test_repo"
TEST_REPO_FULL_NAME = f"{USERNAME}/{TEST_REPO_NAME}"


def test_user_exist():
    github_client = GithubClient()
    assert github_client.user_exists(USERNAME) is True


def test_user_does_not_exist():
    github_client = GithubClient()
    FAKE_USERNAME = "jahelsantiago123"
    assert github_client.user_exists(FAKE_USERNAME) is False


def test_repo_exists():
    github_client = GithubClient()
    assert github_client.repo_exists("jahelsantiago/aider") is True


def test_repo_does_not_exist():
    github_client = GithubClient()
    assert github_client.repo_exists("jahelsantiago/aider123") is False


def test_authenticated_user():
    github_client = GithubClient()
    assert github_client.user.login == USERNAME


def test_create_remote_github_repo():
    github_client = GithubClient()

    remove_repo_if_exist(TEST_REPO_FULL_NAME)
    repo = github_client.create_github_repo(TEST_REPO_NAME)

    assert repo.name == TEST_REPO_NAME
    assert repo.private is True
    repo.delete()


def _test_add_colaborators_to_rep():
    github_client = GithubClient()

    remove_repo_if_exist(TEST_REPO_FULL_NAME)

    repo = github_client.create_github_repo(TEST_REPO_NAME)

    colaborator_username = "jahelleon"
    github_client.add_collaborator_to_repo(repo, colaborator_username)

    colaborators = repo.get_collaborators()

    assert colaborators.totalCount == 1
    assert colaborator_username in [colaborator.login for colaborator in colaborators]

    repo.delete()


def test_add_nonexistent_collaborator_to_repo():
    github_client = GithubClient()

    remove_repo_if_exist(TEST_REPO_FULL_NAME)

    repo = github_client.create_github_repo(TEST_REPO_NAME)

    colaborator_username = "nonexistentuser"
    with pytest.raises(Exception):
        github_client.add_collaborator_to_repo(repo, colaborator_username)

    repo.delete()
