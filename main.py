import json
from gui.main_screen import ventana
from pathlib import Path

if __name__ == "__main__":
    Path("dataset/cut").mkdir(parents=True, exist_ok=True)
    Path("dataset/full").mkdir(parents=True, exist_ok=True)
    with open("settings/settings.json", "r", encoding='utf-8') as config_file:
        config = json.load(config_file)

    print(config)
    ventana()