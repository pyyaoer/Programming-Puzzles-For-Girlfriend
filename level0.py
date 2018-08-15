from ppfg_utils import level_names

def level0(level_index, title):
	content = title
	file_path = "/" + level_names[level_index] + "/" + title
	return "".join([
		"<html><head></head><body>",
		"<a href=", file_path, ">",
		content,
		"</a></body></html>"])
