import os
from contextlib import contextmanager
from sys import stdout

from loguru import logger
from pyconfigparser import ConfigError, ConfigFileNotFoundError, configparser

from config_schema import CONFIG_SCHEMA


class Main:
    """
    This class handles config parsing
    """

    def __init__(self):
        logger_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
            "{extra[instance]} | "
            "{extra[item]} | "
            "<level>{message}</level>"
        )

        logger.configure(extra={"instance": "", "item": ""})  # Default values
        logger.remove()
        logger.add(stdout, format=logger_format)

    def start(self) -> None:
        try:
            # configparser uses cwd, for file opens.
            # Change to root directory, to look for config in /config/config.yml
            with set_directory("/"):
                config = configparser.get_config(CONFIG_SCHEMA)
        except ConfigFileNotFoundError as exc:
            logger.error(
                "Unable to locate config file, please check volume mount paths, config must be mounted at /config/config.yaml"
            )
            logger.error(exc)
            exit(1)
        except ConfigError as exc:
            logger.error(
                "Unable to parse config file, Please see example config for comparison -- https://github.com/hollanbm/movarr/blob/main/docker/config.yml.example"
            )
            logger.error(exc)
            exit(1)

        for friend in config.friends:
            return


@contextmanager
def set_directory(path):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


if __name__ == "__main__":  # pragma nocover
    Main().start()  # pragma: no cover
