import os
import json

class TemplateManager():

    def __init__(self, template_dir=None):
        self.template_dir = template_dir

        if not self.template_dir:
            self.template_dir = os.path.dirname(__file__)

    def generate_template(self, name):
        template_name, source, target, config_env_matches, server_engine = self.get_template_info(name)

        pass

    def get_template_info(self, name, plugins_only=False):
        template_contents = self.__read_template_file(name)

        template_name = template_contents.get('name')
        template_source = template_contents.get('source')
        template_target = template_contents.get('target')
        template_config_env_matches = template_contents.get('config_env_matches')
        template_server_engine = template_contents.get('config_server_engine')

        template_plugins = template_contents.get('plugins') or {}

        if template_source:
            source_template = self.get_template_info(template_source, plugins_only=True)
            source_plugins = source_template.get('plugins') or {}
            template_plugins.update(source_plugins)

        if plugins_only:
            return {"plugins": template_plugins}

        return template_name, template_source, template_target, template_config_env_matches, template_server_engine

    def __read_template_file(self, template_name):
        with open(self.__get_template_path(template_name)) as json_file:
            return json.load(json_file)

    def __get_template_path(self, template_name):
        return os.path.join(self.template_dir, '{}/rcst_template_{}.json')
