class EventDispatcher:
    """Mediator"""

    def __init__(self):
        self.observers = {}

    def attach(self, event, observer):
        self.init_event(event)
        self.observers[event].append(observer)

    def detach(self, event, observer):
        for index, observer_item in enumerate(self.get_event_observers(event)):
            if observer == observer_item:
                self.observers[event].pop(index)

    def fire(self, event, emitter, data=None):
        for observer in self.get_event_observers(event):
            observer.notify(event, emitter, data)

    def init_event(self, event):
        if not self.observers[event]:
            self.observers[event] = []

    def get_event_observers(self, event):
        self.init_event(event)
        return self.observers[event]
