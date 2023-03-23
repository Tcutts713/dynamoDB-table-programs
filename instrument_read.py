import boto3
import logging



TABLE_NAME =  'instruments'

ENDPOINT = 'http://localhost:8000'
def get_item(id,category):

    try:
      db_client = boto3.client('dynamodb', endpoint_url=ENDPOINT)
      db_client.get_item(
        Key={
          'id': {
            'S': id,
          },
          'category': {
              'S': category,
          },      
        },
        TableName=TABLE_NAME,
      )
      return True
    except Exception as e:
      logging.error(e)
      return False

def lambda_handler(event, _) -> str:
  if get_item(event['id'], event['category']) == True:
    item = (f"Item from {TABLE_NAME}", (event['id'], event['category']))
    return {
      'message': item
    }

  logging.error("Error, item not read from table {TABLE_NAME}")
  return None