from git import Repo
import os
import shutil

#create a remote repo

#clone a repository given a url

#remove git history from the repository

#initialize a new git source control

#commit everithing in the repository

#push the repository to a remote


class GitClient:
    def __init__(self, repository_path: str) -> None:
        self.path = repository_path

    def clone_repo(self, repository_url: str):
        Repo.clone_from(repository_url, self.path)

    def remove_git_history(self):
        git_dir = os.path.join(self.path, ".git")
        shutil.rmtree(git_dir)

    def init_git(self):
        self.repo = Repo.init(self.path)
        return self.repo
        
    def commmit_all(self, message: str):
        self.repo.git.add(".")
        self.repo.index.commit(message)

