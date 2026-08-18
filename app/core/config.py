from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Drug Interaction Engine"
    app_version: str = "0.1.0"
    app_env: str = "development"
    log_level: str = "INFO"

    openai_api_key: str | None = None


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()