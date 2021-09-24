import json
import os

CONFIG_FILE = os.path.join('src/pkgs/config', 'config.json')

_config = None


def load() -> None:
    """
    Load the application configuration.
    """
    global _config
    with open(CONFIG_FILE) as configFile:
        _config = json.loads(configFile.read())


def getApiHost() -> str:
    """
    Get the API host.

    Return:
        The API host.
    """
    if _config is None:
        raise ConfigNotLoaded()
    return _config['api']['host']


def getApiPort() -> int:
    """
    Get the API port.

    Return:
        The API port.
    """
    if _config is None:
        raise ConfigNotLoaded()
    return _config['api']['port']


def getChambersCount() -> int:
    """
    Get the count of chambers in the configuration.

    Return:
        The count of chambers.
    """
    if _config is None:
        raise ConfigNotLoaded()
    return len(_config['chambers'])


def getChamberName(idx: int) -> str:
    """
    Get the designed chamber name.

    Params:
        idx:    The designed chamber index.

    Return:
        The designed chamber name.
    """
    if _config is None:
        raise ConfigNotLoaded()
    return _config['chambers'][idx]['name']


def getChamberTempsSensors(idx: int):
    """
    Get the designed chamber temperature sensors ID.

    Params:
        idx:    The designed chamber index.

    Return:
        The temperature sensors ID.
    """
    pass


class ConfigNotLoaded(Exception):
    """
    The ConfigNotLoaded exception.
    """
    def __init__(self):
        """
        Contructor.
        """
        super().__init__('configuration not loaded')
