from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ollama_base_url: str = Field(
        default="http://localhost:11434", description="Ollama API base URL"
    )
    ollama_model: str = Field(default="gemma3:270m", description="Ollama model to use")

    # API Configuration
    api_host: str = Field(default="0.0.0.0", description="API host")
    api_port: int = Field(default=8000, description="API port")
    api_reload: bool = Field(
        default=True, description="Enable auto-reload in development"
    )

    # Logging
    log_level: str = Field(default="info", description="Logging level")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
