import yt_dlp
from pathlib import Path

# Make File To Save Videos
download_folder = Path("downloads")
download_folder.mkdir(exist_ok=True)

# Request the link from the user
url = input("Enter The Url: ").strip()

# Download Stting 
options = {
    "format": "best/bestvideo+bestaudio",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "noplaylist": True,
        "js_runtimes": {
        "deno" : {
            "path": r"C:\Users\ALBRA ALHIDRY\AppData\Local\Microsoft\WinGet\Packages\DenoLand.Deno_Microsoft.Winget.Source_8wekyb3d8bbwe\deno.exe"
            }
    },

    "retries" : 10,
    "fragment_retries": 10,
    "socket_timeout": 30,
    "force_ipv4": True
}

# Donload Vid
if not url:
    print("Enter The Url")

else:
    options = {
    "format": "best/bestvideo+bestaudio",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "noplaylist": True,
        "js_runtimes": {
        "deno" : {
            "path": r"C:\Users\ALBRA ALHIDRY\AppData\Local\Microsoft\WinGet\Packages\DenoLand.Deno_Microsoft.Winget.Source_8wekyb3d8bbwe\deno.exe"
            }
    },

    "retries" : 10,
    "fragment_retries": 10,
    "socket_timeout": 30,
    "force_ipv4": True
}

try:
    with yt_dlp.YoutubeDL(options) as downloader:
        downloader.download([url])
    print("Download Complted")

except yt_dlp.utils.DownloadError as error:
    print("There Is Something Is Wrong", error)

except OSError as error:
    print("There Is Wrong With File Or Folders", error)
    