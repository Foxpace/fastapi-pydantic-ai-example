from pydantic import BaseModel, Field
from typing import Optional


class AIRequest(BaseModel):
    message: str = Field(
        ..., description="The user message to send to the AI", min_length=1
    )
    instructions: Optional[str] = Field(
        default=None, description="Optional instructions to guide the AI's behavior"
    )


class AIResponse(BaseModel):
    response: str = Field(..., description="The AI's response")
    model: str = Field(..., description="The model used to generate the response")
