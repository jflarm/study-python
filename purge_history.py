#!/usr/bin/env python3.7
"""
This script will remove entries from recent history of
Gnome3 File Browser using entries in a specified file: 
/home/user/.local/share/files2remove.txt in my case.
"""
from xml.dom import minidom
import re

def bkup (file):
    """
    This function creates a backup of a file and adds
    the date to the backup file name.
    """
    import shutil
    import datetime
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    newfile = f"{file}.bk_{now}"
    shutil.copyfile(file, newfile)
    return None
    
def to_remove(*files):
    """
    This function creates regular expressions to be used.
    """
    filelist = []
    for file in files:
        file = str(file).replace("/","\/")
        filelist.append(f'file://{str(file)}')
    return filelist

def inputfile(file):
    """
    This function creates the list of entries that will be
    removed.
    """
    feed = []
    with open(file,"r") as file:
        for line in file.readlines():
            feed.append(line.strip('\n'))
    return feed


bkup('/home/francis/.local/share/recently-used.xbel')

files2remove = inputfile("/home/francis/.local/share/files2remove.txt")
document = minidom.parse('/home/francis/.local/share/recently-used.xbel', False)
nodes = document.getElementsByTagName('bookmark')
black_list = []

# print(files2remove)
for node in nodes:
    attr = node.getAttribute('href')
    for item in files2remove:
        if re.search(item, attr):
            black_list.append(attr)
        else:
            continue


print(black_list)

for node in nodes:
    parent = node.parentNode
    attr = node.getAttribute('href')
    if attr in black_list:
        parent.removeChild(node)


with open("/home/francis/.local/share/recently-used.xbel","+w") as file:
    file.write(document.toxml())

exit()
