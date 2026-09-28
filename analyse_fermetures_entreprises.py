"""
Analyse : fermetures / defaillances d'entreprises au Maroc
Cours de Data Science - ENCG Settat

Ce script importe le dataset (CSV) contenant la variation annuelle
du nombre de defaillances d'entreprises au Maroc, puis genere un
graphique en barres illustrant l'evolution de cette variation.

Sources des donnees : voir la colonne 'source' du fichier CSV.
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Import des donnees
df = pd.read_csv("defaillances_entreprises_maroc.csv")
print(df)

# 2. Preparation du graphique
couleurs = ["tomato" if v > 0 else "seagreen" for v in df["variation_defaillances_pct"]]

fig, ax = plt.subplots(figsize=(8, 5))
barres = ax.bar(df["annee"].astype(str), df["variation_defaillances_pct"], color=couleurs)

# Ligne de reference a 0%
ax.axhline(0, color="black", linewidth=0.8)

# Etiquettes de valeur au-dessus/en-dessous de chaque barre
for barre, valeur in zip(barres, df["variation_defaillances_pct"]):
    offset = 0.5 if valeur >= 0 else -1.2
    ax.text(barre.get_x() + barre.get_width() / 2, valeur + offset,
            f"{valeur:+.1f}%", ha="center", fontweight="bold")

ax.set_title("Evolution annuelle des defaillances d'entreprises au Maroc")
ax.set_xlabel("Annee")
ax.set_ylabel("Variation par rapport a l'annee precedente (%)")
ax.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("evolution_defaillances_entreprises.png", dpi=150)
print("Graphique enregistre : evolution_defaillances_entreprises.png")
