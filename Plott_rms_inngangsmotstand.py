import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Filsti til CSV-filen
file_path = "Andreas rms inngansmotstand.csv"

# Les inn data, hopp over metadata-linjer som starter med #
df = pd.read_csv(file_path, comment="#", encoding='latin1')

# Sjekk kolonnenavn og data
print(df.head())

# Anta at første kolonne er tid og de to neste er signaler
tid = df.iloc[:, 0]
signal1 = df.iloc[:, 1]
signal2 = df.iloc[:, 2]

# Beregn RMS for begge signaler
rms1 = np.sqrt(np.mean(signal1**2))
rms2 = np.sqrt(np.mean(signal2**2))

# Lag plott
plt.figure(figsize=(12, 7))
plt.plot(tid, signal1, label="Inngangssignal V_0")
plt.plot(tid, signal2, label="Utgangssignal V_1")

# Vis RMS-verdier i plottet
rms_text = f"RMS Inngangssignal: {rms1:.3f} V\nRMS Utgangssignal: {rms2:.3f} V"
plt.gcf().text(0.7, 0.15, rms_text, fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title("RMS Inngangsmotstand")
plt.legend(loc="best")
plt.grid(True)
plt.show()