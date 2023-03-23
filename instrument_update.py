import uuid
import boto3
import logging



TABLE_NAME =  'instruments'

ENDPOINT = 'http://localhost:8000'


def put_item(id, category, desc):
    Item={
        'id': {
          'S': id
        },
        'catergory': {
          'S': category
        },
        'desc': {
          'S':desc
        }
    }

    try:
      db_client = boto3.client('dynamodb', endpoint_url=ENDPOINT)
      db_client.put_item(Item=Item,TableName=TABLE_NAME)
      return True
    except Exception as e:
      logging.error(e)
      return False

def lambda_handler(event, _) -> str:
  uuid_val = uuid.uuid49.hex
  if put_item(uuid_val,event['category'], event['desc']) == True:
    logging.info(f"Success, Item {uuid_val} added to table {TABLE_NAME}")
    return uuid_val

  logging.error("Error, item not added to table {TABLE_NAME}")
  return None