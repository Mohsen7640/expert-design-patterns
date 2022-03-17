from structural.bridge.campaign.contracts.campaign import Campaign


class PaperViewCampaign(Campaign):

    def __init__(self, promotion):
        super().__init__(promotion)

    def run(self):
        return self.promotion.display()
