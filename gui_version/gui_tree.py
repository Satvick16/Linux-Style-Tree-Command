import tkinter as tk
from tkinter import filedialog, Text
import os
from gui_tree import *


root = tk.Tk()


def get_folder_and_make_tree():
	folder_path = filedialog.askdirectory(initial="/", title="Select Folder")
	
	original_depth = len(folder_path.split('\\'))
	make_tree(folder_path, original_depth)


def make_tree(path, original_depth):
	contents = os.listdir(path)
	
	# iterate over list of contents
	for item in contents:
		
		# if item is a file (not a directory)
		if '.' in item:
			# locate full path of item	
			for root, dirs, files in os.walk(path):
				for name in files:
					display(path, original_depth, root, name, item)
		
		# if item is a directory (not a file)
		else:
			# locate full path of item
			for root, dirs, files in os.walk(path):
				for name in dirs:
					display(path, original_depth, root, name, item)

			# continue recursively searching the current directory
			make_tree(str(os.path.join(path, item)), original_depth)


def display(path, original_depth, root, name, item):
	if name == item:
		x = os.path.abspath(os.path.join(root, name))
		# determine how 'deep' item is within the file hierarchy w.r.t the original directory
		curr_depth = len(path.split('\\')) - original_depth
		
		# format the file name based on its 'depth'
		tree.insert(tk.END, "\n" + ('\t' * curr_depth) + item)


canvas = tk.Canvas(root, height=600, width=600, bg="gray")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

select_folder = tk.Button(root, text="Select Folder", padx=10, pady=5, fg="white", bg="black", command=get_folder_and_make_tree)
select_folder.pack()

tree = tk.Text(root)
tree.place(relx=0.1, rely=0.1, relwidth=0.8)

root.mainloop()
