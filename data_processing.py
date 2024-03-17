# data_processing.py
import json

def lambda_handler(event, context):
    print("This log is a new addition to verify deployment.")
    # Assume this is your modified data processing logic
    print("Calculating total sales...")
    
    total_sales = sum(item['amount'] for item in event['sales'])
    
    return {
        'statusCode': 200,
        'body': json.dumps({"total_sales": total_sales})
    }
