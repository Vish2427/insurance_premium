from premium.logger import logging
from premium.exception import PremiumException
from premium.entity.config_entity import *
from premium.entity.artifact_entity import *
from premium.component.data_ingestion import DataIngestion
from premium.component.data_validation import DataValidation
from premium.component.data_transformation import DataTransformation
from premium.component.model_trainer import ModelTrainer
from premium.component.model_evaluation import ModelEvaluation
from premium.component.model_pusher import ModelPusher
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

    def start_data_validation(self,data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation =  DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact= data_ingestion_artifact)
            return data_validation.inititate_data_validation()
        except Exception as e:
            raise PremiumException(e, sys) from e

    def start_data_transformation(self, data_ingestion_artifact:DataIngestionArtifact,
            data_validation_artifact : DataValidationArtifact,
            ):
        try:
            data_transformation = DataTransformation(data_transformation_config = self.config.get_data_transformation_config(),
             data_ingestion_artifact=data_ingestion_artifact, 
             data_validation_artifact=data_validation_artifact
             )
            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise PremiumException(e, sys) from e
    
    def start_model_training(self, data_transformation_artifac: DataTransformationArtifact):
        try:
            model_training = ModelTrainer(model_trainer_config=self.config.get_model_training_config(), 
                data_transformation_artifact=data_transformation_artifac
            )
            return model_training.initiate_model_trainer()
        except Exception as e:
            raise PremiumException(e, sys) from e

    def start_model_evaluation(self,data_ingestion_artifact: DataIngestionArtifact,
        data_validation_artifact: DataValidationArtifact,
        model_trainer_artifact : ModelTrainerArtifact):
        try:
            model_evaluation = ModelEvaluation(model_evaluation_config=self.config.get_model_evaluation_config(),
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact,
                model_trainer_artifact=model_trainer_artifact
            )
            return model_evaluation.initiate_model_evaluation()
        except Exception as e:
            raise PremiumException(e, sys) from e

    def start_model_pusher(self,model_evaluation_artifact: ModelEvaluationArtifact):
        try:
            model_pusher = ModelPusher(model_pusher_config=self.config.get_model_pusher_config(),
             model_evaluation_artifact=model_evaluation_artifact)
            return model_pusher.initiate_model_pusher()
        except Exception as e:
            raise PremiumException(e, sys) from e


    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifac= self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact,
                             data_validation_artifact=data_validation_artifact
                             )
            model_trainer_artifact = self.start_model_training(data_transformation_artifac=data_transformation_artifac)    
            model_evaluation_artifact = self.start_model_evaluation(data_ingestion_artifact=data_ingestion_artifact, 
            data_validation_artifact=data_validation_artifact, model_trainer_artifact=model_trainer_artifact)   
            model_pusher_artifact =  self.start_model_pusher(model_evaluation_artifact=model_evaluation_artifact)    
        except Exception as e:
            raise PremiumException(e, sys) from e