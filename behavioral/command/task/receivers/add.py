from time import sleep


class AddTaskReceiver:

    def operation(self, command):
        print("Delay")
        sleep(5)
        print(f'Add Task: Title: {command.task.title} - Status: {command.task.status}')