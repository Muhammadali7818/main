
def faktorial(n):
    result = 1  
    for i in range(2, n + 1):
        result *= i  
    return result

natija = faktorial(son)
print(f"faktoriali: {natija}")
