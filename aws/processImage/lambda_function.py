import os
import json
from textract import textract_main
from comprehend import comprehend_main
BUCKET = os.environ['BUCKET']
REGION = os.environ['REGION']
# DOCUMENT = 'print.pbm'

def lambda_handler(event, context):
    body = json.loads(event['body'])
    DOCUMENT = body["object_name"]
    summary = textract_main(BUCKET, DOCUMENT, REGION)
    entities = comprehend_main(REGION, " ".join(summary))
    
    entities_dic = {
        "ANATOMY" : [],
        "MEDICAL_CONDITION" : [],
        "MEDICATION" : [],
        "PROTECTED_HEALTH_INFORMATION" : [],
        "TEST_TREATMENT_PROCEDURE" : [],
        "DOSAGE" : []
    }
    for e in entities:
        c = e['Category']
        entities_dic[c].append(e['Text'])
        if 'Attributes' in e:
            a_list = e['Attributes']
            for a in a_list:
                if a['RelationshipType'] == 'DOSAGE':
                    entities_dic['DOSAGE'].append({
                        e['Text']: a['Text']
                    })
    entities_dic = {key:list(set(entities_dic[key])) for key in entities_dic}
    output = {
        "summary": " ".join(summary),
        "entities": entities,
        "entities_dic": entities_dic
    }
    return {
        "statusCode": 200,
        "body" : json.dumps(output),
        "headers": {"Content-Type": "application/json"}
    }