'''
	Teaching LittleChris to download mp3 file from a youtube page
	Credits goes to http://willdrevo.com/
'''

import youtube_dl
import pandas as pd
import os
import traceback

def printURLInfo(url):
	if not url:
		print "Please provide me a real URL"
		return
	else:
		# download metadata
		ydl = youtube_dl.YoutubeDL()
		r = None
		with ydl:
		    r = ydl.extract_info(url, download=False)  # don't download, much faster
		# print some typical fields
	print "%s was uploaded by '%s' and has %d views, %d likes, and %d dislikes" % (r['title'], r['uploader'], r['view_count'], r['like_count'], r['dislike_count'])
	command  = raw_input("> Do you want me to download it?")
	if command[0] is 'y' or command[0] is 'Y':
		download(url)

def saveTo(title, savedir):
	return os.path.join(savedir, "%s.mp3" % title)

def download(url):
	foldername = "Mp3FromYoutube"

	if not os.path.exists(foldername):
		os.makedirs(foldername)
	# making a youtube downloader
	options = {
		'format': 'bestaudio/best',
		'extractaudio' : True,
		'audioformat' : "mp3",
		'outtmpl': '%(id)s',
		'noplaylist': True,
	}

	ydl = youtube_dl.YoutubeDL(options)
	r = ydl.extract_info(url, download=False)
	tit = r['title']
	# download location, check for progress
	savepath = saveTo(tit,foldername)

	result = ydl.extract_info(url, download=True)
	os.rename(result['id'], savepath)
	print "Downloaded and converted %s successfully!" % savepath



