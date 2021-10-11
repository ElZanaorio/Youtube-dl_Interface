import tkinter
from moviepy.audio.io.AudioFileClip import AudioFileClip
from shutil import move
from glob import glob
from os import getlogin, system, remove
from pathlib import Path

usuario = getlogin()
path = Path().absolute()

def descargar_mp3(url):
    system(f"start /min cmd /C cd {path} && youtube-dl -f 140 {url}")
    mp3()

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

ventana = tkinter.Tk()
ventana.iconbitmap("favicon.ico")
ventana.title("Downloader")
ventana.geometry("540x170")

borde_boton = tkinter.Frame(ventana,
                            highlightbackground="#37d3ff",
                            highlightthickness=3, bd=0)

texto_youtube_dl = tkinter.Label(ventana,
                                 pady = 5,
                                 text = " ")

texto_youtube_dl.pack(side = 'top')

caja_url = tkinter.Entry(ventana, font = "Helvetica 18", width = 40)
caja_url.pack(side = "top")

blanco = tkinter.Label(ventana, pady = 2)
blanco.pack(side = "bottom")


boton_descargar_sonido = tkinter.Button(borde_boton,
                                        text="Descargar",
                                        padx = 15,
                                        pady = 12,
                                        font = "Georgia 12" ,
                                        command = lambda: descargar_mp3(caja_url.get()))

boton_descargar_sonido.pack(side = "bottom")

borde_boton.pack(side = "bottom")

ventana.mainloop()