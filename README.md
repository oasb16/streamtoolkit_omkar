# streamtoolkit_omkar

Shared toolkit for GPT-enabled apps (LandTena, Hyperpersonalizer, etc.)

## Structure

- `auth/` — Cognito JWT handling
- `config/` — Secure .env and Streamlit secret loader
- `streamlit_components/` — Streamlit UI pieces like token input
- `utils/` — GPT + DynamoDB helpers

## Usage

```python
from streamtoolkit_omkar import get_current_user, token_input_box, probe_and_summarize
```
