@DecoratorFunc
def PositiveQuotentDivision(a, b):
    print(a/b)

def DecoratorFunc(func):
    def swapnumber(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return swapnumber

# We can also use this instead of using @DecoratorFunc
# PositiveQuotentDivision = DecoratorFunc(PositiveQuotentDivision)

PositiveQuotentDivision(2, 4)

