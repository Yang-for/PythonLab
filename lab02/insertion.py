def insertion_sort_recursion(a, n):
        if n == 0 :
            return
        insertion_sort_recursion(a, n - 1)
        j = n
        if j < len(a):
            while j > 0 and a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                j -= 1
            print(a)


a = [5, 4, 3, 1]
insertion_sort_recursion(a, len(a))