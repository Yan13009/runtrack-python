def custom_round(num):
   
    return int(num + 0.5)

def custom_sort(lst):
   
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                
                lst[i], lst[j] = lst[j], lst[i]


numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


rounded_numbers = [custom_round(num) for num in numbers]


custom_sort(rounded_numbers)


print(rounded_numbers)
