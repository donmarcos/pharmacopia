import boto3
SERVICE_NAME = "comprehendmedical"

def comprehend_main(region, text):
    client = boto3.client(service_name=SERVICE_NAME, region_name=region)
    result = client.detect_entities(Text=text)
    entities = result['Entities']
    return entities