import pafy
from Tkinter import Tk 

# must copy the exact link from Youtube to the clipboard
r = Tk()
r.withdraw()
result = r.clipboard_get()

url = result
video = pafy.new(url)
audiostreams = video.audiostreams
for a in audiostreams:
	print (a.bitrate, a.extension, a.get_filesize())

bestaudio = video.getbestaudio()
bestaudio.bitrate

print "Would you like to download the best audiofile?"
print "yes or no"
answer = raw_input("> ")

if 'yes' in answer:
	bestaudio.download()