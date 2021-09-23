import scrapy


class KinvoSpider(scrapy.Spider):
    name = 'kinvo'
    start_urls = ['https://www.financenews.com.br/feed/']

    def parse(self, response, **kwargs):
        #response.selector.register_namespace('content', 
        #                             'http://purl.org/rss/1.0/modules/content/')
        #response.selector.remove_namespaces()
        
        #'//channel/item/encoded'
        for i in response.css('item'):
            #print(i.css('p::text'))
              
            yield{
                #'titulo': i.css('title::text').getall(),
                #'descricao': i.css('description::text').getall()
                'noticia': i.css('p.span::text').attrib['span']
            }
