import scrapy


class FacebookSpider(scrapy.Spider):
    name = 'facebook'
    allowed_domains = ['www.facebook.com']
    start_urls = ['http://www.facebook.com/']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'image Link':x.xpath(newsel).extract_first(),
            }