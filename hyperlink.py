
def hyperlink_function(level_index, next_title):
	content = next_title
	file_path = "/level" + str(level_index) + "/" + next_title
	return "".join(["<a href=", file_path, ">", content, "</a>"])
