
# ======================================================================
# Exercice 1 - Proteger le solde
# ======================================================================
print()
print("=== Exercice 1 - Proteger le solde ===")

class Compte:
    def __init__(self, titulaire, solde_initial):
        self._titulaire = titulaire       # "_" : usage interne
        self._solde = solde_initial

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        self._solde = self._solde + montant

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        if montant > self._solde:
            raise ValueError("solde insuffisant")
        self._solde = self._solde - montant

    def __str__(self):
        return f"Compte ({self._titulaire}) : {self._solde:.2f}"

c = Compte("Amina", 100.0)
c.deposer(50)
c.retirer(30)
print(c)
try:
    c.retirer(500)
except ValueError as e:
    print("Erreur :", e)
try:
    c.deposer(-5)
except ValueError as e:
    print("Erreur :", e)
print(c)

# ======================================================================
# Exercice 2 - Un constructeur qui refuse les comptes invalides
# ======================================================================
print()
print("=== Exercice 2 - Un constructeur qui refuse les comptes invalides ===")

class Compte:
    _prochain_numero = 1                  # attribut de classe : partage

    def __init__(self, titulaire, solde_initial):
        if titulaire.strip() == "":
            raise ValueError("titulaire vide")
        if solde_initial < 0:
            raise ValueError("solde initial negatif")
        self._numero = Compte._prochain_numero
        Compte._prochain_numero += 1
        self._titulaire = titulaire       # "_" : usage interne
        self._solde = solde_initial

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        self._solde = self._solde + montant

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        if montant > self._solde:
            raise ValueError("solde insuffisant")
        self._solde = self._solde - montant

    def __str__(self):
        return f"Compte {self._numero} ({self._titulaire}) : {self._solde:.2f}"


a = Compte("Amina", 100.0)
try:
    Compte("   ", 50.0)
except ValueError as e:
    print("Erreur :", e)
try:
    Compte("Karim", -10.0)
except ValueError as e:
    print("Erreur :", e)
b = Compte("Youssef", 250.0)
print(a)
print(b)


# ======================================================================
# Exercice 3 - Lire sans pouvoir modifier
# ======================================================================
print()
print("=== Exercice 3 - Lire sans pouvoir modifier ===")

class Compte:
    _prochain_numero = 1                  # attribut de classe : partage

    def __init__(self, titulaire, solde_initial):
        if titulaire.strip() == "":
            raise ValueError("titulaire vide")
        if solde_initial < 0:
            raise ValueError("solde initial negatif")
        self._numero = Compte._prochain_numero
        Compte._prochain_numero += 1
        self._titulaire = titulaire       # "_" : usage interne
        self._solde = solde_initial

    @property
    def numero(self):
        return self._numero

    @property
    def titulaire(self):
        return self._titulaire

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        self._solde = self._solde + montant

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        if montant > self._solde:
            raise ValueError("solde insuffisant")
        self._solde = self._solde - montant

    def __str__(self):
        return f"Compte {self._numero} ({self._titulaire}) : {self._solde:.2f}"


c = Compte("Amina", 100.0)
c.deposer(20)
print("Numero :", c.numero)
print("Titulaire :", c.titulaire)
print(f"Solde : {c.solde:.2f}")

# ======================================================================
# Exercice 4 - Membres de classe : compter et fabriquer des comptes
# ======================================================================
print()
print("=== Exercice 4 - Membres de classe : compter et fabriquer des comptes ===")

class Compte:
    _prochain_numero = 1                  # attribut de classe : partage

    def __init__(self, titulaire, solde_initial):
        if titulaire.strip() == "":
            raise ValueError("titulaire vide")
        if solde_initial < 0:
            raise ValueError("solde initial negatif")
        self._numero = Compte._prochain_numero
        Compte._prochain_numero += 1
        self._titulaire = titulaire       # "_" : usage interne
        self._solde = solde_initial

    @classmethod
    def nombre_comptes(cls):
        return cls._prochain_numero - 1

    @classmethod
    def depuis_ligne_csv(cls, ligne):
        champs = ligne.split(";")
        if len(champs) != 2:
            raise ValueError("ligne mal formee : " + ligne)
        try:
            solde = float(champs[1])
        except ValueError:
            raise ValueError("solde non numerique : " + champs[1]) from None
        return cls(champs[0], solde)

    @property
    def numero(self):
        return self._numero

    @property
    def titulaire(self):
        return self._titulaire

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        self._solde = self._solde + montant

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        if montant > self._solde:
            raise ValueError("solde insuffisant")
        self._solde = self._solde - montant

    def __str__(self):
        return f"Compte {self._numero} ({self._titulaire}) : {self._solde:.2f}"


for ligne in ["Youssef;250.0", "Salma;80.5", "Karim;abc", "Hind"]:
    try:
        print(Compte.depuis_ligne_csv(ligne))
    except ValueError as e:
        print("Rejet :", e)
print("Comptes crees :", Compte.nombre_comptes())


# ======================================================================
# Exercice 5 - Meme objet ou meme compte ?
# ======================================================================
print()
print("=== Exercice 5 - Meme objet ou meme compte ? ===")

class Compte:
    _prochain_numero = 1                  # attribut de classe : partage

    def __init__(self, titulaire, solde_initial):
        if titulaire.strip() == "":
            raise ValueError("titulaire vide")
        if solde_initial < 0:
            raise ValueError("solde initial negatif")
        self._numero = Compte._prochain_numero
        Compte._prochain_numero += 1
        self._titulaire = titulaire       # "_" : usage interne
        self._solde = solde_initial

    @classmethod
    def nombre_comptes(cls):
        return cls._prochain_numero - 1

    @classmethod
    def depuis_ligne_csv(cls, ligne):
        champs = ligne.split(";")
        if len(champs) != 2:
            raise ValueError("ligne mal formee : " + ligne)
        try:
            solde = float(champs[1])
        except ValueError:
            raise ValueError("solde non numerique : " + champs[1]) from None
        return cls(champs[0], solde)

    @property
    def numero(self):
        return self._numero

    @property
    def titulaire(self):
        return self._titulaire

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        self._solde = self._solde + montant

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        if montant > self._solde:
            raise ValueError("solde insuffisant")
        self._solde = self._solde - montant

    def copie_de_sauvegarde(self):
        import copy
        return copy.copy(self)            # nouvel objet, meme numero

    def __eq__(self, autre):
        return isinstance(autre, Compte) and self._numero == autre._numero

    def __hash__(self):
        return hash(self._numero)

    def __str__(self):
        return f"Compte {self._numero} ({self._titulaire}) : {self._solde:.2f}"


def oui(b):
    return "oui" if b else "non"

a = Compte("Amina", 100.0)
b = a                                     # alias : meme objet
c = Compte("Amina", 100.0)                # autre compte, meme titulaire
d = a.copie_de_sauvegarde()               # autre objet, meme numero
print(f"a/b : meme objet = {oui(a is b)}, egaux = {oui(a == b)}")
print(f"a/c : meme objet = {oui(a is c)}, egaux = {oui(a == c)}")
print(f"a/d : meme objet = {oui(a is d)}, egaux = {oui(a == d)}")
print(f"Ensemble {{a, b, c, d}} : {len({a, b, c, d})} comptes")

# ======================================================================
# Exercice 6 - Tester le compte sans bibliotheque
# ======================================================================
print()
print("=== Exercice 6 - Tester le compte sans bibliotheque ===")

class Compte:
    _prochain_numero = 1                  # attribut de classe : partage

    def __init__(self, titulaire, solde_initial):
        if titulaire.strip() == "":
            raise ValueError("titulaire vide")
        if solde_initial < 0:
            raise ValueError("solde initial negatif")
        self._numero = Compte._prochain_numero
        Compte._prochain_numero += 1
        self._titulaire = titulaire       # "_" : usage interne
        self._solde = solde_initial

    @classmethod
    def nombre_comptes(cls):
        return cls._prochain_numero - 1

    @classmethod
    def depuis_ligne_csv(cls, ligne):
        champs = ligne.split(";")
        if len(champs) != 2:
            raise ValueError("ligne mal formee : " + ligne)
        try:
            solde = float(champs[1])
        except ValueError:
            raise ValueError("solde non numerique : " + champs[1]) from None
        return cls(champs[0], solde)

    @property
    def numero(self):
        return self._numero

    @property
    def titulaire(self):
        return self._titulaire

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        self._solde = self._solde + montant

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("montant invalide")
        if montant > self._solde:
            raise ValueError("solde insuffisant")
        self._solde = self._solde - montant

    def copie_de_sauvegarde(self):
        import copy
        return copy.copy(self)            # nouvel objet, meme numero

    def __eq__(self, autre):
        return isinstance(autre, Compte) and self._numero == autre._numero

    def __hash__(self):
        return hash(self._numero)

    def __str__(self):
        return f"Compte {self._numero} ({self._titulaire}) : {self._solde:.2f}"


reussis, echecs = 0, 0

def verifier(nom, condition):
    global reussis, echecs
    if condition:
        reussis += 1
    else:
        echecs += 1
        print("ECHEC :", nom)

def doit_echouer(nom, operation):
    global reussis, echecs
    try:
        operation()
    except ValueError:
        reussis += 1
    else:
        echecs += 1
        print("ECHEC :", nom, "(ne devait pas reussir)")

c = Compte("Amina", 100.0)
c.deposer(50)
verifier("depot valide", c.solde == 150.0)
c.retirer(150)
verifier("retrait de tout le solde", c.solde == 0.0)
c.deposer(100)
doit_echouer("depot nul", lambda: c.deposer(0))
doit_echouer("depot negatif", lambda: c.deposer(-5))
doit_echouer("retrait nul", lambda: c.retirer(0))
doit_echouer("retrait trop grand", lambda: c.retirer(500))
verifier("solde inchange apres les refus", c.solde == 100.0)
doit_echouer("titulaire vide", lambda: Compte("", 10))
doit_echouer("titulaire espaces", lambda: Compte("   ", 10))
doit_echouer("solde initial negatif", lambda: Compte("Karim", -1))
print(f"{reussis} tests reussis, {echecs} echec(s)")

