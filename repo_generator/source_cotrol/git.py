from git import Repo
import os
import shutil


class GitClient:
    def __init__(self, repository_path: str = os.getcwd()) -> None:
        self.path = repository_path

    def clone_and_reset_git_repo(self, repository_url: str):
        self.clone_repo(repository_url)
        self.remove_git_history()
        self.init_git()
        self.commmit_all("Initial commit")

    def init_git(self):
        self.repo = Repo.init(self.path)
        return self.repo

    def clone_repo(self, repository_url: str):
        Repo.clone_from(repository_url, self.path)

    def remove_git_history(self):
        git_dir = os.path.join(self.path, ".git")
        shutil.rmtree(git_dir)

    def commmit_all(self, message: str):
        self.repo.index.add("*")
        self.repo.index.commit(message)

    def set_remote(self, repository_url: str):
        self.repo.create_remote("origin", repository_url)

    def push(self):
        self.repo.remotes.origin.push("master", force=True)
