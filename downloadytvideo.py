from pytube import YouTube
link = 'https://www.youtube.com/watch?v=hoNb6HuNmU0'
video=YouTube(link)
stream = video.streams.get_highest_resolutions()
stream.download()