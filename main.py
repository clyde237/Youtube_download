from pytube import YouTube

#fonction de telechargement
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    try:
        youtubeObject.download()
        print("telechargement en cours...")
    except:
        print("Nous avons rencontré un probleme lors du telechargement")
    print("Ce telechargement est terminé!!")

link = input("Mettez votre lien youtube ici!! URL:")
Download(link)