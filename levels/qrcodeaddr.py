
def qrcodeaddr_function(level_index, next_title, my_path):
	file_path = "/" + ".".join(my_path.split('.')[0:-1]) + ".png"
	import qrcode
	img = qrcode.make(next_title)
	img.save(".." + file_path)
	return "<img src=\"" + file_path + "\" />"

def qrcodeaddr_hint():
	return ""