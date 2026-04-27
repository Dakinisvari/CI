import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
def calc(y,target):
    probs,counts = y.value_counts(normalize=True),y.value_counts()
    if target=="Entropy":
        ent = -(probs * np.log2(probs)).sum()
        print(f"     Entropy = {round(ent,4)}")
        return ent
    else:
        g = 1 - (probs ** 2).sum()
        print(f"     Gini = {round(g,4)}")
        return g
def weighted_impurity(df, feature, target, criterion):
    if criterion == "Entropy":
        print("\nCalculating Weighted Entropy:")
    else:
        print("\nCalculating Weighted Gini:")
    total = len(df)
    weighted_value = 0
    for value, subset in df.groupby(feature):
        print(f"\n  For {feature} = {value}")
        impurity = calc(subset[target], criterion)
        weight = len(subset) / total
        contrib = weight * impurity
        weighted_value += contrib
    if criterion == "Entropy":
        print(f"\nTotal Weighted Entropy of {feature} = {round(weighted_value,4)}")
    else:
        print(f"\nTotal Weighted Gini of {feature} = {round(weighted_value,4)}")
    return weighted_value
def information_gain(df, feature, target, criterion):
    print("\n-----------------------------------")
    print(f"Evaluating Feature: {feature}")
    print("\nCalculating Initial Impurity")
    initial = calc(df[target], criterion)
    weighted = weighted_impurity(df, feature, target, criterion)
    ig = initial - weighted
    print(f"\nInformation Gain({feature}) = {round(initial,4)} - {round(weighted,4)}")
    print(f"IG({feature}) = {round(ig,4)}")
    print("-----------------------------------")
    return ig
def build_tree(df, target, criterion, level=0):
    indent = "   " * level
    if df[target].nunique() == 1:
        leaf = df[target].unique()[0]
        print(indent + f"Leaf Node {leaf}")
        return leaf
    if len(df.columns) == 1:
        majority = df[target].mode().values[0]
        print(indent + f"No features left. Majority {majority}")
        return majority
    features = df.columns.drop(target)
    print("\n" + indent + "Calculating Information Gain for all features")
    gains = {}
    for f in features:
        gains[f] = information_gain(df, f, target, criterion)

    best_feature = max(gains, key=gains.get)

    print("\n" + indent + f"Best Feature Selected {best_feature}")
    print(f"\nThe root node is {best_feature} ")
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = list(tree.keys())[0]
    value = sample[feature]
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        return None
print("1. Manual Input")
print("2. Load CSV File")
choice = input("Enter choice: ")
if choice == '1':
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns (including target): "))
    col_names = [input(f"Enter column {i+1} name: ") for i in range(cols)]
    data = [input(f"Enter row {i+1}: ").split() for i in range(rows)]
    df = pd.DataFrame(data, columns=col_names)
    print("\nDataset Loaded:")
    print(df)
    target = input("\nEnter Target Column Name: ")
    print("\nChoose Criterion")
    print("1. Entropy")
    print("2. Gini Index")
    crit_choice = input("Enter choice: ")
    criterion = "Entropy" if crit_choice == '1' else "Gini"
    print("\n================ BUILDING COMPLETE TREE ================")
    build_tree(df, target, criterion)
elif choice == '2':
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
    print(f"\nTotal number of records in dataset: {len(df)}")
    print(f"Number of training records: {len(X_train)}")
    print(f"Number of testing records: {len(X_test)}")
    print("\nChoose Criterion")
    print("1. Entropy")
    print("2. Gini Index")
    crit_choice = input("Enter choice: ")
    crit_param = "entropy" if crit_choice == '1' else "gini"
    clf = DecisionTreeClassifier(criterion=crit_param)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
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
else:
    print("Invalid choice")
