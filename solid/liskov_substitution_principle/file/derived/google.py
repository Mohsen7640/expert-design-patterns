from solid.liskov_substitution_principle.file.contracts.downloadable_file_interface import \
    DownloadableFileInterface


class GoogleDriveFile(DownloadableFileInterface):

    def rename(self):
        pass

    def move(self):
        pass

    def copy(self):
        pass

    def download(self) -> bool:
        pass