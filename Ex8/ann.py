import numpy as np
import math
def threshold(x):
    return 1 if x >= 0 else 0
def bipolar_threshold(x):
    return 1 if x >= 0 else -1
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def tanh(x):
    return math.tanh(x)
alpha = float(input("Enter learning rate (alpha): "))
n = int(input("Enter number of inputs: "))
weights = np.array([float(input(f"Enter w{i+1}: ")) for i in range(n)])
b = float(input("Enter bias: "))
print("\nChoose Activation Function:")
print("1. Threshold")
print("2. Sigmoid")
print("3. Tanh")
choice = int(input("Enter choice: "))
if choice == 1:
    act_binary = threshold
    act_bipolar = bipolar_threshold
elif choice == 2:
    act_binary = sigmoid
    act_bipolar = sigmoid
elif choice == 3:
    act_binary = tanh
    act_bipolar = tanh
else:
    print("Invalid choice")
    exit()
m = int(input("\nEnter number of samples: "))
print("Enter inputs + target:")
data = np.array([list(map(float, input().split())) for _ in range(m)])
inputs, targets = data[:, :-1], data[:, -1]
if set(targets).issubset({0,1}):
    data_type = "binary"
    act = act_binary
elif set(targets).issubset({-1,1}):
    data_type = "bipolar"
    act = act_bipolar
else:
    print("Targets must be {0,1} or {-1,1}")
    exit()
print(f"\nDetected: {data_type.upper()}")
for epoch in range(20):
    print(f"\n***** EPOCH {epoch+1} *****\n")
    header = ""
    for i in range(n):
        header += f"{('x'+str(i+1)):>4}"
    header += f"{'t':>6}{'yin':>10}{'y':>6}"
    for i in range(n):
        header += f"{('Δw'+str(i+1)):>10}"
    header += f"{'Δb':>8}"
    for i in range(n):
        header += f"{('w'+str(i+1)):>10}"
    header += f"{'b':>8}"
    print(header)
    print("-" * len(header))
    no_update = True
    for x, t in zip(inputs, targets):
        yin = np.dot(x, weights) + b
        y_raw = act(yin)
        if choice == 1:
            y = y_raw
        elif choice == 2:
            if data_type == "binary":
                y = 1 if y_raw >= 0.5 else 0
            else:
                y = 1 if y_raw >= 0.5 else -1
        else:
            if data_type == "binary":
                y = 1 if y_raw >= 0 else 0
            else:
                y = 1 if y_raw >= 0 else -1
        if y != t:
            if data_type == "bipolar":
                dws = alpha * x * t
                db = alpha * t
            else:
                dws = alpha * (t - y) * x
                db = alpha * (t - y)
            weights += dws
            b += db
            no_update = False
        else:
            dws = np.zeros(n)
            db = 0
        row = ""
        for val in x:
            row += f"{val:>4.0f}"
        row += f"{t:>6.0f}{yin:>10.2f}{y:>6.0f}"
        for i in range(n):
            val = dws[i]
            row += f"{val:>10}" if isinstance(val, str) else f"{val:>10.2f}"
        row += f"{db:>8}" if isinstance(db, str) else f"{db:>8.2f}"
        for w in weights:
            row += f"{w:>10.2f}"
        row += f"{b:>8.2f}"
        print(row)
    if no_update:
        for i in range(n):
            val = weights[i]
            print("w",i,"=",val)
        print("b=",b)
        print("\nConverged!")
        break
    else:
        for i in range(n):
            val = weights[i]
            print("w",i,"=",val)
        print("b=",b)
        continue

if epoch == 19:
    print("\nDid NOT converge")
