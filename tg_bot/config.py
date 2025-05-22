import yaml
from pathlib import Path

# Path to the config directory
config_dir = Path(__file__).parent.parent / "config"

# Load config.yml
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# Extract values from YAML
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]

# Optional: print to confirm (you can remove this)
# print("Loaded config:", telegram_token, openai_api_key)