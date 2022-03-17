from behavioral.command.file_manager.contracts.command import FileCommand


class RemoveFileCommand(FileCommand):

    def __init__(self, file_id, receiver):
        self.file_id = file_id
        self.receiver = receiver

    def execute(self):
        self.receiver.remove(self)
