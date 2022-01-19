class Pagination():
	def __init__(self, items=[], page_size=10):
		self.items = items
		self.page_size = page_size
		self._page = 1
		self._page_amount = len(items)//page_size+1 if len(items)%page_size else len(items)/page_size
		

	def get_visible_items(self):
		start_idx = (self._page-1) * self.page_size
		end_idx = None if self._page == self._page_amount else start_idx + self.page_size
		return self.items[start_idx: end_idx]

	def next_page(self):
		if self._page<self._page_amount:
			self._page += 1
		return self

	def prev_page(self):
		if self._page > 1:
			self._page -= 1
		return self

	def first_page(self):
		self._page = 1
		return self

	def last_page(self):
		self._page = self._page_amount
		return self

	def go_to_page(self, page_number):
		if page_number < 0:
			self._page = 1
		elif page_number > self._page_amount:
			self._page = self._page_amount
		else:
			self._page = page_number
		return self

	def get_current_page(self):
		return self._page

	def get_page_size(self):
		return self.page_size

	def get_items(self):
		return self.items




alphabetList = list("abcdefghijklmnopqrstuvwxyz")
     
p = Pagination(alphabetList, 4)
print(p.get_visible_items())

p.next_page()
print(p.get_visible_items())

p.last_page()
print(p.get_visible_items()) # ["y", "z"]
p.go_to_page(0).prev_page()
print(p._page,p._page_amount)


# a = Pagination('1234567132',7)
# a.next_page()

# # print(a._page)
# # print(a.page_size)
# # print(a._page_amount)
# # print(len(a.items)%a.page_size, len(a.items)//a.page_size+1)

# print(a.get_visible_items())