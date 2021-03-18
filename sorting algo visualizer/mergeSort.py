import time

def merge_sort(data, drawData):
	merge_algo(data, 0, len(data)-1, drawData)

def merge_algo(data, left, right, drawData):
	if left < right:
		middle = (left + right) // 2
		merge_algo(data, left, middle, drawData)
		merge_algo(data, middle+1, right, drawData)
		merge(data, left, middle, right, drawData)

def merge(data, left, middle, right, drawData):
	drawData(data, colorArray(len(data), left, middle, right))
	time.sleep(0.05)

	l = data[left:middle+1]
	r = data[middle+1:right+1]

	l_idx, r_idx = 0, 0
	for x in range(left, right+1):
		if l_idx < len(l) and r_idx < len(r):
			if l[l_idx] <= r[r_idx]:
				data[x] = l[l_idx]
				l_idx += 1
			else:
				data[x] = r[r_idx]
				r_idx += 1
		elif l_idx < len(l):
			data[x] = l[l_idx]
			l_idx += 1
		else:
			data[x] = r[r_idx]
			r_idx += 1

	drawData(data, ["blue" if i>=left and i <=right else "white" for i in range(len(data))])
	time.sleep(0.05)

def colorArray(length, left, middle, right):
	colorArr = []

	for i in range(length):
		if i >= left and i <= right:
			if i <= middle:
				colorArr.append("yellow")
			else:
				colorArr.append("orange")
		else:
			colorArr.append("grey")

	return colorArr