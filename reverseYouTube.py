import pytube
#python-youtube 0.9.2

#https://developers.google.com/youtube/v3/code_samples/code_snippets

p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

#store the playlist in a file
for url in p.video_urls[:3]:
    print(url)

#reverse the playlist

#save it in a file

#create a playlist from file
