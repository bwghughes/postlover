# Upload Scanned PDF's to dropbox.
import os
import datetime
from fnmatch import fnmatch

from dropbox.client import DropboxClient
from dropbox.rest import ErrorResponse

from postlover.auth import StoredSession


def connect():
    session = StoredSession(os.environ.get('POSTLOVER_APP_KEY'),
                            os.environ.get('POSTLOVER_APP_SECRET'),
                            access_type=
                            os.environ.get('POSTLOVER_ACCESS_TYPE'))
    session.load_creds()
    client = DropboxClient(session)
    return client


def get_folder(client):
    try:
        folder_name = datetime.datetime.now().strftime('%d-%m-%Y')
        client.file_create_folder(folder_name)
    except ErrorResponse:
        print "Folder already exists."
    finally:
        return folder_name


def main():
    client = connect()
    path = os.path.abspath(os.path.join(os.curdir, 'dropboxintray'))
    folder_name = get_folder(client)
    for filename in os.listdir(path):
        print "uploading_file {} to {}".format(filename, folder_name)




if __name__ == '__main__':
    main()