import time

def bubble_sort(arr, drawData):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                drawData(arr, ["blue" if i == j or i == j+1 else "red" for i in range(len(arr))])
                time.sleep(0.05)

    drawData(arr, ["blue" for i in range(len(arr))])