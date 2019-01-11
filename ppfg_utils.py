import random
import string
import os

# new legal file in file_dir
def new_rand(file_dir):
	while True:
		ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 9))
		if os.path.exists(file_dir + "/" + ran_str+".html"):
			continue
		return ran_str

# create file with name(file_path) and return new file (to be created in base_dir next)
def create_file(file_path, level_index, description, puzzle_function):
	base_dir = "level" + str(level_index)
	new_title = new_rand(base_dir)
	new_path = base_dir + "/" + new_title + ".html"
	file = open("../" + file_path, 'w')
	content = "".join([
		"<html><head></head><body>",
		"<div>", description, "</div>",
		"<div>", puzzle_function[0](level_index, new_title, file_path), "</div>",
		"<div>", puzzle_function[1](), "</div>",
		"</body></html>"])
	file.write(content)
	file.close()
	return new_path

def create_welcome(file_path, level_index, puzzle_function):
	description = "Welcome to Level " + str(level_index) + "!"
	return create_file(file_path, level_index, description, puzzle_function)

def create_body(file_path, level_index, puzzle_function):
	description = ""
	return create_file(file_path, level_index, description, puzzle_function)

def create_goodbye(file_path, level_index, puzzle_function):
	description = "You've passed Level " + str(level_index) + "! Next level:"
	return create_file(file_path, level_index+1, description, puzzle_function)
