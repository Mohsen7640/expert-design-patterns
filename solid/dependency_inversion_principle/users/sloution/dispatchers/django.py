from solid.dependency_inversion_principle.users.sloution.contracts.dispatcher_interface import DispatcherInterface


class DjangoDispatcher(DispatcherInterface):

    def dispatch(self, event, params):
        pass