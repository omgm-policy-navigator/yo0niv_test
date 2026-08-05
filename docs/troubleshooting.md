# Troubleshooting

## Virtual Environment

If `uvicorn` or `pytest` is not found, activate the local virtual environment and install dependencies:

```bash
source .venv/bin/activate
pip install ".[dev]"
```

## Python Version

This project targets Python 3.9 or newer. Check your active interpreter:

```bash
python --version
```

## Environment Variables

Create a local `.env` from the example when running the app locally:

```bash
cp .env.example .env
```

Do not commit `.env` files.
