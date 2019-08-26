        def common_elements(a, b):
            return [element for element in a if element in b]


        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        c = common_elements(a, b)

        print(c)

        for i in range(c):
            if (c[i] == c[i + 1]):


