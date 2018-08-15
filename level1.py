from ppfg_utils import level_names

def level1_body(level_index, title):
	return "".join([
		"<html><head></head><body>",
		"<p>",
		title,
		"</p></body></html>"])

def level1_welcome(level_index, title):
	return "".join([
		"<html><head></head><body>",
		"<p>Level 1:",
		title,
		"</p></body></html>"])

def level1_goodbye(level_index, title):
	content = title
	file_path = "/" + level_names[level_index] + "/" + title
	return "".join([
		"<html><head></head><body>",
		"<p>You've passed Level 1! Next level:</p>",
		"<p>",
		content,
		"</p></body></html>"])