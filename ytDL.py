<<<<<<< HEAD
#pip install youtube-dl


from pytube import YouTube

# Load the YouTube video
yt = YouTube('https://www.youtube.com/watch?v=XGn5cZF-Ogk')

# Select the video resolution to download
video = yt.get('mp4', '720p')

# Save the video to disk
video.download('/path/to/save/video')
=======
#pip install youtube-dl


from pytube import YouTube

# Load the YouTube video
yt = YouTube('https://www.youtube.com/watch?v=XGn5cZF-Ogk')

# Select the video resolution to download
video = yt.get('mp4', '720p')

# Save the video to disk
video.download('/path/to/save/video')
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b
