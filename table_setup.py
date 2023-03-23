import logging
import time
import boto3
from botocore.exceptions import ClientError

INDEX_NAME_DT = 'InstrumentidIndex'
INDEX_NAME_P = 'SecondIdIndex'
table_name = 'instruments'
ENDPOINT = 'http://localhost:8000'

def create_table():

    try:
        db_client = boto3.client('dynamodb', endpoint_url = ENDPOINT)
        db_client.create_table(
          AttributeDefinitions=[
             {
                  'AttributeName': 'id',
                  'AttributeType': 'S',
              },
              {
                  'AttributeName': 'category',
                  'AttributeType': 'S',
              },
              {
                  'AttributeName': 'desc',
                  'AttributeType': 'S',
              }
          ],
          KeySchema=[
              {
                  'AttributeName': 'id',
                  'KeyType': 'HASH',
              },
              {
                  'AttributeName': 'category',
                  'KeyType': 'RANGE',
              }             
          ],
          ProvisionedThroughput={
              'ReadCapacityUnits': 2,
              'WriteCapacityUnits': 2,
          },
          GlobalSecondaryIndexes=[
          {
                'IndexName': INDEX_NAME_DT,
                'KeySchema': [
                    {
                        'AttributeName': 'category',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'id',
                        'KeyType': 'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 2,
                    'WriteCapacityUnits': 2
                }
            },
            {
                'IndexName': INDEX_NAME_P,
                'KeySchema': [
                    {
                      'AttributeName': 'category',
                      'KeyType': 'HASH'
                    },
                    {
                      'AttributeName': 'desc',
                      'KeyType': 'RANGE'
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 2,
                    'WriteCapacityUnits': 2
                }
            },
          ],          
          TableName= table_name,
        )
        #time.sleep(120)
        return True
        
    except ClientError as e:
        logging.error(e)
        return False


def delete_table():

    try:
        db_client = boto3.client('dynamodb', enpoint_url = ENDPOINT)
        db_client.delete_table(TableName=table_name)
        return True
    except ClientError as e:
        logging.error(e)
        return False





#main function
def main():

    user_choice = 'x'
    while user_choice != "q":
        print("What would you like to do? (Inputs are case sensitive) \n Create a table (C)  \n Delete whole table (D)")
        user_choice = input()
        if user_choice == "C":
#get info for creating table
            create_table(table_name) #call the function
            
        elif user_choice == "D":
#get info for delete table 
            print("\nWhat was the name of your table?")
            user_table_name = input()

            delete_table(user_table_name) #call the function

    print("\nEnd of program\n") #end of program to screen

main() #call main
