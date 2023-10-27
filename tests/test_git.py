import os
from repo_generator.io import temporary_directory
from repo_generator.github.git import GitClient

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

def test_init_git():
    git_client = GitClient(os.getcwd())
    git_client.init_git()
    assert ".git" in os.listdir(os.getcwd())
    


    