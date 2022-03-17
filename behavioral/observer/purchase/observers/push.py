from behavioral.observer.purchase.contracts.observer_interface import ObserverInterface


class PushObserver(ObserverInterface):

    def send(self, message=""):
        print(f'Sending Push Notification message: {message}')