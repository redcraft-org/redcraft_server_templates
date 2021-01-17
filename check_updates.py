from dotenv import load_dotenv

from templates.manager import TemplateManager


if __name__ == '__main__':
    load_dotenv()

    template_manager = TemplateManager()

    template_manager.update_plugins(print_updates=True)
