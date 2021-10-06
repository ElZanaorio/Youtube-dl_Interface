import tkinter
from moviepy.audio.io.AudioFileClip import AudioFileClip
from shutil import move
from glob import glob
from os import getlogin, system, remove
from pathlib import Path

# Link a la pagina con todos los formatos
# https://gist.github.com/sidneys/7095afe4da4ae58694d128b1034e01e2

usuario = getlogin()
path = Path().absolute()

def descargar_mp3(url):
    system(f"start /min cmd /C cd {path} && youtube-dl -f 140 {url}")
    mp3()

def descargar_mp4(url):
    system(f"start /min cmd /C cd {path} && youtube-dl -f 37 {url}")
    mp4()

def mp3():
    m4a = []
    def renombrar_mp3(url):
        url = url[::-1]
        url = url[16:]
        url = url[::-1]
        return (f'{url}.mp3')

    for a in glob('.\*.m4a'):
        m4a.append(str(path)+a[1:])

    for a in m4a:
        audioClip = AudioFileClip(a)
        convertedFile = renombrar_mp3(a)
        audioClip.write_audiofile(convertedFile)
        audioClip.close()
        move(renombrar_mp3(a), f'C:/Users/{usuario}/Desktop')
        remove(a)


def mp4():
    mp4_list = []
    def renombrar_mp4(url):
        url = url[::-1]
        url = url[16:]
        url = url[::-1]
        return (f'{url}.mp4')

    for a in glob('.\*.mp4'):
        mp4.append(a)

    for a in mp4_list:
        move(renombrar_mp4(a), f'C:/Users/{usuario}/Desktop')
        remove(a)



ventana = tkinter.Tk()
ventana.geometry("300x200")

texto_youtube_dl = tkinter.Label(ventana, text="YOUTUBE-DL", fg="black")
texto_youtube_dl.pack(side = tkinter.TOP)


caja_url = tkinter.Entry(ventana)
caja_url.pack(side = "top")

boton_descargar = tkinter.Button(ventana, text="Descargar MP3", padx = 40, pady = 15, command = lambda: descargar_mp3(caja_url.get()))
boton_descargar.pack(side = "bottom")

boton_descargar = tkinter.Button(ventana, text="Descargar MP4", padx = 40, pady = 15, command = lambda: descargar_mp4(caja_url.get()))
boton_descargar.pack(side = "bottom")

ventana.mainloop()