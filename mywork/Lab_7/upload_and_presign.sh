#!/bin/bash

FILE_NAME=$1
BUCKET=$2
EXPIRES=${3:-604800}

aws s3 cp $FILE_NAME s3://$BUCKET/

aws s3 presign --expires-in $EXPIRES s3://$BUCKET/$(basename $FILE_NAME)
