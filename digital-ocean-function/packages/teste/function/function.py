import os
import boto3

from random import choice
from botocore.client import Config
from difflib import SequenceMatcher

########################################
#### Informar os valores adequados ####
aws_access_key_id = ""
aws_secret_access_key = ""
endpoint_url = ""
region_name = ""
bucket_name = ""
######################################## 

s3params = {
    'service_name': 's3',
    'use_ssl': True,
    'aws_access_key_id': aws_access_key_id,
    'aws_secret_access_key': aws_secret_access_key,
    'endpoint_url': endpoint_url,
    'config': Config(
            region_name=region_name,
            s3={'addressing_style': 'path'},
            retries={'max_attempts': 1, 'mode': 'standard'}
        )
}

s3_client = boto3.client(**s3params)
s3_resource = boto3.resource(**s3params)
s3_bucket = s3_resource.Bucket('cloud-2023')

seqdna = s3_resource.Object(bucket_name=bucket_name, key='seqdna.csv') 
seqdna = seqdna.get()['Body'].read().decode('utf-8').split('\n')

idx = list(range(len(seqdna)))


def main(args):
    """Execução na Digital Ocean Functions"""

    i1, i2 = choice(idx), choice(idx)
    s1, s2 = seqdna[i1], seqdna[i2]

    match = SequenceMatcher(None, s1, s2).find_longest_match()
    resultado = s1[match[0]:(match[0] + match[2])]
    
    return {"body": {
        "escolha": {i1: s1, i2: s2},
        "resultado": resultado
        }
    }
