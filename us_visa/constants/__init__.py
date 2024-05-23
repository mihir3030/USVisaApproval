import os
from datetime import date

DATABASE_NAME = "DB_NAME"
COLLECTION_NAME = "COLLECTION_NAME"

MONGO_DB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME = "us_visa"
ARTIFACT_DIR = "artifacts"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data Ingestion Releated Constant
"""
DATA_INGESTION_COLLECTION_NAME: str = "COLLECTION_NAME"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2
