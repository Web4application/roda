# myproject/settings.py
import os

INSTALLED_APPS = [
...
'myapp',
]

# Add your OpenAI API key here
OPENAI_API_KEY = os.getenv('AIzaSyAvrxOyAVzPVcnzxuD0mjKVDyS2bNWfC10')
