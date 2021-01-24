import os

import git
from git.exc import GitCommandError


class GitManager():

    def __init__(self):
        self.repo_location = os.path.join(os.path.dirname(__file__), '..')
        self.repo = git.Repo(self.repo_location)
        self.original_branch = self.repo.active_branch

    def switch_to_original_branch(self):
        self.switch_branch(self.original_branch)

    def switch_branch(self, branch):
        if branch == self.repo.active_branch:
            return

        try:
            self.repo.git.checkout('HEAD', b=branch)
        except GitCommandError:
            self.repo.git.checkout(branch)

    def push_and_create_pull_request(self):
        templates_location = os.path.join(
            self.repo_location, 'templates', '*', 'rcst_template_*.json')
        self.repo.index.add([templates_location])
        return True
