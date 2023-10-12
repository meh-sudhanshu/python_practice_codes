
def sum_till_nth(n):
    




def nth_fibonaci_number(n):
    if n==1 or n==2:
        return n-1
    return nth_fibonaci_number(n-1)+nth_fibonaci_number(n-2)

print(nth_fibonaci_number(10))