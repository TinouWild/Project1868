from O365 import Account, FileSystemTokenBackend, MSGraphProtocol
import sys
import os
import json

protocol = MSGraphProtocol(api_version='beta')
credentials = ('7b9c81d7-2c01-4d48-86fc-9a7cd9700b85', 'cBPj06Vjh_[HNkntI-e6pEf.h1JKn12H')

token_backend = FileSystemTokenBackend(token_path='my_folder', token_filename='my_token.txt')
account = Account(credentials, protocol=protocol, token_backend=token_backend)
account.authenticate(scopes=['basic', 'message_all', 'onedrive_all', 'address_book_all'])

address_book = account.address_book()
contacts = address_book.get_contacts(limit=None)

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all_my_contacts.json')
data = {}
for item in contacts:
    contact = {
        'name': item._Contact__display_name,
        'created_at': item._Contact__created.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
    }
    print(f"Contact {item._Contact__display_name} save...")
    data[item.object_id] = contact

with open(path, "w") as f:
    json.dump(data, f, indent=4)
