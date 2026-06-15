from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url: str):
    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/")

    query = parse_qs(parsed.query)

    return query.get("v", [None])[0]

def get_transcript(video_id: str):
    api = YouTubeTranscriptApi()

    transcript = api.fetch(video_id)

    return " ".join(
        snippet.text
        for snippet in transcript
    )