import os
from us_visa.logger import logging
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.components.data_ingestion import DataIngestion


class TrainingPipeline:
    def __init__(self) -> None:
        self.data_ingestion_config = DataIngestionConfig()

    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(f">>>>>>>>>>>>>>>>> Data Ingestion Stage started")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"data ingesion compleated at {data_ingestion_artifact}")
            logging.info(f">>>>>>>>>>>>>>>>> Data Ingestion Stage compleated successfully\n")
            return data_ingestion_artifact
        except Exception as e:
            raise e
        

    def run_pipeline(self):
        try:
            data_ingestion_artiface = self.start_data_ingestion()
        except Exception as e:
            raise e
        