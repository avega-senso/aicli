# aicli: Interact with GPT-3

`aicli` is a simple command-line script to interact with OpenAI's GPT-3. You can provide prompts either directly as command-line arguments, or pipe them into the script from other sources.

## Prerequisites

- Python 3.x
- `openai` Python package
- `python-dotenv` Python package

## Setup and Installation
### Installation

Here's a quick step by step guide on how to get the development env running:

1. Clone this repository:

    ```bash
    git clone https://github.com/avega-senso/aicli.git
    ```
2. Setup a virtual environment

    ```bash
    cd aicli
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the requirements:

    ```bash
    cd aicli
    pip install -r requirements.txt
    ```

4. Create an .env file for your cliend_id and client_secret: 

    ```bash
    # .env file
       OPENAI_API_KEY=<api key>
    ```

5. Set the alias:

    ```bash
    alias ai="$(pwd)/aicli.py"
    ```

    If you want this alias to persist across different terminal sessions, you need to add the above commands to your shell profile or configuration file (~/.bashrc, ~/.bash_profile, ~/.zshrc, etc.), so it's executed every time you start a new terminal session.

    For instance:   
    ```bash
    alias ai="$(pwd)/aicli.py" >> ~/.zshrc
    ```