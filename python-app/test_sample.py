import falcon
from sample import QuoteResource
import falcon.testing as testing

class TestThings(testing.TestBase):
    def before(self):
        quotes = QuoteResource()
        self.api.add_route('/quote', quotes )

    def test_grace(self):
        body = self.simulate_request('/quote', decode='utf-8')
        self.assertEqual(self.srmock.status, falcon.HTTP_200)

