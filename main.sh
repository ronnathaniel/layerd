
URL=$(aws lambda get-layer-version-by-arn --arn arn:aws:lambda:us-east-1:066549572091:layer:epsagon-node-layer:333 --query Content.Location --output text)
mkdir dplayer && cd dplayer
curl $URL -o layer.zip
open .
