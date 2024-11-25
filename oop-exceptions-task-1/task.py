import math
class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page

    @property
    def page_count(self):
        pages_count = math.ceil(len(self.data) / self.items_on_page)
        return pages_count

    @property
    def item_count(self):
        return len(self.data)

    def count_items_on_page(self, page_number):
        self.page_number = page_number
        if self.page_number < self.page_count-1:
            return self.items_on_page
        elif self.page_number == self.page_count-1:
            return len(self.data) % self.items_on_page
        else:
            raise Exception("Invalid index. Page is missing.")

    def find_page(self, word):
        self.word = word
        pages_list = []
        for page in range(self.page_count):
            start_index = page * self.items_on_page
            end_index = start_index + self.items_on_page
            page_text = self.data[start_index:end_index]
            if self.word in page_text:
                pages_list.append(page)
        if not pages_list:
            raise Exception("{} is missing on the pages".format(self.word))
        return pages_list

    
    def display_page(self, page_number):
        self.page_number = page_number
        if self.page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        start_index = page_number * self.items_on_page
        end_index = start_index + self.items_on_page
        page_text = self.data[start_index:end_index]
        return page_text


pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)
print(pages.count_items_on_page(3))
print(pages.count_items_on_page(2))
print(pages.find_page('e'))
print(pages.display_page(3))

