from structural.proxy.protection.contracts.map import GoogleMapAPIInterface
from structural.proxy.protection.models.user import User


class GoogleMapAPIProxy(GoogleMapAPIInterface):

    def __init__(self, user: User, google_map_api: GoogleMapAPIInterface):
        self.user = user
        self.google_map_api = google_map_api

    def check_access(self):
        if self.user.is_admin():
            return True
        return False

    def find_place_by_lat_and_long(self, lat, long):
        if self.check_access():
            return self.google_map_api.find_place_by_lat_and_long(lat, long)
        return {'mode': 'Development', 'message': 'Access denied', 'status': '403'}
