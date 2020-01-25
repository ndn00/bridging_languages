import io
import sys

def heapify(arr, n, i):
    root = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[i] < arr[l]:
        root = l
    if r < n and arr[root] < arr[r]:
        root = r
    if root != i:
        arr[i],arr[root] = arr[root],arr[i]
        heapify(arr, n, root)

def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def main():
    inp = sys.stdin
    out = sys.stdout
    n = inp.readline()
    a = inp.readline().split('\n')[0].split(' ')
    arr = []
    for i in a:
        arr.append(int(i))
    heapSort(arr)
    print("{}".format(arr))

if __name__=="__main__":
    main()