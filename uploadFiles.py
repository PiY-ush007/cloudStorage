import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb')as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.Alyi3DmIBCYFMGOAVTtBgJvl083lxlKh4XBau36dpcwvuMG_sQJU9B-XjHG9LdxE2yDDHD-jbjXYmlx9jkGVfKhD8Frl8NvJ6dgSAdoVj7R6cBEGNi47Krpnk98IvTFKOkzwQ_w'
    transferData = TransferData(access_token)

    file_from = input('enter the file to transfer')
    file_to = input('enter the file to upload')

    transferData.upload_file(file_from, file_to)
    print('transfer successfull!')


if __name__ == '__main__':
    main()
