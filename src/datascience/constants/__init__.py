from pathlib import Path
import os

# Determine if we're running from research directory or project root
current_dir = Path.cwd()
if current_dir.name == "research":
    # Running from research directory, go up one level
    base_path = current_dir.parent
else:
    # Running from project root
    base_path = current_dir

CONFIG_FILE_PATH = base_path / "config" / "config.yaml"
PARAMS_FILE_PATH = base_path / "params.yaml"
SCHEMA_FILE_PATH = base_path / "schema.yaml"