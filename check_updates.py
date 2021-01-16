from dotenv import load_dotenv

from templates.manager import TemplateManager


if __name__ == '__main__':
    load_dotenv()

    template_manager = TemplateManager()

    outdated_plugins = template_manager.check_updates()

    print(outdated_plugins)
