from O365 import Account
from O365 import MSGraphProtocol
from O365 import FileSystemTokenBackend
import os

path = os.path.dirname(os.path.abspath(__file__))


def save_folder(folder, custom_path=None):
    current_path = custom_path if custom_path else os.path.join(path, folder.name)
    for item in folder.get_items():
        if item.is_folder and item.child_count > 0:
            new_folder = create_folder(item, current_path)
            save_folder(item, new_folder)
        if item.is_file:
            download_file(item, current_path)


def create_folder(item, current_path):
    folder = os.path.join(current_path, item.name)
    os.makedirs(folder, exist_ok=1)
    print(f"Dossier {item.name} créé avec succès !")
    return folder


def download_file(item, path):
    item.download(to_path=path, chunk_size=None)
    print(f"Fichier {item.name} téléchargé avec succès !")


protocol = MSGraphProtocol(api_version='beta')
credentials = ('7b9c81d7-2c01-4d48-86fc-9a7cd9700b85', 'cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H')

token_backend = FileSystemTokenBackend(token_path='my_folder', token_filename='my_token.txt')
account = Account(credentials, protocol=protocol, token_backend=token_backend)
account.authenticate(scopes=['basic', 'message_all', 'onedrive_all', 'address_book_all'])

storage = account.storage()
my_drive = storage.get_default_drive()

save_folder(my_drive)
