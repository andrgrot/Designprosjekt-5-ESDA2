import pandas as pd
import matplotlib.pyplot as plt

file_path = "Andreas v1 mot v2.csv"

df = pd.read_csv(file_path, comment="#", encoding='latin1')

print(df.head()) 

plt.figure(figsize=(10, 6))
plt.plot(df.iloc[:,0], df.iloc[:,1], label="v2 (Utgangssignal)")
plt.plot(df.iloc[:,0], df.iloc[:,2], label="v1 (Inngangssignal)")

v0_amplitude = df.iloc[:,1].max() - df.iloc[:,1].min()
v2_amplitude = df.iloc[:,2].max() - df.iloc[:,2].min()
amplitude_diff = abs(v0_amplitude - v2_amplitude)

amplitude_text = (
    f"v0 amplitude: {v0_amplitude:.2f} V\n"
    f"v2 amplitude: {v2_amplitude:.2f} V\n"
    f"Forskjell: {amplitude_diff:.2f} V"
)
plt.gcf().text(0.7, 0.15, amplitude_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.7))

plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title("Bufferkrets: v1 og v2")
plt.legend(loc="lower right")  # Endret plassering til nede i høyre hjørne
plt.grid(True)
plt.show()

