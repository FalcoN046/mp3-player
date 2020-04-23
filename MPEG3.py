from pygame import mixer

mixer.init()
mixer.music.load('E:\MUSIC\pirates.mp3')
mixer.music.set_volume(0.9)
mixer.music.play()

while True:
    print('press p  to pause  r to resume')
    print('e to exit ')
    query = input(">>>")
    
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break
