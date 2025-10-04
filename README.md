# Local Setup Guide

## Quick Start

### 1. Install uv

Follow the installation guide: <https://docs.astral.sh/uv/getting-started/installation/>

### 2. Install Dependencies

```bash
uv sync
```

### 3. Run the Application

```bash
uv run uvicorn src.main:app --reload
```

### 4. Access the Application

- **Application**: <http://localhost:3000/api>
- **API Documentation**: <http://localhost:3000/api/docs>

## What Each Command Does

- `uv sync` - Installs all project dependencies
- `uv run python src/main.py` - Starts the development server with auto-reload

## Stop the Server

Press `Ctrl + C` in the terminal

## Environment Variables

Create a `.env` file in the project root with the following variables:

```properties
PROJECT_NAME=CCE Rain Prediction API
DESCRIPTION=API to check if it will rain at a specific location and time
VERSION=1.0.0
DEBUG=True

HOST=localhost
PORT=3000
```

## Additional Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
  