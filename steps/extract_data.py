# API public Gael
import requests

# extract all divisas
# response = requests.get("https://api.gael.cloud/general/public/monedas")

# extract for codig

# response = requests.get("https://api.gael.cloud/general/public/monedas/USD")

import requests
import schedule
import time
import json
import logging

# Configure logging
logging.basicConfig(filename='api_extraction.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data():
    try:
        # Make API request to extract 
        response = requests.get("https://api.gael.cloud/general/public/monedas/USD")
        
        if response.status_code == 200:
            # Process the response data
            data = response.json()
            
            # TODO: Data processing and transformation
            with open('extracted_data.json', 'a') as f:
                json.dump(data, f, indent=4)

            
            # Log success
            logging.info('Data extraction successful')
        else:
            # Log error if API request fails
            logging.error(f'Failed to extract data. Status code: {response.status_code}')
    except Exception as e:
        # Log any exceptions that occur during extraction
        logging.error(f'Exception occurred during data extraction: {str(e)}')

# Schedule data extraction every 30 minutes
schedule.every(30).minutes.do(extract_data)

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(1)
