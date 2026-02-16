from pytube import YouTube
import os

savePath = '/Temp/'
fileList = []
with open('linkList.txt','r'):
    fileList.append(linkList.read())

print(fileList)
#targetLink = 'https://www.youtube.com/watch?v=rCU9d5EZaAY'

#yt = YouTube(targetLink)
#yd = yt.streams.get_by_itag(22)
#print(yd.title, (round(yd.filesize/(1024*1024),2)))
#yd.download(savePath)
