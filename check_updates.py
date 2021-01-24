import argparse

from dotenv import load_dotenv

from templates.manager import TemplateManager
from utils.git_manager import GitManager


if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser('Check ')

    parser.add_argument("--push-to-git", action="store_true")
    parser.add_argument('-git-branch', help='Git branch, default is "update"', default='update', type=str)

    args = parser.parse_args()

    git_manager = GitManager() if args.push_to_git else None

    if git_manager:
        git_manager.switch_branch(args.git_branch)

    template_manager = TemplateManager()

    outdated_plugins = template_manager.update_plugins(print_updates=True)

    # TODO Remove or true
    if outdated_plugins and git_manager:
        GitManager().push_and_create_pull_request()
        # TODO

    git_manager.switch_to_original_branch()
