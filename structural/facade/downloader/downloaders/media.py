from structural.facade.downloader.services.encoder import FileEncoder
from structural.facade.downloader.services.file import FileDownloader


class MediaDownloader:

    @classmethod
    def download_mp3(cls, filename, url):
        downloaded = FileDownloader.download(filename, url)
        if downloaded:
            FileEncoder.encode_to_mp3(downloaded)
        return downloaded

    @classmethod
    def download_mp4(cls, filename, url):
        downloaded = FileDownloader.download(filename, url)
        if downloaded:
            FileEncoder.encode_to_mp4(downloaded)
        return downloaded

    @classmethod
    def download_ogg(cls, filename, url):
        downloaded = FileDownloader.download(filename, url)
        if downloaded:
            FileEncoder.encode_to_ogg(downloaded)
        return downloaded

    @classmethod
    def download_webm(cls, filename, url):
        downloaded = FileDownloader.download(filename, url)
        if downloaded:
            FileEncoder.encode_to_webm(downloaded)
        return downloaded

    @classmethod
    def download_flac(cls, filename, url):
        downloaded = FileDownloader.download(filename, url)
        if downloaded:
            FileEncoder.encode_to_flac(downloaded)
        return downloaded

    @classmethod
    def download_wav(cls, filename, url):
        downloaded = FileDownloader.download(filename, url)
        if downloaded:
            FileEncoder.encode_to_wav(downloaded)
        return downloaded
