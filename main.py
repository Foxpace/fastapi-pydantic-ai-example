import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from ai_service import ai_service
from config import settings
from models import AIRequest, AIResponse

logging.basicConfig(level=settings.log_level.upper())
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting FastAPI application with Pydantic AI")
    logger.info(f"Using Ollama at: {settings.ollama_base_url}")
    logger.info(f"Using model: {settings.ollama_model}")
    yield
    logger.info("Shutting down FastAPI application")


app = FastAPI(
    title="FastAPI Pydantic AI Example",
    description="A simple FastAPI application with Pydantic AI integration",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "message": "FastAPI Pydantic AI Example",
        "version": "0.1.0",
        "docs": "/docs",
    }


@app.post("/ai", response_model=AIResponse)
async def ai_response(request: AIRequest):
    try:
        response = await ai_service.generate_response(
            message=request.message, system_prompt=request.instructions
        )

        return AIResponse(response=response, model=settings.ollama_model)
    except Exception as e:
        logger.error(f"AI request failed: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to generate AI response: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.api_reload,
        log_level=settings.log_level,
    )
