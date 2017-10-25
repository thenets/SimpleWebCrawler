# -*- coding: utf-8 -*-
import scrapy, time, json, os


class TudogostosoSpider(scrapy.Spider):
    name = 'tudogostoso'
    allowed_domains = ['tudogostoso.com.br']
    start_urls = ['http://www.tudogostoso.com.br/receita/193463-sanduiche-de-mortadela.html']

    def parse(self, response):
        ingredients = []

        for i in response.css('#info-user > ul > li'):
            ingredients.append(i.extract())
        
        json_ingredients = json.dumps(ingredients)
        print("OOOOOOI", json_ingredients)

        directory = '../out'
        try:
            os.stat(directory)
        except:
            os.mkdir(directory) 
        filename = directory+'/recipe-0.json'
        with open(filename, 'wb') as f:
            f.write(json_ingredients)