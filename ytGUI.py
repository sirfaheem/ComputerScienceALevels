import tkinter as tk
from tkinter import ttk
import pytube

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        # Create a label and text entry box for the video URL
        self.url_label = ttk.Label(self.root, text="Video URL:")
        self.url_entry = ttk.Entry(self.root)

        # Create a label and text entry box for the save directory
        self.dir_label = ttk.Label(self.root, text="Save to:")
        self.dir_entry = ttk.Entry(self.root)

        # Create a download button
        self.download_button = ttk.Button(self.root, text="Download", command=self.download)

        # Place the widgets in the window
        self.url_label.pack()
        self.url_entry.pack()
        self.dir_label.pack()
        self.dir_entry.pack()
        self.download_button.pack()

    def download(self):
        # Get the video URL and save directory from the GUI
        video_url = self.url_entry.get()
        save_dir = self.dir_entry.get()

        # Use pytube to download the video
        yt = pytube.YouTube(video_url)
        video = yt.get('mp4', '720p')
        video.download(save_dir)

# Create the root window
root = tk.Tk()
root.geometry('600x400+300+100') #window size and location

# Create the app and run it
app = App(root)
root.mainloop()
