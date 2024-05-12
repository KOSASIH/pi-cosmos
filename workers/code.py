import os
import time
import logging
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Set up API keys and other configuration
API_KEY = os.getenv('PI_COSMOS_API_KEY')
API_URL = 'https://api.pi-cosmos.com/v1'

def send_email(to, subject, body):
    """Send an email using the Pi Cosmos API."""
    data = {
        'to': to,
        'subject': subject,
        'body': body,
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }
    response = requests.post(f'{API_URL}/email', json=data, headers=headers)
    if response.status_code != 200:
        logging.error(f'Failed to send email: {response.text}')

def process_image(image_path):
    """Process an image using the Pi Cosmos API."""
    with open(image_path, 'rb') as f:
        image_data = f.read()
    data = {
        'image': image_data,
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }
    response = requests.post(f'{API_URL}/image', json=data, headers=headers)
    if response.status_code != 200:
        logging.error(f'Failed to process image: {response.text}')

def generate_report(data):
    """Generate a report using the Pi Cosmos API."""
    data = {
        'data': data,
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }
    response = requests.post(f'{API_URL}/report', json=data, headers=headers)
    if response.status_code != 200:
        logging.error(f'Failed to generate report: {response.text}')

def main():
    """Main function for the worker."""
    while True:
        # Check for new tasks
        tasks = get_tasks()
        for task in tasks:
            # Process the task
            if task['type'] == 'email':
                send_email(task['to'], task['subject'], task['body'])
            elif task['type'] == 'image':
                process_image(task['image_path'])
            elif task['type'] == 'report':
                generate_report(task['data'])
            # Mark the task as complete
            mark_task_complete(task['id'])
        # Sleep for a while
        time.sleep(60)

def get_tasks():
"""Get a list of new tasks from the Pi Cosmos API."""
    data = {
        'status': 'new',
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }
    response = requests.get(f'{API_URL}/task', params=data, headers=headers)
    if response.status_code != 200:
        logging.error(f'Failed to get tasks: {response.text}')
        return []
    return response.json()['tasks']

def mark_task_complete(task_id):
    """Mark a task as complete in the Pi Cosmos API."""
    data = {
        'id': task_id,
        'status': 'complete',
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }
    response = requests.put(f'{API_URL}/task', json=data, headers=headers)
    if response.status_code != 200:
        logging.error(f'Failed to mark task complete: {response.text}')

if __name__ == '__main__':
    main()
