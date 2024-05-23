import os
import pandas as pd
from sklearn.model_selection import train_test_split

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.data_access.usvisa_data import UsVisaData
from us_visa.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig=DataIngestionConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except  Exception as e:
            raise e
        
    def export_data_into_feature_store(self) -> pd.DataFrame:
        """
        This method Export Data from MongoDb and save into Csv file 
        """
        try:
            logging.info("Starting exporting data from MongoDb")
            usvisa_data = UsVisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=
                                                                    self.data_ingestion_config.collection_name)
            print(dataframe.head())
            logging.info(f"dataframe shape is {dataframe.shape}")
            # saving data to feature store
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"saving exported data into feature store path : {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False)
            return dataframe
            
        except Exception as e:
            raise e
    
    def split_data_as_train_test(self, dataframe: pd.DataFrame) -> None:
        """
        THis method splits data into train and test and save it  ingested_dir
        """
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info(f"Performed train_test_split succefully")

            # saving train adn test data file
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            print(f"****************: {dir_path}  **********")

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False)
            logging.info(f"train and test data saved at {dir_path}")
        except Exception as e:
            raise e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        this method initiate data ingestion component one by one
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try:
            dataframe = self.export_data_into_feature_store()

            self.split_data_as_train_test(dataframe=dataframe)

            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                            test_file_path=self.data_ingestion_config.testing_file_path)
            
            return data_ingestion_artifact

        except Exception as e:
            raise e