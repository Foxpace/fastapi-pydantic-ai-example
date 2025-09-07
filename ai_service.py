"""AI service module using Pydantic AI with Ollama."""

import logging
from typing import Optional

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider

from config import settings

logger = logging.getLogger(__name__)


class AIService:
    def __init__(self):
        self.model = OpenAIChatModel(
            model_name=settings.ollama_model,
            provider=OllamaProvider(base_url=f"{settings.ollama_base_url}/v1"),
        )

        # Create a simple agent for text generation
        self.agent = Agent(
            model=self.model,
            instructions="You are a helpful AI assistant. Provide clear, concise, and accurate responses.",
        )

        logger.info(f"AI Service initialized with model: {settings.ollama_model}")

    async def generate_response(
        self, message: str, system_prompt: Optional[str] = None
    ) -> str:
        try:
            agent = self.agent
            if system_prompt:
                agent = Agent(model=self.model, instructions=system_prompt)

            result = await agent.run(message)
            return result.output

        except Exception as e:
            logger.error(f"Failed to generate AI response: {str(e)}")
            raise Exception(f"AI service error: {str(e)}")


ai_service = AIService()
