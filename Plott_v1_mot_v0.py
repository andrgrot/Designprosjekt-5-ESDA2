import pandas as pd
import matplotlib.pyplot as plt

# Filsti til CSV-filen
file_path = "Andreas v1 mot v0.csv"

# Les inn data, hopp over metadata-linjer som starter med #
df = pd.read_csv(file_path, comment="#", encoding='latin1')

# Anta at kolonnene heter f.eks. "Time", "Channel 1", "Channel 2"
print(df.head())  # sjekk hva de faktisk heter

# Plot begge kanaler
plt.figure(figsize=(10, 6))
plt.plot(df.iloc[:,0], df.iloc[:,1], label="v0 (Inngangssignal)")
plt.plot(df.iloc[:,0], df.iloc[:,2], label="v1 (Utgangssignal)")


plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title("Bufferkrets: v0 og v1")
plt.legend(loc="lower right")  # Endret plassering til nede i høyre hjørne
plt.grid(True)
plt.show()
