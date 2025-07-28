import os
from datetime import datetime

def load_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def current_timestamp():
    return datetime.now().isoformat()
