import os
def youtube_downloader(enter_youtube_link,youtube_quality,quality_number):
    youtube_id = enter_youtube_link.split("/")
    if youtube_quality=="Auto":
            dummy="yt-dlp --format mp4 https://www.youtube.com/watch?v="+youtube_id[-1]
            try:
              os.system(dummy)
              print("Download successful")
            except:
              print("Can't download")
    elif youtube_quality=="Manual":
      dummy=f"yt-dlp  https://youtu.be/{youtube_id[-1]} -f {quality_number}+bestaudio"
      try:
        var9=os.system(dummy)
        print(var9)
      except:
        print("Can't download")
