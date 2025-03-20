from notifications_python_client.notifications import NotificationsAPIClient
from dotenv import load_dotenv
import os

load_dotenv()

INCLUDED_TEMPLATE_IDS = [
  "6aa04f0d-94c2-4a6b-af97-a7369a12f681"
]

api_key = os.getenv('NOTIFY_API_KEY')
notifications_client = NotificationsAPIClient(api_key)

response = notifications_client.get_all_templates()
all_templates = response.get('templates', [])

templates = [template for template in all_templates if template.get('id', '') in INCLUDED_TEMPLATE_IDS]

