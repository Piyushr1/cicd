# data_processing.py
import json

def lambda_handler(event, context):
    # Simulate processing sales data contained in the event
    print("Calculating total sales...")
    
    total_sales = sum(item['amount'] for item in event['sales'])
    
    return {
        'statusCode': 200,
        'body': json.dumps({"total_sales": total_sales})
    }
