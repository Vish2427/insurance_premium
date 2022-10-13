from premium.logger import logging
from premium.exception import PremiumException
from premium.entity.config_entity import DataIngestionConfig
from premium.entity.artifact_entity import DataIngestionArtifact
from premium.component.data_ingestion import DataIngestion
from premium.config.configuration import Configuration
import os,sys

class Pipeline:
    
    def __init__(self, config : Configuration=Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise PremiumException(e, sys) from e
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise PremiumException(e, sys) from e

    def run_pipeline(self):
        try:
            data_ingestion = self.start_data_ingestion()
        except Exception as e:
            raise PremiumException(e, sys) from e