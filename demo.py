from premium.pipeline.pipeline import Pipeline
from premium.exception import PremiumException
from premium.config.configuration import Configuration
from premium.logger import logging
import sys

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #configuration = Configuration().get_data_transformation_config()
        #print(configuration)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()