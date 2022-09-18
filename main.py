from time import sleep

songchoice = False

def song_words():
    lyrics="WOAHHHH \nWE'RE HALF WAY THERE \n"
    return lyrics
def song_words2():
    lyrics="WOAHHHHHH \nPRAYER ON A CHAIR \n"
    return lyrics
yesdict = {
    "yes", "y", "Y", "YES", "Yes", "YEs", "YeS"
}
nodict = {
    "no", "n", "NO", "No", "nO"
}
qdict = {
    "q", "Q"
}
while songchoice == False:
    song = input("song??")
    if song in yesdict:
        for char in song_words():
            sleep(0.1)
            print(char, end="", flush=True )
        for char in song_words2():
            sleep(0.15)
            print(char, end="", flush=True)
            songchoice = True
    elif song in nodict:
        print("fine no song for you")
        songchoice = True
    elif song in qdict:
        print("ok monke man")
        songchoice = True
    else:
        print("yes or no (or q)")
        songchoice = False
     