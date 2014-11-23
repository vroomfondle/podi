def clean_video_library():
  return {
      "jsonrpc": "2.0",
      "method": "VideoLibrary.Clean", 
      "id": "clean_video_library", 
  }

def clean_audio_library():
  return {
      "jsonrpc": "2.0",
      "method": "AudioLibrary.Clean", 
      "id": "clean_audio_library", 
  }
