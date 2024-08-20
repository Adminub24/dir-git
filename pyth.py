#!/usr/bin/env python3

import os

def get_size(path):
    size = 0
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        for dirpath, dirname, filenames in os.walk(path):
            for filename in filenames:
                fp = os.path.join(dirpath, filename)
                if os.path.isfile(fp):
                    size =+ os.path.getsize(fp)      

    return size

def human_readable_size(size):
    for unit in ['B','KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            break
        size /= 1024
    return "{:.2f} {}".format(size, unit)

path = '.'
rez = sorted(os.listdir(path))
size_list = []

for n, item in enumerate(rez):
    full_path = os.path.join(path, item)
    size = get_size(full_path)
    size_list.append((size, item))
    #print("{} {} {}".format(n+1, size, item,))
    
    size_list.sort(key=lambda x: x[0], reverse=True)
    for size, item in size_list:
        print("{} {}".format(human_readable_size(size), item,))
        
