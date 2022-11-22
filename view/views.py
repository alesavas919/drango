from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

elements = [
    {
    "table":"random",
    "container":"random",
    "prod_name":"random",
    "buyer":"random",
    "condition":"random",
    "owner":"random",
    "sold":"random",
    "stock":"random",
    "price":"random",
    },
]

def index(request):
    global elements
    data = {'name':'test','group':elements}
    return render(request, "Index.html",context=data)

def test(request):

    return HttpResponse("Prueba")

def find(request):
    global elements
    data = {'name':'test','group':elements}

    return render(request,"Index.html",data)

import boto3
from boto3.dynamodb.conditions import Key

def putItem(request):

    table = request.POST["table"]
    container = request.POST["container"]
    prod_name = request.POST["prod_name"]
    buyer = request.POST["buyer"]
    condition = request.POST["condition"]
    owner = request.POST["owner"]
    sold = request.POST["sold"]
    stock = request.POST["stock"]
    price = request.POST["price"]
   
    

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
