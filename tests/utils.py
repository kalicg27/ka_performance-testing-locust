import os
import yaml

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "config",
    "settings.yaml"
)


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


config = load_config()
TARGET_HOST = config["target_host"]
LOAD_PROFILE = config["load_profile"]
ENDPOINTS = config["endpoints"]
