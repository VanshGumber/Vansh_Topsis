import sys
import pandas as pd
import numpy as np

if len(sys.argv) != 5:
    print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
    sys.exit(1)

inp = sys.argv[1]
w = sys.argv[2]
imp = sys.argv[3]
out = sys.argv[4]

try:
    df = pd.read_csv(inp)
except FileNotFoundError:
    print("Input file not found")
    sys.exit(1)

if df.shape[1] < 3:
    print("Input file must contain three or more columns")
    sys.exit(1)

data = df.iloc[:, 1:]

try:
    data = data.astype(float)
except:
    print("From 2nd to last columns must contain numeric values only")
    sys.exit(1)

weights = w.split(",")
impacts = imp.split(",")

if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
    print("Number of weights, impacts and criteria columns must be same")
    sys.exit(1)

try:
    weights = [float(i) for i in weights]
except:
    print("Weights must be numeric and comma separated")
    sys.exit(1)

for i in impacts:
    if i not in ["+", "-"]:
        print("Impacts must be either + or -")
        sys.exit(1)

norm = data.copy()
for i in range(data.shape[1]):
    d = np.sqrt(sum(data.iloc[:, i] ** 2))
    for j in range(data.shape[0]):
        norm.iat[j, i] = data.iat[j, i] / d

for i in range(norm.shape[1]):
    for j in range(norm.shape[0]):
        norm.iat[j, i] = norm.iat[j, i] * weights[i]

ideal_best = []
ideal_worst = []

for i in range(norm.shape[1]):
    if impacts[i] == "+":
        ideal_best.append(norm.iloc[:, i].max())
        ideal_worst.append(norm.iloc[:, i].min())
    else:
        ideal_best.append(norm.iloc[:, i].min())
        ideal_worst.append(norm.iloc[:, i].max())

s_plus = []
s_minus = []

for i in range(norm.shape[0]):
    s1 = 0
    s2 = 0
    for j in range(norm.shape[1]):
        s1 += (norm.iat[i, j] - ideal_best[j]) ** 2
        s2 += (norm.iat[i, j] - ideal_worst[j]) ** 2
    s_plus.append(np.sqrt(s1))
    s_minus.append(np.sqrt(s2))

score = []
for i in range(len(s_plus)):
    score.append(s_minus[i] / (s_plus[i] + s_minus[i]))

df["Topsis Score"] = score
df["Rank"] = df["Topsis Score"].rank(ascending=False, method="max").astype(int)

df.to_csv(out, index=False)
print("TOPSIS result saved to", out)
