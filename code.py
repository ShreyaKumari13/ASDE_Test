def can(p, k, a, b):
    n = len(k)
    k3_regenerated = False
    k7_regenerated = False
    
    for i in range(n):
        if a > 0:
            a -= 1
            print(f"Skipped circle {i+1}")
            continue
        
        if p < k[i]:
            print(f"Failed at circle {i+1}. Power remaining: {p}, Enemy power: {k[i]}")
            return "Failure"
        
        print(f"Battling enemy at circle {i+1}. Power before battle: {p}, Enemy power: {k[i]}")
        p -= k[i]
        print(f"Power after battle: {p}")
        
        # Handle regeneration attacks from k3 and k7
        if i == 4 and not k3_regenerated:
            k3_regenerated = True
            print(f"k3 enemy regenerates with power {k[2] / 2} and attacks from behind")
            if p < k[2] / 2:
                print(f"Failed at regeneration attack by k3. Power remaining: {p}, Regenerated power: {k[2] / 2}")
                return "Failure"
            p -= k[2] / 2
            print(f"Power after k3 regeneration attack: {p}")
        
        if i == 8 and not k7_regenerated:
            k7_regenerated = True
            print(f"k7 enemy regenerates with power {k[6] / 2} and attacks from behind")
            if p < k[6] / 2:
                print(f"Failed at regeneration attack by k7. Power remaining: {p}, Regenerated power: {k[6] / 2}")
                return "Failure"
            p -= k[6] / 2
            print(f"Power after k7 regeneration attack: {p}")
        
        if b > 0 and p < (k[i+1] if i+1 < n else 0):
            recharge_amount = 30  # Assuming a recharge amount (can be set according to requirements)
            print(f"Recharging power by {recharge_amount}. Recharge attempts left: {b}")
            p += recharge_amount
            b -= 1
            print(f"Power after recharge: {p}")
    
    return "Success"

# Test Case 1 (Success)
p1 = 120
k1 = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
a1 = 3  # Number of skips
b1 = 2  # Number of recharges
result1 = can(p1, k1, a1, b1)
print(f"Test Case 1: {result1}\n")

# Test Case 2 (Failure)
p2 = 80
k2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
a2 = 1  # Number of skips
b2 = 0  # Number of recharges
result2 = can(p2, k2, a2, b2)
print(f"Test Case 2: {result2}\n")
