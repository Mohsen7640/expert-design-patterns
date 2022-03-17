from behavioral.observer.purchase.contracts.observer_interface import ObserverInterface


class SMSObserver(ObserverInterface):

    def send(self, message=""):
        print(f'Sending Mobile Notification message: {message}')