import tkinter as tk
import random
from bubbleSort import bubble_sort
from mergeSort import merge_sort

window = tk.Tk()
window.title("Text Editor")

window.maxsize(900, 400)

data = []

def bar(arr, color_arr):
	canvas.delete("all")
	c_height = 400
	c_width = 700
	x_width = c_width / (len(arr) + 1)
	offset = 10
	spacing = 5
	normalizedData = [i/max(arr) for i in arr]
	for i, height in enumerate(normalizedData):
		# top left
		x0 = i * x_width + offset + spacing
		y0 = c_height - height * 350
		# bottom right
		x1 = (i + 1) * x_width + offset
		y1 = c_height

		canvas.create_rectangle(x0, y0, x1, y1, fill=color_arr[i])
		canvas.create_text(x0+2, y0, anchor=tk.SW, text=str(arr[i]))

	window.update_idletasks() # to see bar getting sorted step by step

def generate():
	global data
	minVal = 1
	maxVal = 100
	size = 30

	data = []
	for i in range(size):
		data.append(random.randrange(minVal, maxVal+1))
	bar(data, ["red" for i in range(len(data))])

def startAlgorithm_1():
	global data
	bubble_sort(data, bar)

def startAlgorithm_2():
	global data
	merge_sort(data, bar)


canvas = tk.Canvas(window, width=700, height=400)
buttons = tk.Frame(window)

# buttons in buttons frame
merge_bt = tk.Button(buttons, text="Merge Sort", command=startAlgorithm_2)
bubble_bt = tk.Button(buttons, text="Bubble Sort", command=startAlgorithm_1)
shuffle = tk.Button(buttons, text="Shuffle", command=generate)


# setting layout for the buttons in buttons frame
merge_bt.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
bubble_bt.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
shuffle.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

# setting the grid for text and buttons field
buttons.grid(row=0, column=0, sticky="ns")
canvas.grid(row=0, column=1, sticky="nsew")

window.mainloop()