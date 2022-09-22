from pytube import YouTube

url_video=input("Digite a Url do Video do Youtube: ")

youtube = YouTube(url_video)

youtube.streams.get_highest_resolution().download()