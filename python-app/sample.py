import falcon
import json
 
class QuoteResource:
    def on_get(self, req, resp):
        quote = {
            'quote': 'Sillyness is important',
            'author': 'nobody'
        }

        resp.body = json.dumps(quote)
 
api = falcon.API()
api.add_route('/quote', QuoteResource())
