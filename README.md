# Lambda_executes_remote_code_on_ec2_using_boto3_and_ssm

Set up a Python Lambda that executes remote code on an EC2. Use the boto3 library and SSM

# Prerequisite

1. Make the IAM role for the service EC2 with the permission of AmazonSSMManagedInstanceCore

2. Create the EC2 instance (ubuntu 18.04-amd64-server) and attached to the above role

3. Make another role for lambda with permissions of AmazonEC2FullAccess , AmazonSSMFullAccess and AWSLambdaExecute

4. Create the lambda function and attached the existing role with that

5. Paste the python script in lamda function code
