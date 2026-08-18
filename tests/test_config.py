from app.core.config import settings

def test_settings() -> None:
    assert settings.app_name == "Drug Interaction Engine"
    assert settings.app_version == "0.1.0"
    assert settings.app_env == "development"
    assert settings.log_level == "INFO"
    assert settings.openai_api_key is None