s = int(input("Enter the required sum: "))
total_outcomes = 36
if 2 <= s <= 7:
    favorable = s - 1
elif 8 <= s <= 12:
    favorable = 13 - s
else:
    favorable = 0
if favorable == 0:
    print("P(A) = 0 (Sum not possible)")
else:
    print("Let A be the event that sum =", s)
    print("Total outcomes =", total_outcomes)
    print("Favorable outcomes =", favorable)
    print("P(A) =", favorable, "/", total_outcomes)
    print("P(A) =", favorable / total_outcomes)
