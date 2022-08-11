"""
Layerd. Download Lambda Layers.
"""

import os
import sys
import boto3
import botocore
from io import BytesIO
import requests
from threading import Timer
import typing
import zipfile

from layerd.package import __usage__
from layerd.utils import (
    _flag_add_region,
    _flag_parent_dir,
    _progress_bar,
    _stdout_del_last_row,
)


def parse_cli_args() -> str:
    """
    @returns ARN: str.
    """
    args = [*sys.argv]
    args.pop(0)
    if (not args) or ('help' in args[0].lower()):
        print(__usage__)
        return
    arn = args[0]

    # don't be tempted to return early. leave room for expansion.
    #   - Confucius [Date Unknown]

    return arn


def mount(arn: str = None) -> None:
    """
    @arg arn: str. ARN of Public (Authorized) Lambda Layer.
    """
    arn = arn or parse_cli_args()
    names = arn.split(':')
    if not (6 <= len(names) <= 8):
        print(__usage__)
        print('Error: <ARN> not valid. Recieved ' + arn)
        exit(1)
    region: str = names[3]
    layer_q: str = names[5]
    layer_name: str = names[6]
    version: int = int(names[-1])

    # boto3's LambdaClient.get_layer_version() accepts the arn
    # without a version. arn_vless: str is just that.
    names_vless: typing.List[str] = [*names]
    names_vless.pop(-1)
    arn_vless: str = ':'.join(names_vless)

    print('Layer:\t', layer_name)
    print('Region:\t', region)
    print('V:\t', version)

    client_lambda = boto3.client('lambda', region_name=region)
    _progress_bar(1, 10, message='Pulling')

    try:
        layer_version_d = client_lambda.get_layer_version(LayerName=arn_vless, VersionNumber=version)
    except botocore.exceptions.ClientError as err:
        _stdout_del_last_row()
        print('\nError:', err)
        return

    _progress_bar(3, 10, message='Addressing')
    layer_address = layer_version_d.get('Content', {}).get('Location', '')
    res = requests.get(layer_address, stream=True)
    _progress_bar(6, 10, message='Unzipping')
    zip = zipfile.ZipFile(BytesIO(res.content))
    _progress_bar(7.2, 10)
    layer_dir = os.path.join(
        _flag_parent_dir,
        f'{layer_q}-{layer_name}-{version}'
    )
    if _flag_add_region:
        layer_dir += f'-{region}'
    _progress_bar(8.8, 10, message='Extracting')
    zip.extractall(layer_dir)
    _progress_bar(10, 10, message='Done')
    print()
    print(f'Created: {layer_dir}/')


if __name__ == '__main__':
    mount()
