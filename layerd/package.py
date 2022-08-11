"""
Layerd. Inspect Lambda Layers.
"""

import os

__author__ = 'ronnathaniel'
__license__ = 'MIT'
__usage__ = '' + \
            'Usage:     \n' + \
            '\tlayerd <ARN>  \n' + \
            '\t\t@arg ARN being an Amazon Resource Name of a Public AWS Lambda Layer. \n' + \
            '\t\t@example arn:aws:lambda:REGION:ACC:layer:NAME:VERSION. \n' + \
            '\tFeature Flags (By Environment): \n' + \
            '\t\tLAYERD_REGION=TRUE for REGION in DIR. \n' + \
            '\t\t\tDefault=FALSE \n' + \
            '\t\tLAYERD_PARENT_DIR=<PATH> \n' + \
            '\t\t\tDefault=. \n'
__region__ = os.environ.get('AWS_REGION')
