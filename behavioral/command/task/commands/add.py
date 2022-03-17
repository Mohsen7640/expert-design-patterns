from behavioral.command.task.contracts.command import Command


class AddTaskCommand(Command):

    def __init__(self, task, receiver):
        self.task = task
        self.receiver = receiver

    def execute(self):
        self.receiver.operation(self)
