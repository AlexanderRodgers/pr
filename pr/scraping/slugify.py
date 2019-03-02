import re

regex = re.compile('[^a-zA-Z0-9]')

def slugify(*args):
	pre_slug = []
	for arg in args:
		for string in arg.split():
			regex.sub('', string)
			pre_slug.append(string.lower())
	return "-".join(pre_slug)