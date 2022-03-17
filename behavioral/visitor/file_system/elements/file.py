from behavioral.visitor.file_system.contracts.file_system import FileSystem


class File(FileSystem):

    def __init__(self):
        self.size = None

    def size(self):
        return self.size

    def accept(self, visitor):
        visitor.visit_file(self)
