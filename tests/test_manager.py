import os
import json
import tempfile
import unittest

from templates.manager import TemplateManager, get_template_resources


class FakeTemplateManager(TemplateManager):

    def __init__(self, templates, available_plugins):
        self.templates = templates
        self.available_plugins = available_plugins
        self.saved_templates = {}

    def list_templates(self, include_no_target=False):
        return list(self.templates)

    def get_template_info(self, template_name):
        return self.templates[template_name]

    def save_template_info(self, template_name, new_template_info):
        self.saved_templates[template_name] = new_template_info


class TemplateResourcesTests(unittest.TestCase):

    def test_legacy_plugins_key(self):
        template = {'plugins': {'SomePlugin': '1.0.*'}}
        self.assertEqual({'plugins': {'SomePlugin': '1.0.*'}},
                         get_template_resources(template))

    def test_resources_key(self):
        template = {
            'resources': {
                'mods': {'SomeMod': '1.0.*'},
                'plugins': {'SomePlugin': '2.0.*'}
            }
        }
        self.assertEqual(template['resources'],
                         get_template_resources(template))

    def test_resources_key_takes_precedence(self):
        template = {
            'plugins': {'LegacyPlugin': '1.0.*'},
            'resources': {'mods': {'SomeMod': '1.0.*'}}
        }
        self.assertEqual(template['resources'],
                         get_template_resources(template))

    def test_empty_template(self):
        self.assertEqual({'plugins': {}}, get_template_resources({}))

    def test_returns_references_for_updates(self):
        template = {'resources': {'mods': {'SomeMod': '1.0.*'}}}
        resources = get_template_resources(template)
        resources['mods']['SomeMod'] = '1.1.*'
        self.assertEqual('1.1.*', template['resources']['mods']['SomeMod'])


class UpdateFlowTests(unittest.TestCase):

    def make_manager(self):
        templates = {
            'fabric': {
                'resources': {
                    'mods': {'FakeMod': '1.0.*'},
                    'plugins': {'FakePlugin': '2.1.*'}
                }
            },
            'legacy': {
                'plugins': {'LegacyPlugin': '3.0.*'}
            }
        }
        available_plugins = {
            'FakeMod': {'1.0.2': 1, '1.1.0': 2},
            'FakePlugin': {'2.1.4': 1},
            'LegacyPlugin': {'3.0.1': 1, '3.1.0': 2}
        }
        return FakeTemplateManager(templates, available_plugins)

    def test_check_updates_covers_mods(self):
        manager = self.make_manager()

        outdated = manager.check_updates()

        self.assertIn('fabric', outdated)
        self.assertIn('FakeMod', outdated['fabric'])
        self.assertEqual(
            '1.1.0', outdated['fabric']['FakeMod']['latest_version'])
        self.assertNotIn('FakePlugin', outdated['fabric'])

    def test_check_updates_covers_legacy_plugins(self):
        manager = self.make_manager()

        outdated = manager.check_updates()

        self.assertIn('legacy', outdated)
        self.assertEqual(
            '3.1.0', outdated['legacy']['LegacyPlugin']['latest_version'])

    def test_update_plugins_updates_mods(self):
        manager = self.make_manager()

        manager.update_plugins()

        self.assertEqual(
            '1.1.*', manager.templates['fabric']['resources']['mods']['FakeMod'])
        self.assertEqual(
            '2.1.*', manager.templates['fabric']['resources']['plugins']['FakePlugin'])
        self.assertIn('fabric', manager.saved_templates)

    def test_update_plugins_updates_legacy_plugins(self):
        manager = self.make_manager()

        manager.update_plugins()

        self.assertEqual(
            '3.1.*', manager.templates['legacy']['plugins']['LegacyPlugin'])
        self.assertIn('legacy', manager.saved_templates)


class TemplateInfoRoundTripTests(unittest.TestCase):

    def test_save_template_info_keeps_format(self):
        with tempfile.TemporaryDirectory() as template_dir:
            manager = TemplateManager.__new__(TemplateManager)
            manager.template_dir = template_dir
            os.mkdir(os.path.join(template_dir, 'fake'))

            template = {
                'name': 'fake',
                'resources': {'mods': {'FakeMod': '1.0.*'}}
            }
            manager.save_template_info('fake', template)

            template_path = os.path.join(
                template_dir, 'fake', 'rcst_template_fake.json')
            with open(template_path) as json_file:
                content = json_file.read()

            self.assertEqual(template, json.loads(content))
            self.assertIn('    "name": "fake"', content)
            self.assertLess(content.index('"name"'), content.index('"resources"'))
