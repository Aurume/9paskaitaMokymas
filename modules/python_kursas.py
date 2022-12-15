from modules.kursas import Kursas


# Faile python_kursas.py sukurti objekto klasę PythonKursas+
# kuri paveldėtų viską iš klasės Kursas+
# bei perrašytų metodą destyti() taip, kad jis spausdintų „Vyksta programavimas!“+

class PythonKursas(Kursas):
    def destyti(self):
        print("Vyksta programavimas!")
