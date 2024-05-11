import scrapy


class CountriesSpider(scrapy.Spider): #Basically, the CountriesSpider is the class and it is a subclass of scrapy.Spider
    #which it inherits from the spider class. Therefore, scrapy.Spider the parent class.


    #In this case, CountriesSpider is inheriting from scrapy.Spider, which means it will have the functionalities provided by scrapy.Spider 
    #and can also have its own additional or modified functionalities.

    name = "countries"                  #...located in Scrapy module. The spider name here is "countries". The spider name must be unique.
    allowed_domains = ["www.worldometers.info/"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        title = response.xpath("//h1/text()").get()

        countries= response.xpath("//td/a/text()").getall()

        yield{

            'title': title,
            'countries': countries
        }

#You cannot have two spiders with the same name!because it will create a conflict!
    
# allowed_domains = [" "] must contain all the domains that the spider is allowed to access and scrape
# In the  allowed_domains = [" "], NEVER EVER put http protocol in the begining e.g "https://www.worldometers.info/" , LEAVE THE HTTP PROTOCOL

#in start_urls =[""], we write all the links we want to scrape.
    


#Since the scrapy by default http protocol and the website uses https protocol so change the website http protocol to https by adding "s":
 #start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

#def parse(self, response): - the parse method is used to parse the response we get back from the spider