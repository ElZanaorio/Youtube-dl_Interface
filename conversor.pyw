from moviepy.editor import AudioFileClip
from shutil import move
from glob import glob
from os import getlogin, remove


usuario = getlogin()

def mp3():
    m4a = []
    def renombrar_mp3(url):
        url = url[::-1]
        url = url[16:]
        url = url[::-1]
        return (f'./{url}.mp3')

    for a in glob('./*.m4a'):
        m4a.append(a)

    for a in m4a:
        audioClip = AudioFileClip(a)
        convertedFile = renombrar_mp3(a)
        audioClip.write_audiofile(convertedFile)
        audioClip.close()

        move(renombrar_mp3(a), f'C:/Users/{usuario}/Desktop')
        remove(a)


def mp4():
    mkv = []
    def renombrar_mp4(url):
        url = url[::-1]
        url = url[16:]
        url = url[::-1]
        return (f'./{url}.mp4')

    for a in glob('./*.mkv'):
        mkv.append(a)

        # Aqui iria lo de convertir a MP4

        move(renombrar_mp4(a), f'C:/Users/{usuario}/Desktop')
        remove(a)

mp3()