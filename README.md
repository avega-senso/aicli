# AI CLI tool - Interact with OpenAI from the cli

Overview
The AI CLI tool provides a simple and direct interface to interact with OpenAI's models from the command line. By leveraging the powerful capabilities of OpenAI, you can quickly obtain responses for any given prompt.

Whether you're integrating with your workflow or just wanting to have a conversation, this CLI tool simplifies the process. It's designed with flexibility in mind, allowing both interactive sessions and the ability to pipe in data for automated tasks.

## Features
### Direct Interactivity
Launch the tool and immediately start a conversation with OpenAI.
### Support for Piped Data
Use other tools in conjunction with this CLI to send data directly into the script.
### Sanitization Feature
The sanitization feature in this script allows users to redact potentially sensitive information from the provided input. It uses a set of predefined patterns (like IP addresses, email addresses, URLs, and Unix file paths) to identify and replace such information with the placeholder `[REDACTED]`. This ensures that confidential or personal data isn't inadvertently exposed or sent in its raw form.

`AI CLI Tool` is a simple command-line script to interact with OpenAI's GPT-3.5 model. You can provide prompts either directly as command-line arguments, or pipe them into the script from other sources.

## Prerequisites

- Python 3.x
- `openai` Python package
- `python-dotenv` Python package

## Setup and Installation
### Installation

Here's a quick step by step guide on how to get the development env running:

1. Clone this repository

    ```bash
    git clone https://github.com/avega-senso/aicli.git
    ```
2. Setup a virtual environment

    ```bash
    cd aicli
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the requirements

    ```bash
    pip install -r requirements.txt
    ```

4. Create an .env file for your OPEN_API_KEY

    ```bash
    # .env file
       OPENAI_API_KEY=<api key>
    ```

5. Set the alias(Optional)

    ```bash
    alias ai="$(pwd)/ai"
    ```

    If you want this alias to persist across different terminal sessions, you need to add the above commands to your shell profile or configuration file (~/.bashrc, ~/.bash_profile, ~/.zshrc, etc.), so it's executed every time you start a new terminal session.

    For instance
    ```bash
    alias ai="$(pwd)/ai" >> ~/.zshrc
    ```