from repo_generator.config_loader import config
from github import Github, Auth
from github.Repository import Repository


class GithubClient:
    def __init__(self) -> None:
        self.client = self.authenticate_with_token()
        self.user = self.client.get_user()

    def authenticate_with_token(self):
        token = config["github"]["access_token"]
        if token is None:
            raise Exception("Github token not found in config file")

        auth = Auth.Token(token)

        return Github(auth=auth)

    def user_exists(self, username: str) -> bool:
        try:
            self.client.get_user(username)
            return True
        except Exception as e:
            return False

    def repo_exists(self, repo_name: str) -> bool:
        try:
            self.client.get_repo(repo_name)
            return True
        except Exception as e:
            return False

    def create_github_repo(self, repo_name: str) -> Repository:
        repo = self.user.create_repo(repo_name, private=True)
        return repo

    def add_collaborator_to_repo(self, repo: Repository, username: str):
        if (not self.user_exists(username)):
            raise Exception(f"User {username} does not exist on Github")
        repo.add_to_collaborators(username, permission="admin")

    def get_repo(self, repo_name: str) -> Repository:
        try:
            return self.client.get_repo(repo_name)
        except Exception as e:
            return None

    def push_local_repo_to_github(self, repo_path: str):
        pass
