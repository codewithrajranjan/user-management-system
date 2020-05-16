from unittest import TestCase
from src.config.config import ConfigManager
import os


class TestConfigManager(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_get_config_should_get_config_from_environment(self):
        os.environ["DATABASE_HOST"] = "some-host"
        actual_response = ConfigManager.get_config("DATABASE_HOST")
        self.assertEqual("some-host", actual_response)

    def test_get_config_should_get_config_from_resource_file_when_env_is_not_set(self):

        actual_response = ConfigManager.get_config("DATABASE_HOST")
        self.assertEqual(ConfigManager.get_config("DATABASE_HOST"), actual_response)

    def test_get_config_should_raise_exception_when_config_not_found(self):
        self.assertRaises(KeyError, ConfigManager.get_config, "UNKNOWN_CONFIG")
