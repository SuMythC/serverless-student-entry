import json
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

def lambda_handler(event, context):
    http_method = event['httpMethod']  # Get HTTP method (GET or POST)

    # Handle GET request to retrieve all student records
    if http_method == 'GET':
        try:
            response = table.scan()  # Scan the table to get all student data
            students = response.get('Items', [])
            return {
                'statusCode': 200,
                'body': json.dumps(students)  # Return student data in the response
            }
        except ClientError as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error retrieving data', 'error': str(e)})
            }

    # Handle POST request to save new student data
    elif http_method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(event['body'])

            # Extract data fields
            student_id = data.get('studentid')
            name = data.get('name')
            student_class = data.get('class')
            age = data.get('age')

            if not all([student_id, name, student_class, age]):
                return {
                    'statusCode': 400,
                    'body': json.dumps({'message': 'Missing required fields'})
                }

            # Insert the new student record into DynamoDB
            response = table.put_item(
                Item={
                    'studentid': student_id,
                    'name': name,
                    'class': student_class,
                    'age': age
                }
            )

            return {
                'statusCode': 201,
                'body': json.dumps({'message': 'Student data saved successfully'})
            }
        except ClientError as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Error saving data', 'error': str(e)})
            }
        except json.JSONDecodeError:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Invalid JSON in request body'})
            }
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method Not Allowed'})
        }
