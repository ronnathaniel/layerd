"""
[D]ownload [P]ublic [L]ayers
"""

import os


__author__ = 'ronnathaniel'

__usage__ = '' + \
'Usage:     \n' + \
'\tdpl <ARN>  \n' + \
'\t@arg ARN being an Amazon Resource Name of a Public AWS Lambda Layer. \n'

__region__ = os.environ.get('AWS_REGION')
