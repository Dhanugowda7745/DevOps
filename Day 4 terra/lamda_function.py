import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return {
        'statusCode': 200,
        'body': f'Buckets: {buckets}'
    }
