# FastAPI Pydantic AI Example

Full article here: <http://tomasrepcik.dev/blog/2025/2025-09-07-pydantic-ai-intro/>

A simple FastAPI application demonstrating integration with Pydantic AI using Ollama for local AI model inference.

## Prerequisites

1. **Python 3.13+**: This project requires Python 3.13 or later
2. **Ollama**: Install and run Ollama locally

   ```bash
   # Install Ollama (macOS) or go to https://ollama.com for other OS
   brew install ollama
   
   # Start Ollama service
   ollama serve
   
   # Pull the gemma3:270m model (or any other model you prefer)
   ollama pull gemma3:270m
   ```

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd fastapi-pydantic-ai-example
   ```

2. **Install dependencies**:

   ```bash
   uv sync
   ```

3. **Configure environment**:

   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env to match your setup
   # The default configuration should work if Ollama is running locally
   ```

## Configuration

The application can be configured via environment variables:

```bash
OLLAMA_BASE_URL=http://localhost:11434  # Ollama server URL
OLLAMA_MODEL=gemma3:270m                # Model name to use

API_HOST=0.0.0.0                        # Server host
API_PORT=8000                           # Server port
API_RELOAD=true                         # Enable auto-reload (development)

LOG_LEVEL=info                          # Logging level
```

## Usage

### Start the Server

```bash
python main.py

# Or
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Test the Implementation

Run the test script to verify everything works:

```bash
python test_implementation.py
```

### API Endpoints

Once the server is running, you can access:

- **Interactive Docs**: <http://localhost:8000/docs>
- **Chat Endpoint**: <http://localhost:8000/ai>
