import tkinter as tk
from tkinter import filedialog
import pytube

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        # Create a label and text entry box for the video URL
        self.url_label = tk.Label(self.root, text="Video URL:")

        self.url_entry = tk.Entry(self.root)


        # Create a label and a button for the save directory
        self.dir_label = tk.Label(self.root, text="Save to:")
        self.dir_button = tk.Button(self.root, text="choose a folder to save", command=self.browse)

        # Create a download button
        self.download_button = tk.Button(self.root, text="Download", command=self.download)

        # Place the widgets in the window
        self.url_label.pack()
        self.url_entry.config(width=60)
        self.url_entry.pack()
        self.dir_label.pack()
        self.dir_button.pack()
        self.download_button.pack()

    def browse(self):
        save_dir = filedialog.askdirectory()
        self.dir_label.config(text=save_dir)

    def download(self):
        # Get the video URL and save directory from the GUI
        video_url = self.url_entry.get()
        save_dir = self.dir_label.cget("text")

        # Use pytube to download the video
        yt = pytube.YouTube(video_url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        #video = yt.get('mp4', '720p')
        video.download(save_dir)




# Create the root window
root = tk.Tk()
root.geometry('600x400+300+100') #window size and location

# Create the app and run it
app = App(root)
root.mainloop()
