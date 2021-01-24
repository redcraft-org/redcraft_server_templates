import os

from git import Repo

class GitManager():

    def __init__(self):
        self.repo_location = os.path.join(os.path.dirname(__file__), '..')
        self.repo = Repo(self.repo_location)

    def use_update_branch(self, branch):
        self.repo.git.checkout('HEAD', b=branch)

    def push_and_create_pull_request(self):

        return True
