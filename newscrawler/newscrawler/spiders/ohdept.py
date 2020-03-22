# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class OhdeptSpider(CrawlSpider):
    name = 'ohdept'
    allowed_domains = ['coronavirus.ohio.gov']
    start_urls = [
        'https://coronavirus.ohio.gov/wps/portal/gov/covid-19/home/News-Releases-News-You-Can-Use'
        # ,
        # 'https://coronavirus.ohio.gov/wps/portal/gov/covid-19/home/Public-Health-Orders/'
        ]

    def parse(self, response):
        base=response.css('base::attr(href)').get()

        for paragraph in response.css('#js-odx-content__body p'):
            link=paragraph.css('a::attr(href)').get()
            if(link is None):
                continue
            date =paragraph.css('::text').re(r'\d{1,2}\/\d{1,2}\/\d{2}')        
            title = paragraph.css('a::attr(title)').get()
            if title is None:
                title = paragraph.css('a::text').extract_first()
            yield {
                    'date' : paragraph.css('::text').re_first(r'\d{1,2}\/\d{1,2}\/\d{2}'),
                    'title' : title,
                    'link' : base + link
            }


