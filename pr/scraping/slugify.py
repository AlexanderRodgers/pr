import re

regex = re.compile('[^a-zA-Z0-9]')

def slugify(*args):
	pre_slug = []
	for arg in args:
		print(arg)
		for string in arg.split():
			print(string)
			regex.sub('', string)
			pre_slug.append(string.lower())
	print('-'.join(pre_slug))
	return "-".join(pre_slug)