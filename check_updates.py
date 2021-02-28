import os
from utils.env_variables_helper import read_env_variable_boolean

from dotenv import load_dotenv

from templates.manager import TemplateManager
from utils.git_manager import GitManager


if __name__ == '__main__':
    load_dotenv()

    git_manager = None

    if read_env_variable_boolean('GIT_ENABLED'):
        git_manager = GitManager()

    template_manager = TemplateManager()

    outdated_plugins = template_manager.update_plugins(print_updates=True)

    print(outdated_plugins)

    if outdated_plugins and git_manager:
        GitManager().push_and_create_pull_request(outdated_plugins)
        git_manager.switch_to_original_branch()
