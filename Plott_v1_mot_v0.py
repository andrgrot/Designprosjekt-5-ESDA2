import pandas as pd
import matplotlib.pyplot as plt

file_path = "Andreas v1 mot v0.csv"

df = pd.read_csv(file_path, comment="#", encoding='latin1')

print(df.head())  

plt.figure(figsize=(10, 6))
plt.plot(df.iloc[:,0], df.iloc[:,1], label="v0 (Inngangssignal)")
plt.plot(df.iloc[:,0], df.iloc[:,2], label="v1 (Utgangssignal)")

plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title("Bufferkrets: v0 og v1")
plt.legend(loc="lower right") 
plt.grid(True)
plt.show()

