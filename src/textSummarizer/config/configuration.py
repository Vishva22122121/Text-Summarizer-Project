from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig, DataValidationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=None,
        params_filepath=None):

        try:
            if config_filepath is None:
                config_filepath = CONFIG_FILE_PATH
            self.config = read_yaml(config_filepath)

            if params_filepath is None:
                params_filepath = PARAMS_FILE_PATH
            self.params = read_yaml(params_filepath)

            create_directories([self.config.artifacts_root])

        except Exception as e:
            print(f"An error occurred during initialization: {str(e)}")

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config = self.config.data_ingestion

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir 
            )

            return data_ingestion_config
        except Exception as e:
            print(f"An error occurred in get_data_ingestion_config: {str(e)}")

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config