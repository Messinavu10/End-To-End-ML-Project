from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        # Initialize the configuration
        data_ingestion_config = config.get_data_ingestion_config()

        # Create DataIngestion instance
        data_ingestion = DataIngestion(data_ingestion_config)

        # Initiate data ingestion
        local_data_file = data_ingestion.initiate_data_ingestion()
        #print(f"Data downloaded to: {local_data_file}")

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

