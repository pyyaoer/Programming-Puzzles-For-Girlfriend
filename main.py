import random
import string
import os
import shutil

def level0(level_index, title):
	content = title
	file_path = "/" + level_names[level_index] + "/" + title
	return "".join([
		"<html><head></head><body>",
		"<a href=", file_path, ">",
		content,
		"</a></body></html>"])

def level1(level_index, title):
	return "".join([
		"<html><head></head><body>",
		"<p>",
		title,
		"</p></body></html>"])

level_names = ["level0", "level1", "level2"]
level_nums = [2, 2]
level_funcs = [level0, level1]

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

# create level in base_dir
def create_level(file_path, level_index, num):
	base_dir = "../" + level_names[level_index]
	if not os.path.exists(base_dir):
		os.mkdir(base_dir)
	for x in xrange(1, num):
		file_path = create_file(file_path, level_index, level_funcs[level_index])
	return create_file(file_path, level_index+1, level_funcs[level_index])

if __name__ == '__main__':
	start_file = "index.html"
	try:
		os.remove("../" + start_file)
		for level in level_names:
			shutil.rmtree("../" + level)
	except Exception as e:
		pass
	for x in xrange(0,2):
		start_file = create_level(start_file, x, level_nums[x])

	if not os.path.exists("../" + level_names[2]):
		os.mkdir("../" + level_names[2])
	file = open("../" + start_file, 'w')
	content = "Congratulations!"
	file.write(content)
	file.close()
