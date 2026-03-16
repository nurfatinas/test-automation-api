import yaml

class ReadConfig:

    @staticmethod
    def load_config():
        with open("config/config.yaml") as file:
            return yaml.safe_load(file)