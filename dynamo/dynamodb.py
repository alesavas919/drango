#from boto3 import client,resource as boto3
#import boto3
#awscli
import boto3
from boto3.dynamodb.conditions import Key

def putItem(table
            ,container
            ,prod_name
            ,buyer
            ,condition
            ,owner
            ,sold
            ,stock
            ,price):

    table.put_item(
        Item={
            "container": container,
            "prod_name": prod_name,
            "buyer": buyer,
            "condition": condition,
            "owner": owner,
            "sold": sold,
            "stock": stock,
            "price":price,
        }
    )

def getItemsByCondition(table):
    resp = table.query(
        IndexName="condition-sold-index",
        KeyConditionExpression=Key('condition').eq('new') & Key('sold').eq(0),
    )
    return resp["Items"]

def getProductsByOwner(table):
    resp = table.query(
        # Add the name of the index you want to use in your query.
        IndexName="owner-index",
        KeyConditionExpression=Key('owner').eq('Anonimo'),
    )
    return resp["Items"]

def getProductByCondition(table):
    resp = table.query(
        # Add the name of the index you want to use in your query.
        IndexName="prod_name-condition-index",
        KeyConditionExpression=Key('prod_name').eq('Anonimo') & Key('condition').eq('new'),
    )
    return resp["Items"]

def init():
    pass
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


    #primary_column_name = "Sr"
    #primary_key = 1
    #columns=["Age","First","Last"]

    #client = boto3.client("dynamodb")



    #print(element["Item"])
    #table.get_item({primary_column_name:primary_key})


    #response = table.get_item({Key = {primary_column_name:primary_key}})

    #arn:aws:dynamodb:us-east-1:964932001346:table/productweb

    #print("rango")

