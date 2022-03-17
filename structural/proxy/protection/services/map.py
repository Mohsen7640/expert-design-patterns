from structural.proxy.protection.contracts.map import GoogleMapAPIInterface


class GoogleMapAPI(GoogleMapAPIInterface):

    def find_place_by_lat_and_long(self, lat, long):
        """
        Find a place by latitude and longitude.
        :param lat:
        :param long:
        :return: Dictionary containing location information.
        """
        pass
