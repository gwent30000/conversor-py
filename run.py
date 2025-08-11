import yt_dlp

url = input("Digite a url do seu video: ")

opcoes = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'merge_output_format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(opcoes) as ydl:
    ydl.download([url])
    print("Download realizado com sucesso!")