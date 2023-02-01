import time
import json
import boto3


def lambda_handler(event, context):

   
    client = boto3.client("ec2")
    ssm = boto3.client("ssm")

    # getting information
    describeInstance = client.describe_instances()

    InstanceId = []
    # fetchin instance id 
    for i in describeInstance["Reservations"]:
        for instance in i["Instances"]:
            if instance["State"]["Name"] == "running":
                InstanceId.append(instance["InstanceId"])

    # looping instance ids
    for instanceid in InstanceId:
        # command executed on instance
        response = ssm.send_command(
            InstanceIds=[instanceid],
            DocumentName="AWS-RunShellScript",
            Parameters={
                "commands": ["mkdir -p /home/ubuntu/bb"]
            }, 
        )

        # command id for the output
        command_id = response["Command"]["CommandId"]

        time.sleep(3)

        # fetching command output
        output = ssm.get_command_invocation(CommandId=command_id, InstanceId=instanceid)
        print(output)

    return {"statusCode": 200, "body": json.dumps("Thanks from knoldus!")}
