
# StreamToolkit Omkar

A reusable developer toolkit for Streamlit apps, with plug-and-play AWS Cognito, Google OAuth, GPT-ready integration, config management, and UI components.

## Features
- 🔐 Auth: AWS Cognito & Google OAuth
- 🤖 GPT integration ready (just plug your key)
- 🧩 Reusable UI components like chat box
- 📦 One config loader for all secrets

## Install

```bash
pip install git+https://github.com/oasb16/streamtoolkit_omkar.git
```

## Usage

```python
from streamtoolkit_omkar.auth.aws_cognito import create_user_pool
from streamtoolkit_omkar.config.secrets_loader import load_secrets
```

MIT License
