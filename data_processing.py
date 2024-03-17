# data_processing.py
import json

def lambda_handler(event, context):
    # Your data processing logic here
    print("Processing data...")

    # Example: simple data processing
    processed_data = {"message": "Data processed successfully"}

    return {
        'statusCode': 200,
        'body': json.dumps(processed_data)
    }
