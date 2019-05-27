import os, unittest

import textwrap
from six import StringIO

from indicoio.config import Settings
from indicoio import config

class TestConfigureEnv(unittest.TestCase):
    """
    Ensure that environment variables are handled by the `Settings` parser
    """

    def setUp(self):
        os.environ = {}

    def test_set_cloud_from_env_var(self):
        """
        Ensure cloud hostname is read in from environment variables
        """
        cloud = "invalid/cloud"
        os.environ["INDICO_CLOUD"] = cloud
        assert config.SETTINGS.cloud() == cloud

    def test_set_auth_from_env_var(self):
        """
        Ensure cloud authentication credentials are read in from environment variables
        """
        api_key = "text"
        os.environ["INDICO_API_KEY"] = api_key
        assert config.SETTINGS.api_key() == api_key


class TestConfigurationFile(unittest.TestCase):
    """
    Ensure that the `Settings` parser reads in configuration files properly
    """

    def setUp(self):
        self.api_key = "test"
        self.cloud = "localhost"
        config = """
        [auth]
        api_key = %s

        [private_cloud]
        cloud = %s
        """ % (self.api_key, self.cloud)

        config_file = StringIO(textwrap.dedent(config))
        self.settings = Settings(files=[config_file])
        os.environ = {}

    def test_set_cloud_from_config_file(self):
        """
        Ensure cloud hostname is read in from file
        """
        assert self.settings.cloud() == self.cloud

    def test_set_auth_from_config_file(self):
        """
        Ensure cloud authentication credentials are read in from file
        """
        assert self.settings.api_key() == self.api_key


class TestPrecedence(unittest.TestCase):
    """
    Ensure that environment variables take precedence to config files
    """

    def setUp(self):
        self.file_api_key = "file-api-key"
        self.file_cloud = "file-cloud"

        self.env_api_key = "env-api-key"
        self.env_cloud = "env-cloud"
        config = """
        [auth]
        api_key = %s

        [private_cloud]
        cloud = %s
        """ % (self.file_api_key, self.file_cloud)

        config_file = StringIO(textwrap.dedent(config))
        os.environ = {
            'INDICO_CLOUD': self.env_cloud,
            'INDICO_API_KEY': self.env_api_key
        }
        self.settings = Settings(files=[config_file])

    def test_set_cloud_from_config_file(self):
        """
        Ensure cloud hosts set in environment variables are used over those in config files
        """
        assert self.settings.cloud() == self.env_cloud

    def test_set_auth_from_config_file(self):
        """
        Ensure cloud authentication credentials set in environment variables
        are used over those in config files
        """
        assert self.settings.api_key() == self.env_api_key


class TestConfigFilePrecedence(unittest.TestCase):
    """
    Ensure that files passed in to a `Settings` object are assigned proper priority
    """

    def setUp(self):
        self.high_priority_api_key = "high-priority-api-key"
        self.high_priority_cloud = "high-priority-cloud"

        self.low_priority_api_key = "low-priority-api-key"
        self.low_priority_cloud = "low-priority-cloud"

        high_priority_config = """
        [auth]
        api_key = %s

        [private_cloud]
        cloud = %s
        """ % (
            self.high_priority_api_key,
            self.high_priority_cloud
        )

        low_priority_config = """
        [auth]
        username = %s

        [private_cloud]
        cloud = %s
        """ % (
            self.low_priority_api_key,
            self.low_priority_cloud
        )

        high_priority_config_file = StringIO(textwrap.dedent(high_priority_config))
        low_priority_config_file = StringIO(textwrap.dedent(low_priority_config))

        os.environ = {}
        self.settings = Settings(files=[
            low_priority_config_file,
            high_priority_config_file
        ])

    def test_cloud_config_file_priority(self):
        """
        Ensure the cloud subdomain priority is handled properly
        """
        assert self.settings.cloud() == self.high_priority_cloud

    def test_auth_config_file_priority(self):
        """
        Ensure the cloud auth priority is handled properly
        """
        assert self.settings.api_key() == self.high_priority_api_key
