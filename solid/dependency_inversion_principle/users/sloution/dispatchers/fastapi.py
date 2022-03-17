from solid.dependency_inversion_principle.users.sloution.contracts.dispatcher_interface import DispatcherInterface


class FastAPIDispatcher(DispatcherInterface):

    def dispatch(self, event, params):
        pass