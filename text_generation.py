"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["AIzaSyAvrxOyAVzPVcnzxuD0mjKVDyS2bNWfC10"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "stop_sequences": [
    "🥰",
    "😡",
    "😂",
  ],
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  upload_to_gemini("1A3S8goubZicoMz_TEYtWVBKl_dGBJJYC", mime_type="application/octet-stream"),
]

response = model.generate_content([
  files[0],
  "\n\nProvides accurate information and answer queries across a wide range of topics.Assist with Tasks: Help users with tasks such as setting reminders, providing directions, or managing schedules.Depth learning and Adapt: Use machine learning to improve responses over time based on interactions.Understand Context: Grasp the context of conversations to provide relevant and appropriate responses.Generate and build Contents: Create imaginative and innovative content like stories, poems, code, and more. Build, create,perform robots , machines and bot functions .Maintain Ensure user data is handled with confidentiality and respect for privacy.Safe and Respectful: Follow ethical guidelines to ensure safety and respect for all users. Be Accessible: Be user-friendly and accessible to people with different abilities and from various backgrounds.",
  "Web4 AI Browser Compatibility",
  "Ensuring the web app works across all browsers.",
  " Run ",
  "Web4 AI Interface",
  "Main interface for viewport, integrates Discord APIs.",
  " Run ",
  "Web4 AI Page",
  "Main interface for chatting after successful login.",
  " Run ",
  "Web4 AI Chat with  Members",
  "Allows users to chat with each other in a Discord API server integration",
  " Run ",
  "Web4 AI Cloud Infrastructure",
  "google cloud services to host the application.",
  " Run ",
  "Web4 AI Cloud Integration",
  "Integration with Microsoft's,google,mongodb,cloud flare cloud services for data storage and processing.",
  " Run ",
  "Web4 AI Authorization",
  "User logs in using Discord credentials for authorization.",
  " Run ",
  "Web4 AI Discord API Integration",
  "Integration with Discord API to enable  web and chat functionality.",
  " Run ",
  "Web4 AI Google Chat API Integration",
  "Integration with Google Chat API to enable web chatting functionality.",
  " Run ",
  "Web4 AI Handling",
  "Processes for sending and receiving data within the application.",
  " Run ",
  "Web4 AI Access",
  "The first action when someone uses the WEB4 application.",
  " Run ",
  "Web4 AI ",
  " Run ",
])

print(response.text)

