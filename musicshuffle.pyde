from random import *

def setup():
    
    songs = [
       "My Song",
       "Bekfast",
       "Cholla",
       "Lust",
       "In the Air",
       "Icon",
       "Fireflies",
       "Broken Clocks",
       "SUPER Model",
       ]
    
    
    def play(track):
        print(track)  
    
    for i in range(8):
      trackNumber = randint (0, len(songs) - 1) 
      play (songs[trackNumber])
      
lst = [8,19,21]
print(lst[0] + 3)
print(lst)
