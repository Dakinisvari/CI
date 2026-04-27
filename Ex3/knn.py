import numpy as np
import pandas as pd
from math import sqrt
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
def euclidean_distance(p1, p2):
    return sqrt(np.sum((np.array(p1) - np.array(p2)) ** 2))
def manhattan_distance(p1, p2):
    return np.sum(np.abs(np.array(p1) - np.array(p2)))
def chebyshev_distance(p1, p2):
    return np.max(np.abs(np.array(p1) - np.array(p2)))
def compute_distances(X_train, test_point, method):
    distances = []
    for i in range(len(X_train)):
        if method == 1:
            dist = euclidean_distance(X_train[i], test_point)
        elif method == 2:
            dist = manhattan_distance(X_train[i], test_point)
        elif method == 3:
            dist = chebyshev_distance(X_train[i], test_point)
        distances.append(dist)
    return distances
def unweighted_vote(neighbors):
    return Counter(neighbors).most_common(1)[0][0]
def weighted_vote(neighbors, distances):
    weight_dict = {}
    for i in range(len(neighbors)):
        label = neighbors[i]
        dist = distances[i]
        weight = 1 /((dist)**2+1e-9)
        if label in weight_dict:
            weight_dict[label] += weight
        else:
            weight_dict[label] = weight
    return max(weight_dict, key=weight_dict.get)
def calculate_k(training_size):
    k = int(0.1 * training_size)
    if k % 2 == 0:
        k += 1
    return max(k, 1)
def knn_predict(X_train, y_train, X_test, k, dist_method, vote_method):
    predictions = []
    for test_point in X_test:
        distances = compute_distances(X_train, test_point, dist_method)
        sorted_indices = np.argsort(distances)
        k_indices = sorted_indices[:k]
        k_labels = [y_train[i] for i in k_indices]
        k_distances = [distances[i] for i in k_indices]
        if vote_method == 1:
            prediction = unweighted_vote(k_labels)
        else:
            prediction = weighted_vote(k_labels, k_distances)
        predictions.append(prediction)
    return predictions
print("1. Manual Data Input")
print("2. CSV File Input (Iris Dataset)")
choice = int(input("Choose option: "))
if choice == 1:
    num_features = int(input("Enter number of features: "))
    col_names = input(f"Enter names for the {num_features} features (space separated): ").split()
    n = int(input("Enter number of training data points: "))

    data, labels = [], []
    print(f"Enter data row-wise ({' '.join(col_names)} ClassLabel):")
    for _ in range(n):
        row = list(map(str, input().split()))
        data.append([float(x) for x in row[:-1]])
        labels.append(row[-1])

    k = int(input("Enter K value: "))
    test_val = list(map(float, input(f"Enter test point ({' '.join(col_names)}): ").split()))
    dist_m = int(input("Distance (1:Euclidean, 2:Manhattan, 3:Chebyshev): "))
    vote_m = int(input("Voting (1:Unweighted, 2:Weighted): "))

    # 1. Input Data Table
    print("\n--- [Step 1] Input Training Data ---")
    header = f"{'Idx':<4} | " + " | ".join([f"{name:<10}" for name in col_names]) + " | Label"
    print(header)
    print("-" * len(header))
    for i in range(n):
        feats = " | ".join([f"{val:<10.2f}" for val in data[i]])
        print(f"{i:<4} | {feats} | {labels[i]}")

    # 2. Distance Table
    dists = compute_distances(data, test_val, dist_m)
    dist_info = sorted([{'id': i, 'd': dists[i], 'l': labels[i]} for i in range(n)], key=lambda x: x['d'])

    print("\n--- [Step 2] Sorted Distances ---")
    print(f"{'Rank':<5} | {'Dist':<10} | {'Label':<10}")
    print("-" * 40)
    for r, info in enumerate(dist_info, 1):
        status = "K-Neighbor" if r <= k else ""
        print(f"{r:<5} | {info['d']:<10.4f} | {info['l']:<10}")

        # 3. Voting Steps
        # 3. Voting Steps
    print("\n--- [Step 3] Voting Details ---")
    k_neighbors = dist_info[:k]
    k_labels = [n['l'] for n in k_neighbors]

    # Identify all possible unique labels from the entire training set
    all_unique_labels = sorted(list(set(labels)))

    if vote_m == 1:
        print("Method: Unweighted Voting (Majority Rule)")
        counts = Counter(k_labels)

        # Print votes for EVERY unique label found in the training data
        for lbl in all_unique_labels:
            vote_count = counts.get(lbl, 0)
            print(f"Label {lbl}: {vote_count} vote(s)")

        result = counts.most_common(1)[0][0]
    else:
        print("Method: Weighted Voting (1 / dist^2)")
        weights = {}
        # Calculate weights for the K-neighbors
        for i, nbr in enumerate(k_neighbors):
            w = 1 / (nbr['d']**2 + 1e-9)
            weights[nbr['l']] = weights.get(nbr['l'], 0) + w
            print(f"Neighbor {i+1} (Label {nbr['l']}): Dist {nbr['d']:.4f} -> Weight {w:.4f}")

        print("\nAccumulated Weights per Class:")
        # Print weights for EVERY unique label
        for lbl in all_unique_labels:
            total_w = weights.get(lbl, 0.0)
            print(f"Label {lbl}: {total_w:.4f}")

        result = max(weights, key=weights.get)

    print(f"FINAL PREDICTED CLASS: {result}")


elif choice == 2:
    file_path = input("Enter CSV file path (iris dataset): ")
    df = pd.read_csv(file_path)
    print("Columns in dataset:")
    for i, col in enumerate(df.columns):
        print(i, ":", col)
    target_col = input("Enter target column name: ")
    attribute_cols = list(map(int, input("Enter attribute column numbers (space separated): ").split()))
    train_percent = float(input("Enter training percentage (e.g., 70): "))
    X = []
    for index, row in df.iterrows():
        temp = []
        for col_index in attribute_cols:
            temp.append(row[df.columns[col_index]])
        X.append(temp)
    y = df[target_col].tolist()
    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 - train_percent / 100, random_state=421)
    k = calculate_k(len(X_train))
    print("Calculated K value:", k)
    print(f"\nTotal number of records in dataset: {len(df)}")
    print(f"Number of training records: {len(X_train)}")
    print(f"Number of testing records: {len(X_test)}")
    print("Choose Distance Method:")
    print("1. Euclidean")
    print("2. Manhattan")
    print("3. Chebyshev")
    dist_method = int(input())
    print("Choose Voting Method:")
    print("1. Unweighted")
    print("2. Weighted")
    vote_method = int(input())
    predictions = knn_predict(X_train, y_train, X_test, k, dist_method, vote_method)
    acc = accuracy_score(y_test, predictions)
    prec = precision_score(y_test, predictions, average='macro')
    rec = recall_score(y_test, predictions, average='macro')
    f1 = f1_score(y_test, predictions, average='macro')
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, predictions)
    print(cm)
    print("\nPerformance Metrics:")
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 Score:", f1)
