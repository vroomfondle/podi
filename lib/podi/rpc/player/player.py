from types import DictType

def play_file(file_path):
  return {
      "jsonrpc": "2.0",
      "method": "Player.Open",
      "params": {
            "item": {"file": file_path}
      },
      "id": "play"
  }
