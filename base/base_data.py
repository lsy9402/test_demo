import yaml


def get_data_yml(file_name = 'data'):
    with open('/Users/mac/Desktop/project/data/' + file_name + '.yml', 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)