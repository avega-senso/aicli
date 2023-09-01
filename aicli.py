#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import openai
import sys
import argparse

# Load .env file if it exists
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

def get_response_from_gpt3(prompt):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0,
        stream=True  # Assuming the API supports streaming
    )
    return response

def main(prompt=None, is_interactive=True):
    if prompt:
        response = get_response_from_gpt3(prompt)
        for chunk in response:
            if 'choices' in chunk and len(chunk['choices']) > 0 and 'content' in chunk['choices'][0]['delta']:
                print(chunk['choices'][0]['delta']['content'], end='', flush=True)  # Print chunk content on the same line immediately
        print()
        sys.exit(0)  # Terminate the script after printing the response

def get_input_from_std_streams():
    # Check for input from stdin
    input_data = sys.stdin.read().strip()
    if not input_data:
        # If nothing in stdin, try reading from stderr
        input_data = sys.stderr.read().strip()
    return input_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ai", description="Interact with OpenAI.")
    parser.add_argument('prompt', type=str, nargs='?', default=None, help="Initial prompt to provide to OpenAI.")
    args = parser.parse_args()
    
    # If a prompt argument was provided
    if args.prompt:
        main(prompt=args.prompt)
    # If data is piped into the script
    elif not sys.stdin.isatty() or not sys.stderr.isatty():
        initial_prompt = get_input_from_std_streams()
        if initial_prompt:
            main(prompt=initial_prompt, is_interactive=False)
    else:  # If the script is run interactively
        initial_prompt = input("AI% ")
        main(prompt=initial_prompt)
