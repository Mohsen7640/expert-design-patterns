from behavioral.mediator.event_dispatcher.contracts.observer import Observer


class Logger(Observer):

    def notify(self, event, emitter, data=None):
        pass
