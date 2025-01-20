from itertools import batched

class Pager:
    def __init__(self, results, page_size=25):
        self.pages = batched(results, page_size)

    def next_page(self):
        """Gets the next page of results or None."""
        return next(self.pages, None)

pager = Pager(range(10), page_size=4)
print(pager.next_page())  # (0, 1, 2, 3)
print(pager.next_page())  # (4, 5, 6, 7)
print(pager.next_page())  # (8, 9)
print(pager.next_page())  # None