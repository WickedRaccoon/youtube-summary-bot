from pytubefix import YouTube

def get_video_title(url: str):
    yt = YouTube(url)
    return yt.title