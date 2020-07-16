# Library
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools


class H264UploaderManager:

    # Variable
    __drive = None
    __folder_ID = '''(input here Google drive folder ID)'''
    # folder ID : https://drive.google.com/drive/u/1/folders/(folder ID)


    def __init__(self):
        SCOPES = 'https://www.googleapis.com/auth/drive'
        store = file.Storage('storage.json')
        creds = store.get()

        # Verfication of authentication
        if not creds or creds.invalid:
            # credentials.json file is OAuthClientID
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
            pass

        self.__drive = discovery.build('drive', 'v3', http=creds.authorize(Http()))

        print("Certification completed")

        pass


    def UploadVideo(self, filePath, fileName):

        # Upload setting.
        file_metadata = {'name' : fileName,
                         'parents' : [self.__folder_ID]}

        # Upload file select.
        media = discovery.MediaFileUpload(filePath + fileName, mimetype = 'application/zip')

        # Upload file
        file = self.__drive.files().create(body=file_metadata, media_body=media, fields='id').execute()

        # Result
        print('Upload success!')
        print('File ID : %s' % (file.get('id')))

        pass
