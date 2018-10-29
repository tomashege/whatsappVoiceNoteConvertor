import sys, os, time
from pydub import AudioSegment
path = "/Users/tomashegewisch/Downloads/"
og = os.listdir(path)
print("Running")
def diff(list1, list2): 
      return [x for x in (set(list1).union(set(list2))-set(list1).intersection(set(list2))) if x not in set(list1)]

while True:
      ogg_version = AudioSegment.from_ogg("/Users/tomashegewisch/Downloads/WhatsApp Ptt 2018-10-28 at 23.45.29.ogg")
      ogg_version.export("Users/tomashegewisch/Downloads/WhatsApp.mp3", format="mp3")
      input("yu")

while True:
      time.sleep(5)
      ng = os.listdir(path)
      if ng!=og:
            newFile = diff(og,ng)
            if newFile != []:
                  if "ogg" == newFile[0][-3:]:
                        print("new voice note", newFile[0], "ready for conversion")
            og=ng
