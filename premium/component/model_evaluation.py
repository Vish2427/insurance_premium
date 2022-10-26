from premium.logger import logging
from premium.exception import PremiumException
from premium.config.configuration import Configuration
from premium.entity.artifact_entity import *
from premium.entity.config_entity import *
import os,sys
from premium.util.util import *

class ModdelEvaluation:

    def __init__(self,model_evaluation_config : ModelEvaluationConfig,
        data_ingestion_artifact : DataIngestionArtifact,
        data_validation_atifact : DataValidationArtifact,
        model_trainer_artifact : ModelTrainerArtifact):
    
        try :
            logging.info(f"{'='*20} Model Evaluation log started.{'='*20} ")
            self.model_evaluation_config = model_evaluation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_atifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception  as e:
            raise PremiumException(e, sys) from e

        def best_model(self):
            try:
                model = None
                model_evaluation_file_path = self.model_evaluation_config.model_evaluation_file_path

                if not os.path.exit(model_evaluation_file_path):
                    write_yaml_file(file_path=model_evaluation_file_path)
                    return model

                model_eval_file_content = read_yaml_file(file_path=model_evaluation_file_path)

                model_eval_file_content = dict() if model_eval_file_content is None else model_eval_file_content

                if BEST_MODEL_KEY not in model_eval_file_content:
                    return model

                model =  load_object(file_path=model_eval_file_content[BEST_MODEL_KEY][MODEL_PATH_KEY])
                
            except Exception as e:
                raise PremiumException(e, sys) from e

        def initiate_model_evaluation(self):
            try:
                trained_model_file_path = self.model_trainer_artifact.trained_model_file_path
                trained_model_object = load_object(file_path=trained_model_file_path)

                train_file_path = self.data_ingestion_artifact.train_file_path
                test_file_path = self.data_ingestion_artifact.test_file_path

                schema_file_path = self.data_validation_artifact.schema_file_path

                train_dataframe = load_data(file_path = train_file_path, schema_file_path = schema_file_path)
                test_dataframe = load_data(file_path = test_file_path, schema_file_path = schema_file_path)

                schema_content = read_yaml_file(file_path=schema_file_path)
                target_column_name = schema_content[TARGET_COLUMN_KEY]

                 # target_column
                logging.info(f"Converting target column into numpy array.")
                train_target_arr = np.array(train_dataframe[target_column_name])
                test_target_arr = np.array(test_dataframe[target_column_name])
                logging.info(f"Conversion completed target column into numpy array.")

                # dropping target column from the dataframe
                logging.info(f"Dropping target column from the dataframe.")
                train_dataframe.drop(target_column_name, axis=1, inplace=True)
                test_dataframe.drop(target_column_name, axis=1, inplace=True)
                logging.info(f"Dropping target column from the dataframe completed.")

                model = self.get_best_model()

            except Exception as e:
                raise PremiumException(e, sys) from e

        def __del__(self):
            logging.info(f"{'>>'*20}Model Evaluation log completed.{'<<'*20} \n\n")