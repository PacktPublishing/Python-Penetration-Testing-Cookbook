from scrapy.item import Item, Field

class BookItem(Item):
    title = Field()
    price = Field()

