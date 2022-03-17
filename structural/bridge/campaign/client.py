from structural.bridge.campaign.campaigns.paper_view import PaperViewCampaign
from structural.bridge.campaign.promotions.banner import BannerPromotion


def run():
    banner = BannerPromotion(
        title='Sample Campaign', url='https://www.google.com/', banner_url='https://www.google.com/img/'
    )
    view = PaperViewCampaign(promotion=banner)
    print(view.run())


if __name__ == "__main__":
    run()
