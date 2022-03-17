from structural.bridge.campaign.contracts.promotion import Promotion


class TextPromotion(Promotion):

    def __init__(self, title, url, banner_url):
        self.title = title
        self.url = url
        self.banner_url = banner_url

    def display(self):
        return f"""
             <a src={self.url}>
                <img src={self.banner_url} alt={self.title}/>
             </a>
        """
