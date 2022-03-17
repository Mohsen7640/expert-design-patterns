from behavioral.command.file_manager.contracts.command import FileCommand


class SaveFileCommand(FileCommand):

    def __init__(self, file, receiver):
        self.file = file
        self.receiver = receiver

    def execute(self):
        self.receiver.save(self)
