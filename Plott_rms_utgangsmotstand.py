import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "Andreas rms utgangsmotstand.csv"

df = pd.read_csv(file_path, comment="#", encoding='latin1')

print(df.head())

tid = df.iloc[:, 0]
signal1 = df.iloc[:, 1]
signal2 = df.iloc[:, 2]

rms1 = np.sqrt(np.mean(signal1**2))
rms2 = np.sqrt(np.mean(signal2**2))

plt.figure(figsize=(12, 7))
plt.plot(tid, signal1, label="Inngangssignal V_s")
plt.plot(tid, signal2, label="Utgangssignal V_2")

rms_text = f"RMS Inngangssignal: {rms1:.3f} V\nRMS Utgangssignal: {rms2:.3f} V"
rms_text = f"RMS Inngangssignal: {rms1:.3f} V\nRMS Utgangssignal: {rms2:.3f} V"
plt.gcf().text(0.7, 0.15, rms_text, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title("RMS Inngangsmotstand")
plt.legend(loc="best")
plt.grid(True)

plt.show()
