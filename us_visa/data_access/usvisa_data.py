import numpy as np
import pandas as pd
from typing import Optional
from us_visa.configuration.mongodb_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME


class UsVisaData:
    """
    This class helpto get Entire MongoDb data into Pandas DataFrame
    """
    def __init__(self) -> None:
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise e
        
    def export_collection_as_dataframe(self, collection_name: str, database_name:Optional[str]=None) -> pd.DataFrame:
        try:
            """
            export entire collection as dataframe
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find({}, {'_id':0})))
            df = df.drop(columns=["case_id"], axis=1)
            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            raise e
        
