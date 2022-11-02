from premium.logger import logging
from premium.exception import PremiumException
from premium.entity.config_entity import DataIngestionConfig
from premium.entity.artifact_entity import DataIngestionArtifact
from sklearn.model_selection import StratifiedShuffleSplit
from six.moves import urllib
from premium.data_access.premium_data import PremiumData
from premium.Constant.database import COLLECTION_NAME
from premium.Constant import *
import tarfile
import pandas as pd
from pandas import DataFrame
import numpy as np
import os,sys

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20} Data Ingestion log started.{'='*20} ")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise PremiumException(e, sys) from e

    
    def export_data_into_feature_store(self) -> DataFrame:
        """
        Export mongo db collection record as data frame into raw data dir
        """
        try:
            logging.info("Exporting data from mongodb to raw data dir")
            premium_data = PremiumData()
            dataframe = premium_data.export_collection_as_dataframe(collection_name=COLLECTION_NAME)
            feature_store_file_path = self.data_ingestion_config.raw_data_dir           

            #creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            logging.info(" Exporting data completed")
            return dataframe
        except  Exception as e:
            raise  PremiumException(e,sys)


    def split_data_as_train_test(self) ->DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            #file_name = os.listdir(raw_data_dir)[0]

            premium_file_path = os.path.join(raw_data_dir)

            premium_data_frame = pd.read_csv(premium_file_path)

            premium_data_frame['expense_cat'] = pd.cut(premium_data_frame['expenses'],
                            bins=[1000,10000,20000,30000,40000,np.inf],
                            labels=[1,2,3,4,5]
            )

            logging.info(f"Splitting data into train and test")
            strat_train_set = None
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            for train_index,test_index in split.split(premium_data_frame, premium_data_frame["expense_cat"]):
                strat_train_set = premium_data_frame.loc[train_index].drop(["expense_cat"],axis=1)
                strat_test_set = premium_data_frame.loc[test_index].drop(["expense_cat"],axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            FILE_NAME)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        FILE_NAME)
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path,index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path,index=False)

            data_ingestion_artifact= DataIngestionArtifact(
                train_file_path=train_file_path,
                test_file_path=test_file_path,
                is_ingested=True,
                message=f"Data ingestion completed successfully."
            )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact
        except Exception as e:
            raise PremiumException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            return self.split_data_as_train_test()
        except Exception as e:
            raise PremiumException(e, sys) from e

    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")