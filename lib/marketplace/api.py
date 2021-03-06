from django.conf import settings

from ..utils import SlumberWrapper
from slumber.exceptions import HttpClientError


class TierNotFound(Exception):
    pass


class MarketplaceAPI(SlumberWrapper):
    errors = {}

    def get_price(self, tier):
        # TODO: cache this.
        try:
            return self.api.webpay.prices(id=tier).get(provider='bango')
        except HttpClientError, err:
            if err.response.status_code:
                raise TierNotFound(tier)
            raise

if not settings.MARKETPLACE_URL:
    raise ValueError('MARKETPLACE_URL is required')

client = MarketplaceAPI(settings.MARKETPLACE_URL)
client.slumber.activate_oauth(settings.MARKETPLACE_OAUTH.get('key'),
                              settings.MARKETPLACE_OAUTH.get('secret'))
