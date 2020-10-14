import tkinter as tk
from tkinter import filedialog, Text
import os
from gui_tree import *


root = tk.Tk()
root.title("Directory Tree Generator")
root.iconbitmap("tree_icon.ico")

app_width = 600
app_height = 650

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


def get_folder_and_make_tree():
	folder_path = filedialog.askdirectory(initial="/", title="Select Folder")
	
	original_depth = len(folder_path.split('\\'))
	make_tree(folder_path, original_depth)


def make_tree(path, original_depth):
	contents = os.listdir(path)
	
	for item in contents:
		
		if '.' in item:
			for root, dirs, files in os.walk(path):
				for name in files:
					display(path, original_depth, root, name, item)
		
		else:
			for root, dirs, files in os.walk(path):
				for name in dirs:
					display(path, original_depth, root, name, item)

			make_tree(str(os.path.join(path, item)), original_depth)


def display(path, original_depth, root, name, item):
	if name == item:
		x = os.path.abspath(os.path.join(root, name))
		curr_depth = len(path.split('\\')) - original_depth
		
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
