from O365 import Account, FileSystemTokenBackend
from O365 import MSGraphProtocol
import os
import json
from datetime import datetime

protocol = MSGraphProtocol(api_version='beta')
credentials = ('7b9c81d7-2c01-4d48-86fc-9a7cd9700b85', 'cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H')

token_backend = FileSystemTokenBackend(token_path='my_folder', token_filename='my_token.txt')
account = Account(credentials, protocol=protocol, token_backend=token_backend)
account.authenticate(scopes=['basic', 'message_all', 'onedrive_all', 'address_book_all'])

mailbox = account.mailbox()
inbox = mailbox.inbox_folder()


def save_mailbox_in_file(inbox):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_mailbox.json')
    data = {}
    for item in inbox.get_messages(limit=300):
        message = {
            'subject': item.subject,
            'from': str(item._Message__sender),
            'datetime': item._Message__received.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
            'attachments': item.has_attachments,
            'draft': item._Message__is_draft,
            'read': item._Message__is_read,
            'body': item._Message__body,
            'folder': item.folder_id
        }
        print(f"Le message {message['subject']} est sauvegardé avec succès !")
        data[item.object_id] = message
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


save_mailbox_in_file(inbox)


def restore_mailbox(mailbox, path_data_to_restore):
    dir_resto_name = datetime.today().strftime('Restore %A %d %B %Y %H.%M.%S.%f')
    restore_folder = mailbox.create_child_folder(dir_resto_name)
    print("Dossier {} créé avec succès...".format(dir_resto_name))
    with open(path_data_to_restore, 'r') as f:
        list_mails = json.load(f)
    for mail in list_mails:
        print(mail)


restore_mailbox(mailbox, "/home/etienne/Documents/Perso/Project1868/data_mailbox.json")
