"""
[D]ownload [P]ublic [L]ayers
"""

import sys
import boto3
from io import BytesIO
import requests
import zipfile

from dpl import __usage__

def run():
    args = [*sys.argv]
    _ = args.pop(0)
    if not args:
        print(__usage__)
        exit(1)
    arn = args[0]
    names = arn.split(':')
    if not (6 <= len(names) <= 8):
        print(__usage__)
        print('Error: <ARN> not valid. Recieved ' + arn)
        exit(1)
    region = names[3]
    version = int(names[-1])
    names_vless = [*names]
    _ = names_vless.pop(-1)
    arn_vless = ':'.join(names_vless)

    client_lambda = boto3.client('lambda', region_name=region)
    version = client_lambda.get_layer_version(LayerName=arn_vless, VersionNumber=version)
    layer_address = version.get('Content', {}).get('Location', '')
    res = requests.get(layer_address, stream=True)
    zip = zipfile.ZipFile(BytesIO(res.content))
    zip.extractall(f'{names[5]}-{names[6]}-{names[7]}')
    print('done.')

if __name__ == '__main__':
    run()
