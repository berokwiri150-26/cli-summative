import json
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT, "data")


def _path(filename: str) -> str:
	return os.path.join(DATA_DIR, filename)


def read_json(filename: str):
	path = _path(filename)
	if not os.path.exists(path):
		return []
	with open(path, "r", encoding="utf-8") as f:
		try:
			return json.load(f)
		except Exception:
			return []


def write_json(filename: str, data):
	path = _path(filename)
	os.makedirs(os.path.dirname(path), exist_ok=True)
	with open(path, "w", encoding="utf-8") as f:
		json.dump(data, f, indent=4)


def next_id(items, key_name):
	if not items:
		return 1
	try:
		return max(item.get(key_name, 0) for item in items) + 1
	except Exception:
		return len(items) + 1
