# Use requests library to make HTTP POST request to OpenAI API
# Using API completions endpoint, our API key, and a prompt for
# the AI model selected.
# Get response, validate it, and see response
# Input Arguments
# - Topic of python script
# - Output file name
# Output: Python script file with AI response
import requests
import argparse
import os

# Get argument to use as prompt
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="Prompt to use for AI model")
parser.add_argument("file_name", help="Name of file to save output to")
args = parser.parse_args()

# From https://platform.openai.com/docs/api-reference/completions
api_endpoint = "https://api.openai.com/v1/completions"
# Get from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Example curl API call used to create HTTP POST
# max_tokens : Maximum tokens in response
# temperature : Randomness/creativeness of response, use 0.5 for balance
# curl https://api.openai.com/v1/completions \
#   -H "Content-Type: application/json" \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -d '{
#     "model": "text-davinci-003",
#     "prompt": "Say this is a test",
#     "max_tokens": 7,
#     "temperature": 0
#   }'

# Headers for OpenAI API call
request_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# Data for OpenAI API call with prompt
request_data = {
    "model": "text-davinci-003",
    "prompt": f"Write python script for {args.prompt}. Provide only code, no text",
    "max_tokens": 500,
    "temperature": 0.5,
}

# Call OpenAI API with request data set above
response = requests.post(api_endpoint, headers=request_headers, json=request_data)

# Validate response
if response.status_code == 200:
    # Save/Show response
    # print(response.json()["choices"][0]["text"])
    # Save response, write mode to a new file from input
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")
    raise Exception(response.status_code, response.text)
