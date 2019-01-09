
def picaddr_function(level_index, next_title, my_path):
	file_path = "/" + ".".join(my_path.split('.')[0:-1]) + ".png"

	from PIL import Image, ImageDraw, ImageFont
	img = Image.new('RGB', (120, 40), color = (0, 0, 0))
	d = ImageDraw.Draw(img)
	fnt = ImageFont.truetype("resource/consola.ttf", 20)
	d.text((10,10), next_title, fill=(255, 255, 0), font=fnt)
	img.save(".." + file_path)

	return "<img src=\"" + file_path + "\" />"