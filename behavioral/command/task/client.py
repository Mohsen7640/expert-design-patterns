from behavioral.command.task.commands.add import AddTaskCommand
from behavioral.command.task.models.task import Task
from behavioral.command.task.receivers.add import AddTaskReceiver


def run():
    task = Task(pk=1, title="Sample", status="DOING")
    receiver = AddTaskReceiver()
    command = AddTaskCommand(task, receiver)

    command.execute()


if __name__ == '__main__':
    run()
