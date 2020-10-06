import os


def tree(path, original_depth):
	# list all directories within current path
	contents = os.listdir(path)
	
	# iterate over list of contents
	for item in contents:
		# if item is a file (not a directory)
		if '.' in item:

			# locate full path of item			
			for root, dirs, files in os.walk(path):
				for name in files:
					if name == item:
						x = os.path.abspath(os.path.join(root, name))
						# determine how 'deep' item is within the file hierarchy w.r.t the original directory
						curr_depth = len(path.split('\\')) - original_depth
						
						# format the file name based on its 'depth'
						print(('\t' * curr_depth) + item)
		# if item is a directory
		else:
			
			# locate full path of item
			for root, dirs, files in os.walk(path):
				for name in dirs:
					if name == item:
						x = os.path.abspath(os.path.join(root, name))
						# determine how 'deep' item is within the file hierarchy w.r.t the original directory
						curr_depth = len(path.split('\\')) - original_depth
						
						# format the directory name based on its 'depth'
						print(('\t' * curr_depth) + item)

			# continue recursively searching the current directory
			tree(str(os.path.join(path, item)), original_depth)


def main():
	# Windows-style path of the directory in question
	PATH = r' <<insert the location of this repository on your device>> \demo_dir'
	PATH_DEPTH = len(PATH.split('\\'))

	print()
	tree(PATH, PATH_DEPTH)
	print()


if __name__ == '__main__':
	main()
