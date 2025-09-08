import pandas as pd
import matplotlib.pyplot as plt

file_path = "Andreas økende v_0 amplitude -1.3.csv"

df = pd.read_csv(file_path, comment="#", encoding='latin1')

print(df.head())

tid = df.iloc[:, 0]
v0 = df.iloc[:, 1]
v1 = df.iloc[:, 2]

plt.figure(figsize=(12, 7))
plt.plot(tid, v0, label="Inngangssignal V₀")
plt.plot(tid, v1, label="Utgangssignal V₁")

plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title("Økende V₀ amplitude (1.3 V)")
plt.legend(loc="upper left", fontsize=12, framealpha=0.9)
plt.grid(True)
plt.tight_layout()

plt.show()
