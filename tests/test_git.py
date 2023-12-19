import os
from repo_generator.io import temporary_directory
from repo_generator.source_cotrol import GitClient


@temporary_directory
def test_git_clone():
    git_client = GitClient(os.getcwd())
    git_client.clone_repo("https://github.com/jahelsantiago/simple_repo_test.git")
    assert ".git" in os.listdir(os.getcwd())


@temporary_directory
def test_remove_git_history():
    git_client = GitClient(os.getcwd())
    git_client.clone_repo("https://github.com/jahelsantiago/simple_repo_test.git")
    git_client.remove_git_history()

    assert ".git" not in os.listdir(os.getcwd())


@temporary_directory
def test_init_git():
    git_client = GitClient(os.getcwd())
    git_client.init_git()
    assert ".git" in os.listdir(os.getcwd())


@temporary_directory
def test_commit_all():
    git_client = GitClient(os.getcwd())
    git_client.init_git()
    with open("test.txt", "w") as f:
        f.write("test content")

    git_client.commmit_all("test commit")

    last_commit = git_client.repo.head.commit

    commit_message = last_commit.message
    assert commit_message == "test commit"

    modified_files = last_commit.stats.files.keys()
    assert "test.txt" in modified_files
