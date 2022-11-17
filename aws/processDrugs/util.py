import requests, json
from lambda_function import *

REGION = os.environ['REGION']
CLIENT = boto3.client('dataexchange', region_name = REGION)
DATA_SET_ID = os.environ['DATA_SET_ID']
REVISION_ID = os.environ['REVISION_ID']
ASSET_ID = os.environ['ASSET_ID']

def drugs_fda(drug_name):
    QUERY_STRING_PARAMETERS = {'search': drug_name.upper()}
    response = CLIENT.send_api_asset(
        DataSetId=DATA_SET_ID,
        RevisionId=REVISION_ID,
        AssetId=ASSET_ID,
        Method='GET',
        Path='/drug/drugsfda.json',
        QueryStringParameters=QUERY_STRING_PARAMETERS
    )
    return response

def drugs_label(drug_name):
    QUERY_STRING_PARAMETERS = {'search': drug_name.upper()}
    response = CLIENT.send_api_asset(
        DataSetId=DATA_SET_ID,
        RevisionId=REVISION_ID,
        AssetId=ASSET_ID,
        Method='GET',
        Path='/drug/label.json',
        QueryStringParameters=QUERY_STRING_PARAMETERS
    )
    return response

def drugs_ndc(drug_name):
    QUERY_STRING_PARAMETERS = {'search': drug_name.upper()}
    response = CLIENT.send_api_asset(
        DataSetId=DATA_SET_ID,
        RevisionId=REVISION_ID,
        AssetId=ASSET_ID,
        Method='GET',
        Path='/drug/ndc.json',
        QueryStringParameters=QUERY_STRING_PARAMETERS
    )
    return response

def drugs_enforcement(drug_name):
    QUERY_STRING_PARAMETERS = {'search': drug_name.upper()}
    response = CLIENT.send_api_asset(
        DataSetId=DATA_SET_ID,
        RevisionId=REVISION_ID,
        AssetId=ASSET_ID,
        Method='GET',
        Path='/drug/enforcement.json',
        QueryStringParameters=QUERY_STRING_PARAMETERS
    )
    return response

def drugs_alternative(drug_name):
    QUERY_STRING_PARAMETERS = {'search': drug_name.upper()}
    response = CLIENT.send_api_asset(
        DataSetId=DATA_SET_ID,
        RevisionId=REVISION_ID,
        AssetId=ASSET_ID,
        Method='GET',
        Path='/drug/drugsfda.json',
        QueryStringParameters=QUERY_STRING_PARAMETERS
    )
    return response