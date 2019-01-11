import pyfiglet

def asciiart_function(level_index, next_title, my_path):
	content = "\n" + pyfiglet.figlet_format(next_title, font="banner3")
	return "<pre>" + content + "</pre>"
