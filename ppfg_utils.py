import random
import string
import os

level_names = ["level0", "level1", "level2"]

# new legal file in file_dir
def new_rand(file_dir):
	while True:
		ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
		if os.path.exists(file_dir + "/" + ran_str+".html"):
			continue
		return ran_str

# create file with name(file_path) and return new file (to be created in base_dir next)
def create_file(file_path, level_index, content_func):
	base_dir = level_names[level_index]
	new_title = new_rand(base_dir) + ".html"
	new_path = base_dir + "/" + new_title
	file = open("../" + file_path, 'w')
	content = content_func(level_index, new_title)
	file.write(content)
	file.close()
	return new_path
