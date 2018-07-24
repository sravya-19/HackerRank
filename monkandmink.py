def bin_search(list1, size, number, ch):
    if ch == 'g':
        start = 0
        end = size - 1
        answer = size
        while start <= end:
            mid = (start + end) // 2
            if mid not in range(0, size):
                break
            else:
                if start == end:
                    if a[mid] > number and mid < answer:
                        answer = mid
                    return size - answer
                elif a[mid] > number:
                    start = mid - 1
                    end = mid
                    if mid < answer:
                        answer = mid
                elif a[mid] <= number:
                    start = mid + 1
        return size - answer
    if ch == 'g':
        start = 0
        end = size - 1
        answer = size
        while start <= end:
            mid = (start + end) // 2
            if mid not in range(0, size):
                break
            else:
                if start == end:
                    if a[mid] >= number and mid < answer:
                        answer = mid
                    return size - answer
                elif a[mid] >= number:
                    start = mid - 1
                    end = mid
                    if mid < answer:
                        answer = mid
                elif a[mid] < number:
                    start = mid + 1
        return size - answer


if __name__ == '__main__':
    size = int(input())
    list1 = sorted(list(map(int, input().split(' '))))
    q = int(input())
    for i in range(q):
        a, b = map(int, input().split(' '))
        if a == 0:
            print(bin_search(list1, size, b, 'ge'))
        elif a == 1:
            print(bin_search(list1, size, b, 'g'))
