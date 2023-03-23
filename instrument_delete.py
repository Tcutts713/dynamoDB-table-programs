
import boto3
import logging



TABLE_NAME =  'instruments'

ENDPOINT = 'http://localhost:8000'

def delete_item(id):

    try:
      db_client = boto3.client('dynamodb')
      db_client.delete_item(
        Key={
          'id': {
            'S': id,
          },  
        },
        TableName=TABLE_NAME,
      )
      return True
    except Exception as e:
      logging.error(e)
      return False

def lambda_handler(event, _) -> str:
  if delete_item(event['id']) == True:
    item = (f"Item from {TABLE_NAME}, {event['id']} deleted"))
    return {
      'message': item
    }

  logging.error("Error, item not deleted from table {TABLE_NAME}")
  return None
