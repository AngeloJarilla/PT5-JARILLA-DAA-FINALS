def bubble_sort_with_steps(arr):
    n = len(arr)
    round_num = 0

    print(f"Round {round_num}: {arr}")
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        round_num += 1
        print(f"Round {round_num}: {arr}")


data = [33, 41, 28, 15, 22, 10]


bubble_sort_with_steps(data)
