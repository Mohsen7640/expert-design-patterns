from behavioral.visitor.file_system.contracts.file_system import FileSystem


class Directory(FileSystem):

    def __init__(self):
        self.files = []

    def files(self):
        return self.files

    def accept(self, visitor):
        visitor.visit_directory(self)
