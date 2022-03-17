from behavioral.command.file_manager.contracts.command import FileCommand


class DownloadFileCommand(FileCommand):

    def __init__(self, file, receiver):
        self.file = file
        self.receiver = receiver

    def execute(self):
        self.receiver.download(self)
