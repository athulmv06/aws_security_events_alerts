## Security Events Alert
Publish in Serverless Application Repository and Deploy with AWS SAM
To publish the Evenst Alert application(Serverless application that sends alerts to a Slack channel using CloudTrail, EventBridge, and Lambda functions when matching events occur) in the AWS Serverless Application Repository and deploy it using AWS SAM, follow these steps:

Prerequisites

Before deploying the application, ensure you have the following prerequisites:

- AWS CLI installed and configured with your AWS credentials
- AWS SAM CLI installed


Deployment Steps

Follow the steps below to deploy the Events Alert application:

- Create a new directory for your project.

- Clone the repository to the new directory:
```
git clone https://github.com/2cloudfze/AWSSecurityEventsAlert
```

- Configure the AWS S3 Bucket Create an S3 bucket to package the AWS SAM application. Ensure you have a valid Amazon S3 bucket policy that grants the necessary permissions. Follow these steps to set up the bucket policy:

- Open the Amazon S3 console.
- Select the bucket you created for packaging the application.
- Go to the Permissions tab and click the Bucket Policy button.
- Paste the following policy statement into the Bucket policy editor, replacing bucketname with your bucket name and 123456789012 with your AWS account ID:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "serverlessrepo.amazonaws.com"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bucketname/*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "123456789012"
                }
            }
        }
    ]
}
```

Click Save to apply the bucket policy.

Package the AWS SAM application:
```
sam package --template-file template.yaml --s3-bucket your-bucket-name --output-template-file packaged.yaml
```

Replace your-s3-bucket with the name of your S3 bucket where the application package will be stored.

Publish your application:
```
sam publish --template packaged.yaml
```

Deploy your application:
```
sam deploy -g --capabilities CAPABILITY_NAMED_IAM
```

When prompted, provide the following deployment values:
                    
|    **Parameters/Keys**     |                                                                     **Values**                                                                      | 
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Stack Name                 | Choose a unique name for your stack.                                                                                                                |
| Capabilities               | Include the capability flag "CAPABILITY_NAMED_IAM" to acknowledge the creation of IAM resources.                                                    |
| AWS-Region                 | Your-region                                                                                                                                         |
| CreateCloudTrail           | Specify if CloudTrail needs to be created (YES/NO)                                                                                                  |
| CloudTrailName             | Provide the name for the CloudTrail you want to create. If you don't want to create a CloudTrail, set this value to 'NIL'.                          |
| S3BucketName               | Provide the name for the S3 bucket to be used by CloudTrail. If you don't want to create a CloudTrail and the S3 bucket, set this value to 'NIL'.   |
| FunctionName               | Provide the Lambda Function name                                                                                                                    |            
| SlackWebhookUrl            | Provide the Slack channel webhook URL to send alerts                                                                                                |
| EventBridgeRuleName        | Provide the EventBridge Rule Name                                                                                                                   |
| EventPattern               | Provide the EventBridge Pattern                                                                                                                     |


Make sure to replace the placeholder values with your actual values when providing the deployment inputs.

Once the deployment is complete, you can start using the application. 
When any changes or events match the event pattern, an alert is sent to the Slack channel with the Event Name, Account ID, Event Time, User, and Request Parameters.
=======
# Events Alert SAM Application

## Overview

This AWS Serverless Application Model (SAM) application is designed to send alerts to a Slack channel when specific AWS events occur. The application leverages AWS CloudTrail for monitoring, S3 for log storage, AWS Lambda for processing, and Amazon EventBridge for event pattern matching and triggering.

## Features

- **CloudTrail Integration**: Captures AWS events and logs them to an S3 bucket (if enabled).
- **Lambda Function**: Processes CloudTrail logs and sends notifications to Slack.
- **EventBridge Rule**: Defines the event pattern that triggers the Lambda function.
- **Slack Notifications**: Sends alerts to a specified Slack channel via webhook URL.

## Components

- **AWS::S3::Bucket**: Creates an S3 bucket for storing CloudTrail logs (if CloudTrail is enabled).
- **AWS::S3::BucketPolicy**: Defines permissions for CloudTrail to write logs to the S3 bucket.
- **AWS::CloudTrail::Trail**: Configures CloudTrail to log events to the S3 bucket.
- **AWS::Serverless::Function**: The Lambda function that processes events and sends notifications to Slack.
- **AWS::Events::Rule**: Sets up the EventBridge rule that triggers the Lambda function based on the event pattern.
- **AWS::Lambda::Permission**: Grants EventBridge permission to invoke the Lambda function.

## Parameters

- **CreateCloudTrail**: Specify 'YES' to create a CloudTrail or 'NO' if not required.
- **CloudTrailName**: Name of the CloudTrail to create.
- **S3BucketName**: Name of the S3 bucket for CloudTrail logs.
- **FunctionName**: Name of the Lambda function.
- **SlackWebhookUrl**: Slack webhook URL for sending notifications.
- **EventBridgeRuleName**: Name of the EventBridge rule.
- **EventPattern**: The EventBridge event pattern for triggering the Lambda function.

## Setup Instructions

1. **Clone the Repository**:

```
git clone https://github.com/athulmv06/aws_security_events_alerts.git
```
2. **Navigate to the Project Directory**:
```
cd aws_security_events_alerts
```
3. **Deploy the SAM Application**:

Ensure you have the AWS CLI and SAM CLI installed. Then, run:
```
sam deploy --guided
```
4. **Provide the Required Parameters**:

During the deployment process, provide the necessary parameter values such as CloudTrail settings, S3 bucket name, Lambda function name, Slack webhook URL, and EventBridge rule settings.

## Usage
After deployment, the application will monitor for AWS events matching the specified event pattern and send notifications to the configured Slack channel. Ensure the Lambda function has the necessary permissions and that the Slack webhook URL is correctly set up.