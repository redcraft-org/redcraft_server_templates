# RedCraft Server Templates (rcst)

This repo contains all the configuration of our Minecraft instances.

All the configuration can be found under `/templates`, including the list of plugins in the `rcst_template_*.json` file. You can use the `templates/common/rcst_template_common.json` file as a template.

`target` must be defined in order to have an output template, but it can be set to `null` and be used as a `source` of another template.

## Setup the project

If you're running Linux, macOS, BSD or WSL, it should be as easy as running `./setup.sh`. Make sure you have Python 3 and virtualenv installed (`pip3 install virtualenv`).

Otherwise, create and activate a virtualenv (optional, usually by running `python3 -m venv env` and `source env/bin/activate`), and install requirements using `pip install -r requirements.txt`.

## Config

To set your credentials and preferences, copy `.env.example` to `.env` and edit the values as you want.

## How it works

You just have to run `python generate_templates.py` to generate templates, or `python check_updates.py` to update your templates with an up-to-date version of available plugins.
