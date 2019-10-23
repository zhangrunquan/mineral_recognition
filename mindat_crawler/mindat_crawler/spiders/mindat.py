# -*- coding: utf-8 -*-
import scrapy
from tool import Tools

class MindatSpider(scrapy.Spider):
    name = 'mindat'
    allowed_domains = ['mindat.org']
    start_urls = ['http://mindat.org/']

    def parse(self, response):
        keyword_list=['正长石']
        for kw in keyword_list:
            
