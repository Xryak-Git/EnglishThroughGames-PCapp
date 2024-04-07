import configparser
import logging
import os

from pathlib import Path

LOG = logging.getLogger(__name__)
LOG_FILE = "log.txt"

DEFAULT_USER_DIR = Path(__file__).resolve().parent
DEFAULT_PORCESSES = 4

SETTINGS_FILE = "../settings.ini"
SETTINGS_FILE_TEMPLATE = """
[user_data]
directory={}

[multiprocessing]
processes={}

"""


class Settings:
    user_dir: Path
    processes: int

    _filename: Path

    def __init__(self, filename: Path):

        self.user_dir = DEFAULT_USER_DIR / "userdata"
        self.processes = DEFAULT_PORCESSES

        self._filename = filename

        self._search_existing_configuration()

    def parse_from_file(self) -> int:
        try:
            LOG.info(
                f"Found existing configuration file at: " f"{self._filename.resolve()}"
            )

            parsed_config = configparser.ConfigParser()
            parsed_config.read(self._filename)

            self._parse_user_dir(parsed_config)
            self._parse_processes(parsed_config)

            LOG.info(f"Done parsing existing configuration.")
            return 0

        except Exception as e:
            LOG.error(
                f"Unhandled error while parsing configuration file "
                f"at {self._filename}: {e}. Default configuration will be "
                "used."
            )
            return 1

    def write_to_file(self) -> int:
        try:
            LOG.info(f"Writing configuration to: {self._filename.resolve()}")
            with open(self._filename, "w") as f:
                f.write(
                    SETTINGS_FILE_TEMPLATE.format(
                        self.user_dir.resolve(),
                        int(self.processes),

                    )
                )
            LOG.info("Successfully wrote configuration file.")
            return 0
        except Exception:
            return 1

    def _search_existing_configuration(self):
        if not self._filename.is_file():
            LOG.info(
                f"No existing configuration file found, "
                f"writing default configuration to: {self._filename.resolve()}"
            )
            self.write_to_file()
        else:
            self.parse_from_file()

    def _parse_user_dir(self, parsed_config):
        if (
                "user_data" in parsed_config
                and "directory" in parsed_config["user_data"]
        ):
            self.user_dir = Path(parsed_config["user_data"]["directory"])

    def _parse_processes(self, parsed_config):
        if (
                "multiprocessing" in parsed_config
                and "processes" in parsed_config["multiprocessing"]
        ):
            processes = parsed_config["multiprocessing"]["processes"]
            try:

                assert 1 <= int(processes) <= 8
                self.processes = int(processes)

            except AssertionError:
                LOG.error(
                    f"Invalid value {processes} specified for "
                    f"concurrency limit, must be an integer <= 1 and >= 8. Using "
                    f"default value of {DEFAULT_PORCESSES} "
                    f"instead."
                )

