from abc import ABC, abstractmethod


class GoogleMapAPIInterface(ABC):

    @abstractmethod
    def find_place_by_lat_and_long(self, lat, long):
        pass
