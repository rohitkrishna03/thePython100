# write a program to clear the clutter inseide a folder on your computer.
# you should use os module to rename all the png iomages from 1.png all the same for other file formates.
# FOR EXAMPLE:

# sadas.png -> 1.png
# aaefa.png -> 2.png
# rvwvve.png ->3.png
# ybkoh.png -> 4.png
# here create a folder named clutter folder and kee all the .png images in it 

import os

files = os.listdir("clutterfolder")
i =1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutterfolder/{file}", f"clutterfolder/{i}.png")
        i=i+1