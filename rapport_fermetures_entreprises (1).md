# Pourquoi un grand nombre d'entreprises ferment-elles au Maroc ?

**Cours de Data Science — ENCG Settat**

**Auteure : Asmaa Makdoud**

## 1. Introduction

Depuis 2022, la presse économique marocaine relaie régulièrement des chiffres inquiétants
sur les défaillances d'entreprises. Ce rapport cherche à quantifier ce phénomène et à en
identifier les principales causes, à partir de données publiées par des organismes
spécialisés (Allianz Trade, Euler Hermes) et relayées par la presse économique nationale.

## 2. Méthodologie

Les données utilisées portent sur la **variation annuelle en pourcentage du nombre de
défaillances d'entreprises au Maroc** (entreprises entrées en procédure de liquidation
judiciaire ou ayant cessé leur activité de manière définitive), sur la période 2022-2025.
Ces chiffres proviennent des rapports annuels d'Allianz Trade sur les défaillances
d'entreprises dans le monde, repris par la presse économique marocaine (voir sources en
section 5). Le script `analyse_fermetures_entreprises.py` importe ce dataset
(`defaillances_entreprises_maroc.csv`) et génère le graphique en barres présenté ci-dessous.

## 3. Résultats

Le graphique (`evolution_defaillances_entreprises.png`) montre une hausse continue des
défaillances d'entreprises au Maroc sur trois années consécutives, suivie d'un premier
recul :

| Année | Variation | Commentaire |
|---|---|---|
| 2022 | +17 % | Sortie de la période post-Covid |
| 2023 | +15 % | Retards de paiement, pression fiscale |
| 2024 | +13 % | Environ 16 100 défaillances estimées |
| 2025 | -3,3 % | Première baisse depuis la période Covid |

Ce niveau reste, en 2024, plus de deux fois supérieur à la moyenne observée entre 2016 et
2019, avant la pandémie.

## 4. Analyse : pourquoi tant d'entreprises ferment-elles ?

Plusieurs facteurs, convergents sur les principales sources consultées, expliquent cette
dynamique :

- **Allongement des délais de paiement** entre entreprises, qui fragilise la trésorerie des
  PME/TPME, en particulier lorsqu'elles sont en aval de grands donneurs d'ordre.
- **Hausse des coûts de financement** : le resserrement monétaire de Bank Al-Maghrib entre
  2022 et 2023, destiné à contenir l'inflation, a renchéri l'accès au crédit bancaire pour
  les entreprises déjà fragilisées.
- **Inflation et hausse des coûts de production**, portée par le renchérissement des
  matières premières et de l'énergie après le déclenchement de la guerre en Ukraine.
- **Sécheresse persistante** : plusieurs campagnes agricoles consécutives dégradées ont
  pesé sur l'agriculture et les activités qui en dépendent (commerce de proximité,
  agroalimentaire).
- **Pression fiscale croissante** et durcissement de l'accès au crédit bancaire pour les
  petites structures jugées plus risquées.
- **Concurrence structurelle** du commerce moderne (grandes surfaces) au détriment du petit
  commerce de proximité.

Le repli de 2025 est attribué en partie à l'entrée en application de la loi sur les délais
de paiement, qui commencerait à améliorer la trésorerie des entreprises. Les analystes
restent toutefois prudents : ce recul est qualifié de "signal encourageant" plutôt que de
retournement structurel confirmé, les entreprises les plus vulnérables ayant déjà quitté
le marché les années précédentes.

Sur le plan géographique, le phénomène reste très concentré : en 2025, la région
Casablanca-Settat concentre à elle seule environ 29 % des défaillances nationales, suivie
de Rabat-Salé-Kénitra (15 %), Fès-Meknès (12 %) et Tanger-Tétouan-Al Hoceima (11 %) — soit
près des deux tiers du total national dans quatre régions.

## 5. Limites de l'analyse

- Les données utilisées sont des variations en pourcentage relayées par la presse et non
  les séries brutes complètes publiées par Bank Al-Maghrib ou le Conseil National des
  Greffiers des Tribunaux de Commerce marocain ; elles suffisent à dégager une tendance
  mais gagneraient à être recoupées avec une source officielle primaire.
- La notion de "défaillance" (procédure de liquidation) diffère de la "radiation" du
  registre du commerce suivie par l'OMPIC : les deux indicateurs mesurent des réalités
  proches mais non identiques.
- L'analyse est macroéconomique ; elle n'isole pas statistiquement le poids relatif de
  chaque facteur cité (délais de paiement, taux d'intérêt, inflation, etc.).

## 6. Conclusion

La fermeture d'un grand nombre d'entreprises au Maroc entre 2022 et 2024 résulte d'un
cumul de chocs (inflation, resserrement monétaire, retards de paiement, sécheresse) qui a
particulièrement fragilisé les PME/TPME. Le repli observé en 2025, encore modeste,
suggère un début de normalisation, porté notamment par le nouveau cadre légal sur les
délais de paiement — sans que la tendance de fond soit encore inversée.

## 7. Sources

- Allianz Trade / Hespress — *Défaillances d'entreprises au Maroc, des prévisions
  inquiétantes pour 2024 et 2025* : https://fr.hespress.com/391179-defaillances-dentreprises-au-maroc-des-previsions-inquietantes-pour-2024-et-2025.html
- Finances News Hebdo — *Défaillances d'entreprises : baisse des faillites de 3,3 % en
  2025, une première depuis la période Covid* : https://fnh.ma/article/actualite-economique/defaillances-entreprises-baisse-faillites
- Finances News Hebdo — *Un signal encourageant, mais pas encore un retournement
  structurel* : https://www.fnh.ma/article/actualite-economique/defaillances-entreprisess-signal-retournement
