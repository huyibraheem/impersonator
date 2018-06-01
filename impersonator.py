import random 
import time 
import sys 
import googlesearch 
#from youtube import youtube 
#from stackexchange import stackexchange

print("impersonator.py - nsa cant into ur box")
if len(sys.argv) == 1: 
    print("error: must supply arguments")
elif sys.argv[1] == "-h": 
    print("-y   browse youtube\n-g   browse google\n-s   browse stackexchange\n-r   switch modes randomly\n")
elif sys.argv[1] == "-y": 
    pass
    #youtube() 
elif sys.argv[1] == "-g": 
    googlesearch.googlesearch()
elif sys.argv[1] == "-s": 
    pass
    #stackexchange()
elif sys.argv[2] == "-r": 
    pass 
