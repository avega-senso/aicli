#!/usr/bin/env python
import os
import openai
import sys
import argparse

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://y2kiidz6fgoomcw45rlul6cnki0wgbcc.lambda-url.us-west-1.on.aws/v1"

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
        content = ""
        for chunk in response:
            if 'choices' in chunk and len(chunk['choices']) > 0 and 'content' in chunk['choices'][0]['delta']:
                content += chunk['choices'][0]['delta']['content']
        print(content)
    
    if not is_interactive:
        return

    try:
        while True:
            user_input = input("Enter your question or prompt: ")
            
            # Check for exit command
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting...")
                break

            response = get_response_from_gpt3(user_input)
            content = ""
            for chunk in response:
                if 'choices' in chunk and len(chunk['choices']) > 0 and 'content' in chunk['choices'][0]['delta']:
                    content += chunk['choices'][0]['delta']['content']
            print(content)
    except KeyboardInterrupt:
        print("\nExiting...")  # Print an exit message when Ctrl+C is pressed

def get_input_from_std_streams():
    # Check for input from stdin
    input_data = sys.stdin.read().strip()
    if not input_data:
        # If nothing in stdin, try reading from stderr
        input_data = sys.stderr.read().strip()
    return input_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interact with GPT-3.")
    parser.add_argument('--prompt', type=str, default=None, help="Initial prompt to provide to GPT-3.")
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
        initial_prompt = input("Enter initial prompt: ")
        main(prompt=initial_prompt)

