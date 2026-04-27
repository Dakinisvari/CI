# ===== BAYES THEOREM: USER INPUT =====

print("\n--- BAYES THEOREM (SPAM DETECTION) ---")

print("S -> Spam Email")
print("F -> Contains word 'Free'\n")

print("We will compute: P(S | F)\n")

# ===== INPUT =====
P_F_given_S = float(input("Enter probability of spam mails containing the word 'Free' : "))
P_S = float(input("Enter the probability of spam mails : "))
P_F = float(input("Enter the probability of mails containing the word 'Free' : "))

# ===== VALIDATION =====
if P_F == 0:
    print(" Error: P(F) cannot be zero (division by zero).")
    exit()

# ===== CALCULATION =====
numerator = P_F_given_S * P_S
result = numerator / P_F

# ===== OUTPUT =====
print("\n--- Calculation ---")

print("\nFormula: P(S | F) = [P(F | S) * P(S)] / P(F)")

print(f"\nP(F | S)*P(S)  = {P_F_given_S:.3f} * {P_S:.3f} = {numerator:.3f}")
print(f"[P(F | S) * P(S)] / P(F) = {numerator:.3f} / {P_F:.3f}")

print("\nFinal Answer:")
print(f"P(S | F) = {result:.3f}")
