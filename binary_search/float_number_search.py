def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    operation_amount = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        operation_amount += 1
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return operation_amount, arr[mid]
 
    # якщо елемент не знайдений
    return operation_amount, arr[low] 

arr = [2.1, 2.4, 3.2, 3.4, 3.6, 5.5, 10.0]
x = 5.7
operation_amount, el  = binary_search(arr, x)
print(f"Next-closest element is {el}, operations {operation_amount}")

