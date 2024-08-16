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
