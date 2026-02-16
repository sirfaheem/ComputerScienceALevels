import requests
import subprocess

# Download the video data
response = requests.get('https://www.youtube.com/watch?v=XGn5cZF-Ogk')

# Save the video data to a file
with open('/path/to/save/video.mp4', 'wb') as f:
    f.write(response.content)

# Use ffmpeg to convert the video to another format (if desired)
subprocess.run(['ffmpeg', '-i', '/path/to/save/video.mp4', '/path/to/save/video.mkv'])
