import scrapy


class AbwebSpider(scrapy.Spider):
    name = 'ABWeb'
    allowed_domains = ['www.abweb.biz']
    start_urls = ['http://www.abweb.biz/']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'image Link':x.xpath(newsel).extract_first(),
            }
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page))