from structural.bridge.campaign.contracts.promotion import Promotion


class VideoPromotion(Promotion):

    def __init__(self, title, video_url):
        self.title = title
        self.video_url = video_url

    def display(self):
        pass
