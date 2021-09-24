import json
from unittest import TestCase
from unittest.mock import mock_open, patch

import os
import sys

sys.path.append(os.path.abspath('./src'))

from pkgs.config import config      # noqa: E402


class TestConfig(TestCase):
    """
    Config module test cases.
    """
    def setUp(self) -> None:
        with open(config.CONFIG_FILE) as configFile:
            self.configStr = configFile.read()
            self.configDict = json.loads(self.configStr)
        config._config = None

    def test_loadError(self):
        """
        The load function must raise an error if the file access failed.
        """
        with patch('builtins.open', mock_open(read_data=self.configStr)) \
                as mockedConfigFile, \
                self.assertRaises(OSError) as context:
            mockedConfigFile.side_effect = OSError
            config.load()
            self.assertTrue(isinstance(context.exception, OSError))

    def test_loadJsonLoads(self):
        """
        The load function must read the JSON configuration.
        """
        with patch('builtins.open', mock_open(read_data=self.configStr)), \
                patch('pkgs.config.config.json.loads') as mockedJsonLoads:
            config.load()
            mockedJsonLoads.assert_called_once_with(self.configStr)

    def test_getApiHostNotLoaded(self):
        """
        The getApiHost function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getApiHost()
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getApiHostReturn(self):
        """
        The getApiHost function must return the API host.
        """
        config.load()
        testResult = config.getApiHost()
        self.assertEqual(testResult, self.configDict['api']['host'])

    def test_getApiPortNotLoaded(self):
        """
        The getApiPort function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getApiPort()
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getApiPortReturn(self):
        """
        The getApiPort function must return the API port.
        """
        config.load()
        testResult = config.getApiPort()
        self.assertEqual(testResult, self.configDict['api']['port'])

    def test_getChambersCountNotLoaded(self):
        """
        The getChambersCount function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getChambersCount()
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getChambersCountReturn(self):
        """
        The getChambersCount function must return the count of chambers.
        """
        config.load()
        testResult = config.getChambersCount()
        self.assertEqual(testResult, len(self.configDict['chambers']))
