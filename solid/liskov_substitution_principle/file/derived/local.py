from solid.liskov_substitution_principle.file.contracts.file_interface import FileInterface


class LocalFile(FileInterface):

    def rename(self):
        pass

    def move(self):
        pass

    def copy(self):
        pass
