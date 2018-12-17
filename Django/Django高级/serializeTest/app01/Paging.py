


class Paging(object):
	"""
	分页类
	具有生成页码: page_number
	计算页数: total属性
	获取上一页和下一页
	获取当前页起始条数和终止条数
	"""

	def __init__(self, total, one_page_num=10, max_page=5):
		self.total, m = divmod(total, one_page_num)
		if m:
			self.total += 1
		self.one_page_num = one_page_num
		self.max_page = max_page
		if self.max_page > self.total:
			self.max_page = self.total
		self.half_max_page = max_page // 2
		print('Paging', self.total)
		print('Paging', self.one_page_num)
		print('Paging', self.max_page)
		print('Paging', self.half_max_page)


	def page_number(self, current):
		"""
		根据当前页生成页码
		"""
		start_page = current - self.half_max_page
		end_page = current + self.half_max_page
		if current - self.half_max_page <= 1:
			start_page = 1
			end_page = self.max_page
		if end_page >= self.total:
			end_page = self.total 
			start_page = self.total - self.max_page + 1
		books_list = [i for i in range(start_page, end_page + 1)]
		return books_list

	def up_down_page(self, current):
		"""
		获取上一页和下一页
		"""
		if current <= 1:
			up_page = None
		else:
			up_page = current - 1

		if current >= self.total:
			down_page = None
		else:
			down_page = current + 1

		return (up_page, down_page)

	def start_end_strip(self, current):
		# 起始条数
		start_strip = (current - 1) * self.one_page_num
		# 终止条数
		end_strip = current * self.one_page_num
		return (start_strip, end_strip)









		