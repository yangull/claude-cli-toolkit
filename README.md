# claude-cli-toolkit

A command-line tool that wraps the Claude API — ask questions, summarize text, translate, and explain code directly from your terminal.

## What it does

- **ask** — ask Claude any question
- **summarize** — summarize any text in 3 bullet points
- **translate** — translate text to any language
- **explain** — explain code in simple terms

All responses stream word by word in real time.

## Setup

**1. Clone the repo**
```bash
git clone git@github.com:yangull/claude-cli-toolkit.git
cd claude-cli-toolkit
```

**2. Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install anthropic
```

**3. Set your API key**
```bash
echo 'export ANTHROPIC_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Usage

```bash
python cli_tool.py ask "What is Docker?"
python cli_tool.py summarize "Your text here"
python cli_tool.py translate "Hello world" german
python cli_tool.py explain "for i in range(10): print(i)"
```

## Tech stack

- Python 3.12
- Anthropic SDK (claude-haiku-4-5)
- Streaming responses

## Author

Can — Computer Engineering graduate, Berlin