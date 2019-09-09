import os
import json

d = '/home/etienne/Documents/Perso/Project1868/Default Drive'
path = '/home/etienne/Documents/Perso/Project1868/tree_files.json'


def list_files(startpath):
    liste_files = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        liste_files.append('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(sub_indent, f))
            liste_files.append('{}{}'.format(sub_indent, f))
    with open(path, 'w') as f:
        json.dump(liste_files, f, indent=2)


list_files(d)
