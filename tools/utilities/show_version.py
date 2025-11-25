#!/usr/bin/env python3
"""Print the NOVA version from NOVA_prompts.VERSION (if present)."""
import importlib, sys
from pathlib import Path
repo_root = Path(__file__).resolve().parents[2]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

try:
    mod = importlib.import_module('NOVA_prompts')
    version = getattr(mod, 'VERSION', None)
    if version is None:
        print('VERSION not defined in NOVA_prompts.py')
    else:
        print(f'NOVA VERSION: {version}')
except Exception as e:
    print(f'Failed to read VERSION: {e}')
