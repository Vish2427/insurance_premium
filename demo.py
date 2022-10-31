from premium.pipeline.pipeline import Pipeline
from premium.exception import PremiumException
from premium.config.configuration import Configuration
from premium.logger import logging
import sys,os

def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        pipeline.start()
        #configuration = Configuration().get_model_evaluation_config()
        #print(configuration)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()