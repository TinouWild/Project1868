from O365 import Account, FileSystemTokenBackend, MSGraphProtocol
import os
from datetime import datetime

protocol = MSGraphProtocol(api_version='beta')
credentials = ('7b9c81d7-2c01-4d48-86fc-9a7cd9700b85', 'cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H')

token_backend = FileSystemTokenBackend(token_path='my_folder', token_filename='my_token.txt')
account = Account(credentials, protocol=protocol, token_backend=token_backend)
account.authenticate(scopes=['basic', 'message_all', 'onedrive_all', 'address_book_all'])

storage = account.storage()
drive = storage.get_default_drive().get_root_folder()

dir_resto_name = datetime.today().strftime('Restore %A %d %B %Y %H.%M.%S.%f')
folder_resto = drive.create_child_folder(dir_resto_name)


def upload_directory(startpath):
    for root, dirs, files in os.walk(startpath):
        if dirs.__len__() > 0:
            current_drive = folder_resto.create_child_folder(os.path.basename(root))
            print("DIR - {} is uploading...".format(os.path.basename(root)))
            for f in files:
                current_drive.upload_file(root + '/' + f)
                print("FILE - {} is uploading...".format(f))


upload_directory("/home/etienne/Documents/Perso/Project1868/Default Drive")
