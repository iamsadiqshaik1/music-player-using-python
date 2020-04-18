from pygame import mixer

mixer.init()

mixer.music.load()
mixer.music.set_volume(1)
mixer.music.play()
while 1:
    print("press 'p' to pause\npress 'r' to resume")
    print("press 'X' to exit")
    r = input(">>>")
    if r == 'p':
        mixer.music.pause()
    elif r=='r':
        mixer.music.unpause()
    elif r=='e':
        mixer.music.stop()
        break
