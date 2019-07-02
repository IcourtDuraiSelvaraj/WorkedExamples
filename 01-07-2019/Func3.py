def simple_interest3(p, t, r):
    print(p)
    return (p * t * r) / 100

def simple_interest3(p, t, r, k=10):
    print(k)
    return (p * t * r *k) / 100

def simple_interest3(p, t, r, k=10, l=90):
    print(l)
    return (p * t * r *k) / 100


print("Simple Interest: ", simple_interest3(p = 1900, t = 10, r = 10))

print("Simple Interest: ", simple_interest3(p = 1900, t = 10, r = 10, l=99))

print("Simple Interest: ", simple_interest3(p = 1900, t = 10))