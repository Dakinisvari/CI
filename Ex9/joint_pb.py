import numpy as np

# ===== RANDOM VARIABLE DEFINITION =====
print("\n--- RANDOM VARIABLES ---")
print("Rain → random variable that represents rainy conditions")
print("Traffic → random variable that represents traffic conditions")
print("Accident → random variable that represents accident occurrence")

# ===== INPUT =====
nx, ny, nz = 2, 2, 2  # fixed for structured table

print("Enter probabilities in this order:")
print("For each Weather (Rain / No Rain),")
print("enter Traffic rows (Traffic, No Traffic), each with 2 values (Accident Yes, No)\n")

data = []

for i in range(nx):
    weather = "Rain" if i == 0 else "No Rain"
    print(f"\n--- {weather} ---")

    layer = []
    for j in range(ny):
        traffic = "Traffic" if j == 0 else "No Traffic"

        while True:
            vals = list(map(float, input(f"Enter P({traffic}, Accident Yes No): ").split()))
            if len(vals) != 2:
                print(" Enter exactly 2 values!")
            else:
                layer.append(vals)
                break

    data.append(layer)

# Convert to NumPy
joint_table = np.array(data)  # (X, Y, Z)


# ===== VALIDATION =====
total = np.sum(joint_table)
print(f"\nTotal Probability = {total:.3f}")

if not np.isclose(total, 1.0):
    print(" Invalid Joint Probability Table")
    exit()

print(" Valid Joint Probability Table")


# ===== DISPLAY TABLE =====
print("\n--- Joint Probability Table ---\n")

print(f"{'':<12}{'Accident':^30}{'No Accident':^30}")
print(f"{'':<12}{'Traffic':^15}{'No Traffic':^15}{'Traffic':^15}{'No Traffic':^15}")
print("-" * 72)

for i in range(nx):
    row_label = "Rain" if i == 0 else "No Rain"
    row = f"{row_label:<12}"

    # Accident Yes (Z=0)
    row += f"{joint_table[i][0][0]:^15.3f}"
    row += f"{joint_table[i][1][0]:^15.3f}"

    # Accident No (Z=1)
    row += f"{joint_table[i][0][1]:^15.3f}"
    row += f"{joint_table[i][1][1]:^15.3f}"

    print(row)

print("-" * 72)

# ===== ALL MARGINAL PROBABILITIES =====
P_X = np.sum(joint_table, axis=(1, 2))
P_Y = np.sum(joint_table, axis=(0, 2))
P_Z = np.sum(joint_table, axis=(0, 1))

print("\n--- All Marginal Probabilities ---")

# ===== P(X) =====
print("\nP(Rain)")
print(f"= {joint_table[0][0][0]:.3f} + {joint_table[0][0][1]:.3f} + "
      f"{joint_table[0][1][0]:.3f} + {joint_table[0][1][1]:.3f}")
print(f"= {P_X[0]:.3f}")

print("\nP(No Rain)")
print(f"= {joint_table[1][0][0]:.3f} + {joint_table[1][0][1]:.3f} + "
      f"{joint_table[1][1][0]:.3f} + {joint_table[1][1][1]:.3f}")
print(f"= {P_X[1]:.3f}")


# ===== P(Y) =====
print("\nP(Traffic)")
print(f"= {joint_table[0][0][0]:.3f} + {joint_table[0][0][1]:.3f} + "
      f"{joint_table[1][0][0]:.3f} + {joint_table[1][0][1]:.3f}")
print(f"= {P_Y[0]:.3f}")

print("\nP(No Traffic)")
print(f"= {joint_table[0][1][0]:.3f} + {joint_table[0][1][1]:.3f} + "
      f"{joint_table[1][1][0]:.3f} + {joint_table[1][1][1]:.3f}")
print(f"= {P_Y[1]:.3f}")


# ===== P(Z) =====
print("\nP(Accident)")
print(f"= {joint_table[0][0][0]:.3f} + {joint_table[0][1][0]:.3f} + "
      f"{joint_table[1][0][0]:.3f} + {joint_table[1][1][0]:.3f}")
print(f"= {P_Z[0]:.3f}")

print("\nP(No Accident)")
print(f"= {joint_table[0][0][1]:.3f} + {joint_table[0][1][1]:.3f} + "
      f"{joint_table[1][0][1]:.3f} + {joint_table[1][1][1]:.3f}")
print(f"= {P_Z[1]:.3f}")


# ===== CONDITIONAL PROBABILITIES =====
print("\n--- Conditional Probabilities ---")

# P(Accident | Rain)
num1 = joint_table[0][0][0] + joint_table[0][1][0]

print("\nP(Accident | Rain)")
print(f"= ({joint_table[0][0][0]:.3f} + {joint_table[0][1][0]:.3f}) / {P_X[0]:.3f}")
print(f"= {num1:.3f} / {P_X[0]:.3f} = {num1 / P_X[0]:.3f}")


# P(Rain | Accident)
num2 = joint_table[0][0][0] + joint_table[0][1][0]

print("\nP(Rain | Accident)")
print(f"= ({joint_table[0][0][0]:.3f} + {joint_table[0][1][0]:.3f}) / {P_Z[0]:.3f}")
print(f"= {num2:.3f} / {P_Z[0]:.3f} = {num2 / P_Z[0]:.3f}")


# P(Traffic | Accident)
num3 = joint_table[0][0][0] + joint_table[1][0][0]

print("\nP(Traffic | Accident)")
print(f"= ({joint_table[0][0][0]:.3f} + {joint_table[1][0][0]:.3f}) / {P_Z[0]:.3f}")
print(f"= {num3:.3f} / {P_Z[0]:.3f} = {num3 / P_Z[0]:.3f}")
