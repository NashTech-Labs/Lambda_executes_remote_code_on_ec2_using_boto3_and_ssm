# Lambda_executes_remote_code_on_ec2_using_boto3_and_ssm

Set up a Python Lambda that executes remote code on an EC2. Use the boto3 library and SSM

# Prerequisite

Make the IAM role for the service EC2 with the permission of AmazonSSMManagedInstanceCore

Create the EC2 instance (ubuntu 18.04-amd64-server) and attached to the above role

Make another role for lambda with permissions of AmazonEC2FullAccess , AmazonSSMFullAccess and AWSLambdaExecute

Create the lambda function and attached the existing role with that

Paste the python script in lamda function code
