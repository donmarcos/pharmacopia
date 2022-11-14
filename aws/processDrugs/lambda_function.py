import os
import requests, json
import boto3

from util import *
REGION = os.environ['REGION']
CLIENT = boto3.client('dataexchange', region_name = REGION)
# DATA_SET_ID = 'b5c571b26671fc8b73a1146b140f0d75'
# REVISION_ID = '9ae2799c1227cc58002a946e27410dd3'
# ASSET_ID = '245ba9ec692792d750753ab605f388d2'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    drug_name = body["drug"]
    response = drugs_fda(drug_name)
    body = json.loads(dict(response)['Body'])
    products = body['results'][0]['products'][0]
    details = {
        'brand_name': products['brand_name'],
        'active_ingredients': products['active_ingredients'],
        'route': products['route'],
        'dosage_form': products['dosage_form']
    }
    response = drugs_label(drug_name)
    body = json.loads(dict(response)['Body'])
    temp = {
        'warnings': body['results'][0]['warnings'],
        'adverse_reactions': body['results'][0]['adverse_reactions'],
        'contraindications': body['results'][0]['contraindications'],
        'information_for_patients': body['results'][0]['information_for_patients']
    }
    details.update(temp)
    response = drugs_ndc(drug_name)
    body = json.loads(dict(response)['Body'])
    details['pharm_class'] = body['results'][0]['pharm_class']
    response = drugs_enforcement(drug_name)
    body = json.loads(dict(response)['Body'])
    details['reason_for_recall'] = body['results'][0]['reason_for_recall']

    return {
        "statusCode": 200,
        "body" : json.dumps(details),
        "headers": {"Content-Type": "application/json"}
    }