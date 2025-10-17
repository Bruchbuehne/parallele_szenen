import itertools
import pandas as pd

# Erstelle ein Dictionary mit allen Szenen und den Leuten darin 
szenen_dict = {
    'Engel&Teufel': ['Kilian', 'Gini'],
    'When to act 1.1': ['Miri', 'Dominic'],
    'When to act 1.2': ['Miri', 'Dominic', 'Anka'],
    'When to act 2': ['Miri', 'Dominic', 'Anka', 'Sarina'],
    'When to act 3': ['Miri', 'Dominic', 'Anka', 'Flynn', 'Jan'],
    'When to act 4.1': ['Miri', 'Dominic', 'Anka', 'Flynn', 'Jan', 'Gini'],
    'When to act 4.2': ['Nicolai'],
    'Wütend': ['Veronika', 'Susanne', 'Jakob'],
    'Aleksei': ['Kilian', 'Susanne', 'Jan', 'Jakob'],
    'Blutrausch': ['Veronika', 'Gabriel', 'Anka', 'Eleni'],
    'Lachs': ['Miri', 'Lio', 'Gabriel'],
    'Pausen': ['Dominic', 'Sarina'],
    'Essenz': ['Ilea'],
    'Was bleibt': ['Anka', 'Lio', 'Kilian'],
    'Diana': ['Susanne', 'Ilea', 'Nicolai', 'Djami'],
    'Midashand': ['Eleni', 'Gabriel', 'Djami'],
    'Goldregen': ['Dominic']
}

alle_personen = set(p for personen in szenen_dict.values() for p in personen)
verwendete_personen = set()
ausgewaehlte_szenen = set()

print("Szenen-Auswahl für parallele Proben")
print("------------------------------------------------------------")

while True:
    # Zeige verfügbare Szenen, die keine Überschneidung haben
    moegliche_szenen = [
        sz for sz, personen in szenen_dict.items()
        if sz not in ausgewaehlte_szenen and verwendete_personen.isdisjoint(personen)
    ]

    if not moegliche_szenen:
        print("\nKeine weiteren Szenen möglich – alle übrigen würden Personen doppelt verwenden.")
        break

    print("\nVerfügbare Szenen:")
    for i, sz in enumerate(moegliche_szenen, 1):
        print(f"{i}. {sz} ({', '.join(szenen_dict[sz])})")

    auswahl = input("\nWelche Szene möchtest du wählen? (Nummer eingeben oder 'q' zum Abbrechen): ").strip()

    if auswahl.lower() == 'q':
        print("\nAbbruch durch Benutzer.")
        break

    if not auswahl.isdigit() or not (1 <= int(auswahl) <= len(moegliche_szenen)):
        print("Ungültige Eingabe, bitte nochmal.")
        continue

    # Szene hinzufügen
    gewaehlte_szene = moegliche_szenen[int(auswahl) - 1]
    ausgewaehlte_szenen.add(gewaehlte_szene)
    verwendete_personen.update(szenen_dict[gewaehlte_szene])

    print(f"\nSzene '{gewaehlte_szene}' gewählt. Aktuell gewählte Szenen:")
    for sz in ausgewaehlte_szenen:
        print(f"  - {sz} ({', '.join(szenen_dict[sz])})")

# Übrige Personen
fehlende_personen = alle_personen - verwendete_personen

# Ergebnis
print("\n------------------------------------")
print("Endergebnis:")
print("Gewählte Szenen:", ", ".join(ausgewaehlte_szenen))
print("Fehlende Personen:", ", ".join(fehlende_personen) if fehlende_personen else "Keine – alle wurden abgedeckt!")
print("------------------------------------")
