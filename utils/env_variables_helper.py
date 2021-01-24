import os

def read_env_variable_boolean(env_variable):
    true_values = ['true', '1', 'on', 'enabled']
    return os.environ.get(env_variable, '').lower() in true_values
