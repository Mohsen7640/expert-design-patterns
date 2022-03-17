from abc import abstractmethod

from behavioral.command.task.contracts.command import Command


class UndoableCommand(Command):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undoable(self):
        pass
