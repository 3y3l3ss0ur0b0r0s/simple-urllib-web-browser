import urllib.request, urllib.parse, urllib.error
import re

done = False

while done is False:
    url = input("What page do you want to see? Give me a link: ")

    while re.search("^https*://www\..*[a-z*]$", url) is None:
        url = input("Try again--that doesn't look like a valid link: ")
        
    print("Thanks! I'll try this link.")

    fileHandle = urllib.request.urlopen(url)
    for line in fileHandle:
        print(line.decode().strip())
        
    userInput = input("That was...something. We can look at another page! Just enter anything (or nothing) if you want to do another. Otherwise, if you're done, enter 0.")
    
    if userInput == '0':
        print("See you next time!")
        done = True