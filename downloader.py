from pytube import YouTube
import os

def downloadVideo():
  link = input(str("Enter the link video then press enter : "))
  YouTube(link).streams.first().download("downloaded/single/")

def downloadVideos():
  try:
    links = []
    f = open("links.txt","r")
    for link in f:
      links.append(link.strip("\n\r"))
    if len(links) <= 0:
      print("\nThere is no links in links.txt file, insert\nvideos links into links.txt file to download them \n")
    else:
      name = input(str("Name dir : "))
      directory = "downloaded/batch/"+name+"/"
      os.mkdir(directory)
      print("\nDownloads will saved into -> " + directory + "\n")
      for l in links:
        YouTube(l).streams.first().download(directory)
        print(l + " " + "Saved to " + directory)
  except Exception as message:
    print(message)

def main():

  print("""
 __     __      _______    _                                                           
 \ \   / /     |__   __|  | |                                                          
  \ \_/ /__  _   _| |_   _| |__   ___                                                  
   \   / _ \| | | | | | | | '_ \ / _ \                                                 
    | | (_) | |_| | | |_| | |_) |  __/                                                 
  __|_|\___/ \__,_|_|\__,_|_.__/_\___|                   _                 _           
 |  _ \      | |     | |     |  __ \                    | |               | |          
 | |_) | __ _| |_ ___| |__   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 |  _ < / _` | __/ __| '_ \  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |_) | (_| | || (__| | | | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
 |____/ \__,_|\__\___|_| |_| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
  """)

  while True:
    read = input(str("(S)ingle download or (B)atch download ? "))
    if read.lower() == "s":
      downloadVideo()
    elif read.lower() == "b":
      downloadVideos()
    else:
      print("Unrecognize")

if __name__ == "__main__":
  try:
    main()
  except Exception as message:
    print(message)