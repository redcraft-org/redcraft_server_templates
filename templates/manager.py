import os
import re
import json
import tarfile
from repository.manager import RepositoryManager
import tempfile
from distutils.dir_util import copy_tree
from tqdm import tqdm

class TemplateManager():

    def __init__(self, template_dir=None):
        self.template_dir = template_dir
        self.repository_manager = RepositoryManager()

        if not self.template_dir:
            self.template_dir = os.path.dirname(__file__)

        self.available_plugins = self.__get_available_plugins()

    def list_templates(self, include_no_target=False):
        templates = []

        for directory in os.listdir(self.template_dir):
            try:
                template_info = self.get_template_info(directory)
                if include_no_target or template_info.get('target'):
                    templates.append(directory)
            except Exception:
                continue

        return templates

    def generate_templates(self):
        for template_name in tqdm(self.list_templates(), desc='Generating templates'):
            self.generate_template(template_name)

    def generate_template(self, name, temporary_directory=None):
        template = self.get_template_info(name)

        temp_directory = temporary_directory or tempfile.TemporaryDirectory()

        source = template.get('source') or None
        if source:
            self.generate_template(source, temporary_directory=temp_directory)

        self.copy_template_config(name, temp_directory.name)

        self.download_plugins(template.get('plugins') or {}, temp_directory.name)

        self.download_server_engine(template.get('server_engine'), temp_directory.name)

        # TODO replace env

        target = template.get('target')

        if target:
            tar_file_path = os.path.join(temp_directory.name, target)

            with tarfile.open(tar_file_path, 'w') as tar:
                tar.add(temp_directory.name, arcname='.')

            self.repository_manager.save(tar_file_path, target)

    def download_server_engine(self, server_engine, output_directory):
        if server_engine:
            filename = '{name}-{version}.jar'.format(**server_engine)
            output_path = os.path.join(output_directory, server_engine.get('target') or filename)
            self.repository_manager.copy(filename, output_path)

    def download_plugins(self, plugins, directory):
        for plugin_name, plugin_version in tqdm(plugins.items(), desc='Downloading plugins', leave=False):
            matched_version = self.get_latest_matching_plugin_version(plugin_name, version_match=plugin_version)
            input_file = self.__get_plugin_filename(plugin_name, matched_version)
            output_file = '{}.jar'.format(plugin_name)
            plugin_directory = os.path.join(directory, 'plugins')

            if not os.path.exists(plugin_directory):
                os.mkdir(plugin_directory)

            self.repository_manager.copy(input_file, os.path.join(plugin_directory, output_file))

    def check_updates(self):
        outdated_plugins = {}
        for template_name in self.list_templates(include_no_target=True):
            template = self.get_template_info(template_name)

            outdated_plugins[template_name] = self.find_outdated_plugins(template.get('plugins') or {})

        return outdated_plugins

    def find_outdated_plugins(self, plugins):
        outdated = {}
        for plugin_name, plugin_version in plugins.items():
            matched_version = self.get_latest_matching_plugin_version(plugin_name, version_match=plugin_version)
            latest_version = self.get_latest_matching_plugin_version(plugin_name)

            if matched_version != latest_version:
                outdated[plugin_name] = {
                    'query': plugin_version,
                    'matched_version': matched_version,
                    'latest_version': latest_version
                }

        return outdated

    def get_latest_matching_plugin_version(self, plugin, version_match='*'):
        available_versions = self.available_plugins.get(plugin)

        if not available_versions:
            raise ValueError('No matching plugin for {}'.format(plugin))

        most_recent_version = None
        most_recent_version_date = None

        for version, version_date in available_versions.items():
            if self.__get_filter_regex(version_match).match(version):
                if not most_recent_version or most_recent_version_date < version_date:
                    most_recent_version = version
                    most_recent_version_date = version_date

        if not most_recent_version:
            raise ValueError('No matching version for {} {}'.format(plugin, version_match))

        return most_recent_version

    def get_template_info(self, template_name):
        with open(self.__get_template_path(template_name)) as json_file:
            return json.load(json_file)

    def copy_template_config(self, template_name, temporary_directory):
        template_config_directory = os.path.join(self.template_dir, template_name, 'config')
        if os.path.exists(template_config_directory):
            copy_tree(template_config_directory, temporary_directory)

    def __get_plugin_filename(self, plugin, version):
        return '{}-{}.jar'.format(plugin, version)

    def __get_available_plugins(self):
        available_plugins = self.repository_manager.list()

        plugins = {}

        for available_plugin, added_date in available_plugins.items():
            plugin_parts = available_plugin.split('-')
            plugin_name = plugin_parts[0]
            plugin_version = '-'.join(plugin_parts[1:]).split('.jar')[0]

            if plugin_name not in plugins:
                plugins[plugin_name] = {}

            plugins[plugin_name][plugin_version] = added_date

        return plugins

    def __get_template_path(self, template_name):
        return os.path.join(self.template_dir, template_name, 'rcst_template_{}.json'.format(template_name))

    def __get_filter_regex(self, filter):
        return re.compile(filter.replace('*', '.+'))
