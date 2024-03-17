# test_data_processing.py
import unittest
import json
from data_processing import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    def test_total_sales_calculation(self):
        """Test the lambda_handler function to ensure it calculates total sales correctly."""
        # Define a test event with a list of sales
        test_event = {
            "sales": [
                {"amount": 100},
                {"amount": 150},
                {"amount": 250}
            ]
        }
        test_context = {}  # Context is not used in this example
        
        # Expected total sales is the sum of amounts
        expected_total_sales = 500
        
        # Call the function
        result = lambda_handler(test_event, test_context)
        
        # Check the statusCode and total_sales in the body of the response
        self.assertEqual(result['statusCode'], 200)
        result_body = json.loads(result['body'])
        self.assertEqual(result_body['total_sales'], expected_total_sales)

if __name__ == '__main__':
    unittest.main()
