import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Filsti til CSV-filen
file_path = "Andreas network.csv"

# Les inn data, hopp over metadata-linjer som starter med #
df = pd.read_csv(file_path, comment="#", encoding='latin1')

# Ekstraher data
freq = df.iloc[:, 0]
mag_db = df.iloc[:, 2]  # Channel 2 Magnitude (dB)

# Finn maksimal verdi og -3 dB punkt
max_db = mag_db.max()
minus3db = max_db - 3

# Finn indeksen til maksimal verdi
idx_max = mag_db.idxmax()
freq_max = freq.iloc[idx_max]

# Finn alle punkter hvor magnitude er <= -3 dB fra topp
idx_3db = np.where(mag_db <= minus3db)[0]

# Finn laveste og høyeste frekvens hvor -3 dB-kriteriet er møtt etter toppunktet
idx_3db_lower = idx_3db[idx_3db < idx_max]
idx_3db_upper = idx_3db[idx_3db > idx_max]

freq_3db_lower = freq.iloc[idx_3db_lower[-1]] if len(idx_3db_lower) > 0 else None
mag_3db_lower = mag_db.iloc[idx_3db_lower[-1]] if len(idx_3db_lower) > 0 else None

freq_3db_upper = freq.iloc[idx_3db_upper[0]] if len(idx_3db_upper) > 0 else None
mag_3db_upper = mag_db.iloc[idx_3db_upper[0]] if len(idx_3db_upper) > 0 else None

plt.figure(figsize=(10, 6))
plt.semilogx(freq, mag_db, label="Utgangssignal (dB)")
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Magnitude [dB]")
plt.title("Bodeplot")


# Marker -3 dB nivå
plt.axhline(minus3db, color='red', linestyle='--', label="-3 dB nivå")

# Marker nedre og øvre -3 dB grense
if freq_3db_lower is not None:
    plt.axvline(freq_3db_lower, color='green', linestyle='--', label=f"Nedre -3 dB: {freq_3db_lower:.0f} Hz")
    plt.scatter([freq_3db_lower], [mag_3db_lower], color='green')
    plt.text(freq_3db_lower, mag_3db_lower, f"  {freq_3db_lower:.0f} Hz", va='top', ha='left', color='green')
if freq_3db_upper is not None:
    plt.axvline(freq_3db_upper, color='orange', linestyle='--', label=f"Øvre -3 dB: {freq_3db_upper:.0f} Hz")
    plt.scatter([freq_3db_upper], [mag_3db_upper], color='orange')
    plt.text(freq_3db_upper, mag_3db_upper, f"  {freq_3db_upper:.0f} Hz", va='bottom', ha='left', color='orange')

plt.legend(loc="best")
plt.grid(True, which="both", ls=":")
plt.tight_layout()
plt.show()