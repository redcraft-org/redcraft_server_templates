import os

import git
from git.exc import GitCommandError
from github import Github

from utils.env_variables_helper import read_env_variable_boolean


class GitManager():

    def __init__(self):
        self.repo_location = os.path.join(os.path.dirname(__file__), '..')
        self.repo = git.Repo(self.repo_location)
        self.update_branch = os.environ.get('GIT_UPDATE_BRANCH') or 'update'
        self.original_branch = self.repo.active_branch

        self.switch_branch(self.update_branch)

    def switch_to_original_branch(self):
        self.switch_branch(self.original_branch)

    def switch_branch(self, branch):
        if branch == self.repo.active_branch:
            return

        try:
            self.repo.git.checkout('HEAD', '-b', b=branch)
        except GitCommandError:
            self.repo.git.checkout(branch)

    def push_and_create_pull_request(self, outdated_plugins):
        changelog, updated_plugins = get_changelog(outdated_plugins)
        templates_location = os.path.join(
            self.repo_location, 'templates', '*', 'rcst_template_*.json')

        # Add files
        self.repo.index.add([templates_location])

        # Commit changes
        commit_name = 'Updated {}'.format(updated_plugins)
        self.repo.git.commit(
            '-m', commit_name, author=os.environ.get('GIT_AUTHOR'))

        # Push changes
        self.repo.remote().push(refspec='origin/{}'.format(self.update_branch))

        # We will open the pull request
        if read_env_variable_boolean('GITHUB_PULL_REQUEST_ENABLED'):
            github = Github(os.environ.get('GITHUB_TOKEN'))
            github_pr_prefix = '[Automated]'
            github_repo = github.get_repo(os.environ.get('GITHUB_PROJECT'))

            for pull_request in github_repo.get_pulls(state='open', sort='created', base='master'):
                if pull_request.title.startswith(github_pr_prefix):
                    new_body = '{}\n\n--- New changes ---\n\n{}'.format(
                        pull_request.body, changelog)
                    new_title = '{} {}'.format(
                        github_pr_prefix, 'Update multiple plugins')
                    pull_request.update(title=new_title, body=new_body)

            pr_title = '{} {}'.format(github_pr_prefix, commit_name)

            github_repo.create_pull(
                title=pr_title, body=changelog, head=self.update_branch, base="master")


def get_changelog(outdated_plugins):
    # This generates a dumb markdown changelog and a list of updated plugins
    changelog = []
    updated_plugins = []
    for template, plugins in outdated_plugins.items():
        if plugins:
            changelog.append(
                '\nChanges to the template **{}**:\n'.format(template))
            for plugin, versions in plugins.items():
                if plugin not in updated_plugins:
                    updated_plugins.append(plugin)

                current_version = versions['query']
                lastest_version = versions['latest_version']

                line = '- Updated **{}** from `{}` to `{}`'.format(
                    plugin, current_version, lastest_version)

                changelog.append(line)

    changelog_string = '\n'.join(changelog)

    updated_plugins_string = generate_human_plugin_list(updated_plugins)

    return changelog_string, updated_plugins_string


def generate_human_plugin_list(updated_plugins):
    if len(updated_plugins) > 1:
        return '{} and {}'.format(', '.join(updated_plugins[:-1]), updated_plugins[-1])

    return ', '.join(updated_plugins)
