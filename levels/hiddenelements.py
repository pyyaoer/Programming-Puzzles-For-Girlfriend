
from random import randint, choice

def hiddenelements_function(level_index, next_title, my_path):
	def random_merge(elements):
		def add_invisible_eles(e):
			eles = ["a", "img", "div"]
			invisible_eles = ["<" + x + " style=\"display:none\">" + "</" + x + ">" for x in eles]
			return e + choice(invisible_eles)
		def wrap_divs(e):
			return "<div style = \"display: inline\">" + e + "</div>"
		single_ele_funcs = [add_invisible_eles, wrap_divs]
		num_ele = len(elements)
		if num_ele == 1:
			return elements[0]
		new_ele = [x for x in elements]
		if choice([1, 2]) == 1:
			r = randint(0, num_ele - 1)
			new_ele[r] = choice(single_ele_funcs)(new_ele[r])
		else:
			r = randint(0, num_ele - 2)
			new_ele[r] += new_ele[r+1]
			del new_ele[r+1]
		return random_merge(new_ele)

	l = [str(x) for x in list(next_title)]
	return random_merge(l)

def hiddenelements_hint():
	return ""