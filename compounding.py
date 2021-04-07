def compound(P, r, n, t):
    return P * (1 + (r / n)) ** (n * t)

def compound_interest(P, r, n, t):
    return compound(P, r, n, t) - P

def aer(r, n):
    return (1 + r / n) ** n - 1

def print_statement(P, r, n, t):
    statement = """The nominal rate is {} and interest is compounded every {} month(s).
After {} years a balance of {} will have earned {} in interest.
The total balance at that time will be {}.
The Annual Equivalent Rate (AER) is {}."""
    
    print (statement.format(
        str(r * 100) + "%",
        12 / compounding_frequency ,
        t,
        "£{:0,.2f}".format(P),
        "£{:0,.2f}".format(compound_interest(P, r, n, t)),
        "£{:0,.2f}".format(compound(P, r, n, t)),
        str(aer(r, n) * 100) + "%",
    ))

balance = 5000
compounding_frequency = 24
years = 4
nominal_rate = 0.02

print_statement(balance, nominal_rate, compounding_frequency, years)