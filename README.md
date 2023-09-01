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

`AI CLI Tool` is a simple command-line script to interact with OpenAI's models. You can provide prompts either directly as command-line arguments, or pipe them into the script from other sources.

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


# Usage
**Model Interaction**
With the AI CLI Tool, you can now easily interact with OpenAI's language models. You can provide an initial prompt to the tool, and it will generate responses based on the provided input.

**Model Selection**
You have the flexibility to choose the model you want to use for interactions. The default model is 'gpt-3.5-turbo', but you can specify other models using the --model command-line option.

**Temperature Control**
Fine-tune the randomness of the model's responses using the --temperature option. Higher values (e.g., 0.8) make responses more diverse, while lower values (e.g., 0.2) make them more focused and deterministic.

**Sensitive Information Redaction**
 The tool includes a --sanitize option that allows you to automatically redact sensitive information from both prompts and generated responses. You can define patterns to be redacted in the .env configuration file.

**Predefined Templates** The AI CLI Tool supports predefined prompt templates specified in the .env file. You can use templates to quickly structure your prompts, and even replace placeholders in templates with your input using the --template option.

**Max Tokens Limit** Control the length of the generated responses using the --max_tokens option. This can be particularly useful when you need concise or specific outputs.

**Usage**
Here's an example of how to use the AI CLI Tool:



## 1. Interactive Mode
**Description:** Engage in dynamic conversations with the AI model in real-time.
**Usage:** Run the tool without providing an initial message, and the AI CLI Tool will prompt you to enter messages. It will respond based on the conversation history.
**Example:**
  ```bash
% ai --system "Man pages"
AI% date
NAME
       date - print or set the system date and time

SYNOPSIS
       date [OPTION]... [+FORMAT]
...
```

### Configuration

    To configure the AI CLI Tool, you can create a .env file in the same directory as the tool's script (ai). The .env file is used to set various environment variables that control the behavior of the tool. Here's how you can configure the tool using the provided configuration:

    Create .env File:
    Create a file named .env in the same directory as the ai.py script.
    ```bash
    cp .env.example .env
    ```
    Save and Use:

    Save the .env file after adding the configurations. The AI CLI Tool script (ai.py) will automatically load these configurations from the .env file when it is run.
    Configuration parameters can be overridden using the cli options, see help for details:

    ```bash
    ai --help
    ```

    Make sure the .env file is in the same directory as the script, and you can run the tool using the various options and configurations as described earlier.

## 2. Direct Message Input
**Description:** Easily provide an input message directly as a command-line argument to the script.
**Usage:** Pass the input message as an argument to the tool script, and the AI CLI Tool will generate a response based on the provided message.
**Example:**
  ```bash
% ai "Translate the following English text to French: 'Hello, how are you?'" --template doc --system html
```
## 3. Piping Input from another command
**Description:** Use the output of one command as input for the AI CLI Tool.
**Usage:** Pipe the output of the echo command into the tool script. The AI CLI Tool will process the input and generate a response.
**Example:**
  ```bash
% echo "Explain the concept of machine learning" | ai template doc --system md 
```
## 4. Piping Standard Error
**Description:** Process error messages from another command and generate responses using the AI CLI Tool.
**Usage:** Redirect the output (both stdout and stderr) from another command to the standard input of the tool script. The AI CLI Tool will generate responses based on the command's output.
**Example:**
  ```bash
% node bug.js 2>&1 | ai --system "javascript troubleshooting" --template ERROR
```
