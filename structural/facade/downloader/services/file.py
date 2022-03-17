class FileDownloader:

    @classmethod
    def download(cls, filename, url):
        print('Downloading file: {}'.format(filename))
        print('From URL: {}'.format(url))
        print('...')
        return True