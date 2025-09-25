def verifier_mot_de_passe(mot_de_passe: str) -> bool:
    """
    Vérifie si un mot de passe est fort.
    Règles :
    - Au moins 8 caractères
    - Au moins une lettre majuscule
    - Au moins un chiffre

    :param mot_de_passe: le mot de passe à vérifier
    :return: True si le mot de passe est fort, False sinon
    """
    # Vérification longueur
    if len(mot_de_passe) < 8:
        print("Erreur : le mot de passe doit contenir au moins 8 caractères.")
        return False

    # Vérification majuscule
    contient_majuscule = False
    for caractere in mot_de_passe:
        if caractere.isupper():
            contient_majuscule = True
            break
    if not contient_majuscule:
        print("Erreur : le mot de passe doit contenir au moins une lettre majuscule.")
        return False

    # Vérification chiffre
    contient_chiffre = False
    for caractere in mot_de_passe:
        if caractere.isdigit():
            contient_chiffre = True
            break
    if not contient_chiffre:
        print("Erreur : le mot de passe doit contenir au moins un chiffre.")
        return False

    return True



if __name__ == "__main__":
    pwd = input("Entrez un mot de passe à tester : ")
    if verifier_mot_de_passe(pwd):
        print("Mot de passe fort")
    else:
        print("Mot de passe faible")
