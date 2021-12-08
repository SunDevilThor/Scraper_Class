# Scraper Class
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTML, HTMLSession

class Scraper: 

    def __init__(self): 
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
        self.base_url = 'http://www.amazon.com/dp/'

    def extract(self, asin):
        r = self.session.get(self.base_url + str(asin), headers=self.headers)
        r.html.render(sleep=1)
        scraped_item = (
            r.html.find('span#productTitle', first=True).text,
            r.html.find('span.a-offscreen', first=True).text,
        )
        return scraped_item

amazon_scraper = Scraper()
product = amazon_scraper.extract('B07M64QXMN')
print(product)
