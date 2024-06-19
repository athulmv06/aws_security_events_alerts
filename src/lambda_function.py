import json
import urllib3
import os
    

def lambda_handler(event, context):
    # Log the event to understand its structure
    print(json.dumps(event))

    try:
        # Extract details from the event
        detail = event.get('detail', {})
        event_name = detail.get('eventName', 'N/A')
        user_identity = detail.get('userIdentity', {})
        user_name = user_identity.get('userName', 'N/A')
        account_id = user_identity.get('accountId', 'N/A')
        request_parameters = detail.get('requestParameters', {})
        event_time = detail.get('eventTime', 'N/A')

        # Format the Request Parameters section
        request_params_formatted = ',\n'.join([f'{key}: {value}' for key, value in request_parameters.items()])

        # Slack webhook URL (replace with your actual Slack webhook URL)
        slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL')
        if not slack_webhook_url:
            raise ValueError('SLACK_WEBHOOK_URL environment variable is not set')

        # Create the Slack message with blocks and alignments
        slack_message = {
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': '*IAM Event Occurred*',
                    },
                },
                {
                    'type': 'section',
                    'fields': [
                        {
                            'type': 'mrkdwn',
                            'text': f'*Event:*\t{event_name}',
                        },
                        {
                            'type': 'mrkdwn',
                            'text': f'*User:*\t{user_name}',
                        },
                        {
                            'type': 'mrkdwn',
                            'text': f'*Account ID:*\t{account_id}',
                        },
                        {
                            'type': 'mrkdwn',
                            'text': f'*Request Parameters:*\n{request_params_formatted}',
                        },
                        {
                            'type': 'mrkdwn',
                            'text': f'*Event Time:*\t{event_time}',
                        },
                    ],
                },
                # Add vertical spacing
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': '\n\n\n\n',
                    },
                },
                {
                    'type': 'divider'
                },
                {
                    'type': 'divider'
                },
            ],
        }
        
        # Send the message to Slack
        http = urllib3.PoolManager()
        response = http.request(
            'POST',
            slack_webhook_url,
            body=json.dumps(slack_message),
            headers={'Content-Type': 'application/json'}
        )
        
        return {
            'statusCode': response.status,
            'body': response.data.decode('utf-8')
        }
    except KeyError as e:
        print(f'KeyError: {e}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
