from behavioral.visitor.file_system.contracts.visitor import Visitor


class SizeVisitor(Visitor):

    def visit_file(self, file):
        return self.size

    def visit_directory(self, directory):
        total_size = 0

        for file in directory.files():
            total_size += self.visit_file(file)

        return total_size

