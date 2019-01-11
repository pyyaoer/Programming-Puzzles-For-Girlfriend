
# a file my_path directs to the "level_index"th level named next_title
def hyperlink_function(level_index, next_title, my_path):
	file_path = "/level" + str(level_index) + "/" + next_title + ".html"
	return "".join(["<a href=", file_path, ">", next_title, "</a>"])
