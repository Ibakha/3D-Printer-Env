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

    def test_getChamberNameNotLoaded(self):
        """
        The getChamberName function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getChamberName(0)
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getChamberNameOutOfRange(self):
        """
        The getChamberName function must raise an IndexError
        if the chamber index is out of range.
        """
        with self.assertRaises(IndexError) as context:
            config.load()
            config.getChamberName(len(self.configDict['chambers']) + 1)
            self.assertTrue(isinstance(context.exception, IndexError))

    def test_getChamberNameReturn(self):
        """
        The getChamberName function must return the chamber name.
        """
        config.load()
        testResult = config.getChamberName(0)
        self.assertEqual(testResult, self.configDict['chambers'][0]['name'])

    def test_getChamberTempSensorsNotLoaded(self):
        """
        The getChamberTempSensors function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getChamberTempSensors(0)
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getChamberTempSensorsOutOfRange(self):
        """
        The getChamberTempSensors function must raise an IndexError
        if the chamber index is out of range.
        """
        with self.assertRaises(IndexError) as context:
            config.load()
            config.getChamberTempSensors(len(self.configDict['chambers']) + 1)
            self.assertTrue(isinstance(context.exception, IndexError))

    def test_getChamberTempSensorsReturn(self):
        """
        The getChamberTempSensors function must return
        the temperature sensors ID.
        """
        config.load()
        testResult = config.getChamberTempSensors(0)
        self.assertEqual(testResult,
                         self.configDict['chambers'][0]['tempSensors'])

    def test_getChamberLedIoNotLoaded(self):
        """
        The getChamberLedIo function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getChamberLedIO(0)
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getChamberLedIoOutOfRange(self):
        """
        The getChamberLedIo function must raise an IndexError
        if the chamber index is out of range.
        """
        with self.assertRaises(IndexError) as context:
            config.load()
            config.getChamberLedIO(len(self.configDict['chambers']) + 1)
            self.assertTrue(isinstance(context.exception, IndexError))

    def test_getChamberLedIoReturn(self):
        """
        The getChamberLedIo function must return
        the LED IO.
        """
        config.load()
        testResult = config.getChamberLedIO(0)
        self.assertEqual(testResult,
                         self.configDict['chambers'][0]['ledIO'])

    def test_getChamberFanIONotLoaded(self):
        """
        The getChamberFanIO function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getChamberFanIO(0)
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getChamberFanIOOutOfRange(self):
        """
        The getChamberFanIO function must raise an IndexError
        if the chamber index is out of range.
        """
        with self.assertRaises(IndexError) as context:
            config.load()
            config.getChamberFanIO(len(self.configDict['chambers']) + 1)
            self.assertTrue(isinstance(context.exception, IndexError))

    def test_getChamberFanIOReturn(self):
        """
        The getChamberFanIO function must return
        the fan IO.
        """
        config.load()
        testResult = config.getChamberFanIO(0)
        self.assertEqual(testResult,
                         self.configDict['chambers'][0]['fanIO'])

    def test_getChamberHeaterIONotLoaded(self):
        """
        The getChamberHeaterIO function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getChamberHeaterIO(0)
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getChamberHeaterIOOutOfRange(self):
        """
        The getChamberHeaterIO function must raise an IndexError
        if the chamber index is out of range.
        """
        with self.assertRaises(IndexError) as context:
            config.load()
            config.getChamberHeaterIO(len(self.configDict['chambers']) + 1)
            self.assertTrue(isinstance(context.exception, IndexError))

    def test_getChamberHeaterIOReturn(self):
        """
        The getChamberHeaterIO function must return
        the heater IO.
        """
        config.load()
        testResult = config.getChamberHeaterIO(0)
        self.assertEqual(testResult,
                         self.configDict['chambers'][0]['heaterIO'])

    def test_getChamberSamplingRateNotLoaded(self):
        """
        The getChamberSamplingRate function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getChamberSamplingRate(0)
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getChamberSamplingRateOutOfRange(self):
        """
        The getChamberSamplingRate function must raise an IndexError
        if the chamber index is out of range.
        """
        with self.assertRaises(IndexError) as context:
            config.load()
            config.getChamberSamplingRate(len(self.configDict['chambers']) + 1)
            self.assertTrue(isinstance(context.exception, IndexError))

    def test_getChamberSamplingRateReturn(self):
        """
        The getChamberSamplingRate function must return
        the sampling rate.
        """
        config.load()
        testResult = config.getChamberSamplingRate(0)
        self.assertEqual(testResult,
                         self.configDict['chambers'][0]['samplingRate'])

    def test_getChamberPidKpNotLoaded(self):
        """
        The getChamberPidKp function must raise a ConfigNotLoaded error
        if the configuration was not loaded before the call.
        """
        with self.assertRaises(config.ConfigNotLoaded) as context:
            config.getChamberPidKp(0)
            self.assertTrue(isinstance(context.exception,
                                       config.ConfigNotLoaded))

    def test_getChamberPidKpOutOfRange(self):
        """
        The getChamberPidKp function must raise an IndexError
        if the chamber index is out of range.
        """
        with self.assertRaises(IndexError) as context:
            config.load()
            config.getChamberPidKp(len(self.configDict['chambers']) + 1)
            self.assertTrue(isinstance(context.exception, IndexError))

    def test_getChamberPidKpReturn(self):
        """
        The getChamberPidKp function must return
        the PID Kp.
        """
        config.load()
        testResult = config.getChamberPidKp(0)
        self.assertEqual(testResult,
                         self.configDict['chambers'][0]['pid']['kp'])
