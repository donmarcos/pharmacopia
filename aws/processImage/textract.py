import boto3
import io
from PIL import Image

def process_text_detection(bucket, document, region):
    s3_connection = boto3.resource('s3')            
    s3_object = s3_connection.Object(bucket,document)
    s3_response = s3_object.get()

    stream = io.BytesIO(s3_response['Body'].read())
    image=Image.open(stream)

    client = boto3.client('textract', region_name=region)
    response = client.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket, 'Name': document}})
    return response

def textract_main(bucket, document, region):
    response=process_text_detection(bucket,document,region)
    summary = []
    for x in response['Blocks']:
        if 'Text' not in x:
            continue
        summary.append(x['Text'])
    return summary
