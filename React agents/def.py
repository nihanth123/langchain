def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n%2 ==1

numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if is_even(n)]
odds = [n for n in numbers if is_odd(n)]
print(evens)  # [2, 4, 6]
print(odds)