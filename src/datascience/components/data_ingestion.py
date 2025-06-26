import urllib.request as request
from src.datascience import logger
import os

from src.datascience.entity.config_entity import (DataIngestionconfig)

class DataIngestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config
    
    def download_file(self):
        """Download the CSV file from the source URL"""
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")
    
    def initiate_data_ingestion(self):
        """Main method to initiate the data ingestion process"""
        logger.info("Entered the data ingestion method or component")
        
        try:
            # Download the CSV file
            self.download_file()
            logger.info("Data ingestion completed successfully")
            
            return (
                self.config.local_data_file,
            )
            
        except Exception as e:
            logger.error(f"Error occurred during data ingestion: {e}")
            raise e