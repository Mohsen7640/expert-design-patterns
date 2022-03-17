class Task:

    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status


class TaskStatus:
    INIT = 0
    DOING = 1
    DONE = 2
