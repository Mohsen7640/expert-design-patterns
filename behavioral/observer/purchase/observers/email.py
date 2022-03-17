from behavioral.observer.purchase.contracts.observer_interface import ObserverInterface


class EmailObserver(ObserverInterface):

    def send(self, message=""):
        print(f'Sending Email Notification message: {message}')