def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def get_even_list(x):    
    for i in x:
        if i%2==1:
            x = remove_values_from_list(x, i)
    return x
            
even_list = get_even_list([1, 2,1,-3, 5, -10, 9, 6,5,5])

print(even_list)
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
