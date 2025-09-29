def demander_nombre_pair():
    while True:
        try:
            n = int(input("Entrez un nombre pair supérieur ou égal à 0 : "))
            if n >= 0 and n % 2 == 0:
                return n
            else:
                print("Erreur : le nombre doit être pair et >= 0.")
        except ValueError:
            print("Erreur : vous devez entrer un nombre valide.")

# Exemple d’utilisation
nombre = demander_nombre_pair()
print(f"Vous avez entré : {nombre}")


# Définition des groupes
groupe_A = [1, 2, 3, 4]
groupe_B = [5, 6, 7, 8]

print("=== Avec FOR ===")
for a in groupe_A:
    for b in groupe_B:
        print(f"{a}-{b}")

print("\n=== Avec WHILE ===")
i = 0
while i < len(groupe_A):
    j = 0
    while j < len(groupe_B):
        print(f"{groupe_A[i]}-{groupe_B[j]}")
        j += 1
    i += 1


# Liste des mois (index 0 = janvier, index 1 = février, etc.)
ls_mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "september", "octobre", "november", "december"]
jours_par_mois = [
    "31",
    "28 ou 29",  # Février
    "31",
    "30",
    "31",
    "30",
    "31",
    "31",
    "30",
    "31",
    "30",
    "31"
]

for i in range(12):
    # 02d afficher sur 2 chiffres (ChatGPT)
    print(f"Le mois {i+1:02d} {ls_mois[i]} possède {jours_par_mois[i]} jours.")
