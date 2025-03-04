# Counting sort
# Time: O(k + n)
# Space: O(k)

def counting_sort(arr):

    n = len(arr)
    maxx = max(arr)
    counts = [0] * (maxx + 1)

    for x in arr:
        counts[x] += 1

    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1

if __name__ == "__main__":
    arr = [5, 3, 2, 1, 3, 3, 7, 1, 3]
    counting_sort(arr)
    print(arr)

