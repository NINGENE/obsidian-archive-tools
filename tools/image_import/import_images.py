import yaml
from pathlib import Path

def load_config(config_path: str) -> dict:
    with open(config_path) as file:
        return yaml.safe_load(file)

config = load_config("config.yaml")

def build_paths(config):
    vault = Path(config['vault_dir'])
    inbox = vault / config['inbox_dir']
    processed = vault / config['processed_dir']
    failed = vault / config['failed_dir']
    originals = vault / config['originals_dir']
    thumbnails = vault / config['thumbnails_dir']
    notes = vault / config['notes_dir']
    logs = vault / config['logs_dir']

    return {
        "inbox": inbox,
        "processed": processed,
        "failed": failed,
        "originals": originals,
        "thumbnails": thumbnails,
        "notes": notes,
        "logs": logs,
    }

#config = load_config("config.yaml")
paths = build_paths(config)
print(paths['inbox'])
print(paths['thumbnails'])