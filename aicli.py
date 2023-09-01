#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import openai
import sys
import argparse
import re

# Load .env file if it exists
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

# Dynamically load patterns from the .env file
patterns = [os.getenv(f'PATTERN_{i}') for i in range(1, 100) if os.getenv(f'PATTERN_{i}')]

def sanitize_message(error_msg):
    sanitized_msg = error_msg
    for pattern in patterns:
        sanitized_msg = re.sub(pattern, '[REDACTED]', sanitized_msg)
    return sanitized_msg


def get_response_from_gpt3(prompt, model='gpt-3.5-turbo', temperature=0):
    messages = [{'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        stream=True
    )
    return response

def main(prompt=None, model='gpt-3.5-turbo', temperature=0, is_interactive=True, sanitize=False):
    if sanitize:
        prompt = sanitize_message(prompt)
    try:
        response = get_response_from_gpt3(prompt, model, temperature)
        for chunk in response:
            if 'choices' in chunk and len(chunk['choices']) > 0 and 'content' in chunk['choices'][0]['delta']:
                content = chunk['choices'][0]['delta']['content']
                print(content, end='', flush=True)
        print()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def get_input_from_std_streams():
    input_data = sys.stdin.read().strip()
    if not input_data:
        input_data = sys.stderr.read().strip()
    return input_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ai", description="Interact with OpenAI.")
    parser.add_argument('prompt', type=str, nargs='?', default=None, help="Initial prompt to provide to OpenAI.")
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo', help="Model to use for the interaction.")
    parser.add_argument('--temperature', type=float, default=0, help="Temperature setting for the model's response.")
    parser.add_argument('--sanitize', action="store_true", help="Sanitize the message to redact sensitive information.")

    args = parser.parse_args()
    
    if args.prompt:
        main(prompt=args.prompt, model=args.model, temperature=args.temperature, sanitize=args.sanitize)
    elif not sys.stdin.isatty() or not sys.stderr.isatty():
        initial_prompt = get_input_from_std_streams()
        if initial_prompt:
            main(prompt=initial_prompt, model=args.model, temperature=args.temperature, sanitize=args.sanitize, is_interactive=False)
    else:
        initial_prompt = input("AI% ")
        main(prompt=initial_prompt, model=args.model, temperature=args.temperature, sanitize=args.sanitize)