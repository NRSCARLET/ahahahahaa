from time import sleep
def song_words():
def song_words2():
thisdict = {
    "yes", "y", "Y", "YES", "Yes", "YEs", "YeS"
}
song = input("song??")
if song == thisdict:

else:
     print("fine no song for you")
     
for char in song_words:
    sleep(0.1)
    print(char, end="", flush=True )
for char in song_words2:
    sleep(0.15)
    print(char, end="", flush=True)
song_words(): "WOAHHHH \nWE'RE HALF WAY THERE \n"
song_words2(): "WOAHHHHHH \nPRAYER ON A CHAIR \n"