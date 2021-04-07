def amortise(r, n, P):
    return P * ((r * (1 + r) ** n) / ((1 + r) ** n - 1))

def final_payment(A, n):
    rounding_error = (A * 100) % 1 * n
    return A + rounding_error / 100
    
def schedule(r, n, P):
    monthly = amortise(r, n, P)
    final = final_payment(monthly, n)
    str = "{} payments of {} and a final payment of {}"
    return str.format(n, "£{:0,.2f}".format(monthly), "£{:0,.2f}".format(final))
    
    
rate = 0.05
months = 5 * 12
loan_value = 10000

print(schedule(rate, months, loan_value))