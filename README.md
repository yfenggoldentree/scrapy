## Explore the 'xpath'

Xpath is how we parse a given HTML page to get the items we want. Here is an example of xpath that we used to 
crawl the sponsor websites from 'https://databricks.com/dataaisummit/2022-sponsors':
`//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href`. 

To explore an html and find the correct xpath to use, run

```
scrapy shell your_url_here
```

Once inside, you will have a `reponse` to play with
```
In [1]: response.xpath('//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href')
Out[1]: 
[<Selector xpath='//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href' data='/dataaisummit/2022-sponsors'>,
 <Selector xpath='//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href' data='https://www.immuta.com/'>,
 <Selector xpath='//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href' data='http://amazon.com/'>,
 <Selector xpath='//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href' data='http://google.com/'>,
 ...
]
```
Note how we have a list of `Selector` here that match up to the given xpath. To retrieve the `data`
field from the `Selector`, call `getall()` on the xpath object
```
In [2]: response.xpath('//div[@class="SponsordCardImageWrapper css-169ypl2"]/a[1]/@href').getall()
Out[2]: 
['/dataaisummit/2022-sponsors',
 'https://www.immuta.com/',
 'http://amazon.com/',
 'http://google.com/',
 ...
]
```
Voila, here are our expected urls for each sponsor. 

## Run the crawler and store to CSV

Once we identify the correct xpath, now we can crawl the website and output above urls to a csv file. To do so, first go to the child directory
```
cd crawler/crawler/spiders
```
We should be in a directory like `/Users/yuansongfeng/Desktop/scrapy/crawler/crawler/spiders` now. 

Once here, run the crawler
```
scrapy crawl crawler -O data.csv 
```
This stores the crawled content to `data.csv`. Check it out!