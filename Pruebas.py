import pafy
#Articulo
#https://www.elarraydejota.com/probando-pydub-para-convertir-y-reproducir-audio/
#https://pythonhosted.org/pafy/
#https://audiosegment.readthedocs.io/en/latest/audiosegment.html
#https://github.com/jiaaro/pydub/blob/master/API.markdown


def datosVideo(video):    
    print(video.title)
    #print(video.rating)
    #print(video.viewcount)
    print(video.author)
    print(video.duration)
    #print(video.likes)
    #print(video.dislikes)
    #print(video.description)
    print(video.audiostreams)

def descargarAudio(video):
    print(f"descargando {video.title}")
    bestaudio = video.getbestaudio(preftype="m4a")
    #bestaudio = video.getbestaudio(preftype="mp3")
    bestaudio.download()
    #bestaudio.download(filepath="C:/Users/DELL/Desktop/DescargarVideosPython/Canciones" + bestaudio.extension)

def metodo():
    print("probando el commit")



video = pafy.new("https://www.youtube.com/watch?v=qkt0W1lQwy4")
datosVideo(video)
#descargarAudio(video)





