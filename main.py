from time import sleep
def song_words():
    lyrics="WOAHHHH \nWE'RE HALF WAY THERE \n"
    return lyrics
def song_words2():
    lyrics="WOAHHHHHH \nPRAYER ON A CHAIR \n"
    return lyrics
thisdict = {
    "yes", "y", "Y", "YES", "Yes", "YEs", "YeS"
}
song = input("song??")
if song in thisdict:
    for char in song_words():
        sleep(0.1)
        print(char, end="", flush=True )
    for char in song_words2():
        sleep(0.15)
        print(char, end="", flush=True)
    
else:    
    print("fine no song for you")


     