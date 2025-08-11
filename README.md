# 🐍 conversor-py 

Projeto simples em Python para conversão de vídeos usando FFmpeg.

---

### 🎥 Como funciona 

1. 📹 import yt_dlp

- 📝 Essa é a biblioteca que faz o download de vídeos

2. 🎞️ url = input("Digite a url do seu video: ")

- 📝 Aqui o programa pede pra você digitar o link do vídeo que quer baixar.

3. 🎞️ opcoes = { ... }

- 📝 Esse é um dicionário do modulo com funções de configuração para o downloader:

    🎞️ 'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'

- 📝 Pede pra baixar o melhor vídeo no formato mp4 junto com o melhor áudio em m4a.Também junta os dois,e se der erro ele baixa o mp4 direto.

    🎞️ 'merge_output_format': 'mp4'

- 📝 Define o formato de video que é o mp4

    🎬 'outtmpl': '%(title)s.%(ext)s'

- 📁 Define o nome do arquivo salvo exatamente como o titulo original do video

## 🛎️ Aviso

Estou preparando um tutorial detalhado com imagens e explicando passo a passo como adicionar o FFmpeg ao PATH do windows para que o programa funcione(é necessario ter ele adicionado ao path)

Em breve estará disponível aqui! :D