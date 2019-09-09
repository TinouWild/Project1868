from O365 import Account, FileSystemTokenBackend, MSGraphProtocol
import os
import json
from datetime import datetime

protocol = MSGraphProtocol(api_version='beta')
credentials = ('7b9c81d7-2c01-4d48-86fc-9a7cd9700b85', 'cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H')

token_backend = FileSystemTokenBackend(token_path='my_folder', token_filename='my_token.txt')
account = Account(credentials, protocol=protocol, token_backend=token_backend)
account.authenticate(scopes=['basic', 'message_all', 'onedrive_all', 'address_book_all'])

storage = account.storage()
folder_resto = storage.get_default_drive().get_root_folder()

date = datetime.today().strftime('%a %d %B %Y -- %H:%M:%S:%f')


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
