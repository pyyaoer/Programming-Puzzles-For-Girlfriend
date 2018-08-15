from ppfg_utils import level_names

def level0_body(level_index, title):
	content = title
	file_path = "/" + level_names[level_index] + "/" + title
	return "".join([
		"<html><head></head><body>",
		"<a href=", file_path, ">",
		content,
		"</a></body></html>"])

def level0_welcome(level_index, title):
	content = title
	file_path = "/" + level_names[level_index] + "/" + title
	return "".join([
		"<html><head></head><body>",
		"<p>Welcome to Level 0!</p>",
		"<a href=", file_path, ">",
		content,
		"</a></body></html>"])

def level0_goodbye(level_index, title):
	content = title
	file_path = "/" + level_names[level_index] + "/" + title
	return "".join([
		"<html><head></head><body>",
		"<p>You've passed Level 0! Next level:</p>",
		"<a href=", file_path, ">",
		content,
		"</a></body></html>"])