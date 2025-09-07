import pandas as pd
import matplotlib.pyplot as plt

# Filsti til CSV-filen
file_path = "Andreas v2 mot v0.csv"

# Les inn data, hopp over metadata-linjer som starter med #
df = pd.read_csv(file_path, comment="#", encoding='latin1')

# Anta at kolonnene heter f.eks. "Time", "Channel 1", "Channel 2"
print(df.head())  # sjekk hva de faktisk heter

# Plot begge kanaler
plt.figure(figsize=(10, 6))
plt.plot(df.iloc[:,0], df.iloc[:,1], label="v0 (Inngangssignal)")
plt.plot(df.iloc[:,0], df.iloc[:,2], label="v2 (Utgangssignal)")

# Beregn og vis forskjell i amplitude
v0_amplitude = df.iloc[:,1].max() - df.iloc[:,1].min()
v2_amplitude = df.iloc[:,2].max() - df.iloc[:,2].min()
amplitude_diff = abs(v0_amplitude - v2_amplitude)

# Legg til tekstboks med amplitudeforskjell
amplitude_text = (
    f"v0 amplitude: {v0_amplitude:.2f} V\n"
    f"v2 amplitude: {v2_amplitude:.2f} V\n"
    f"Forskjell: {amplitude_diff:.2f} V"
)
plt.gcf().text(0.7, 0.15, amplitude_text, fontsize=10, bbox=dict(facecolor='white', alpha=0.7))


plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title("Bufferkrets: v0 og v2")
plt.legend(loc="lower right")  # Endret plassering til nede i høyre hjørne
plt.grid(True)
plt.show()
