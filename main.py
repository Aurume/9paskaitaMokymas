# Pagrindiniame projekto kataloge sukurti failą main.py +
# Faile main.py importuoti PythonKursas modulį (failą) +

from modules.kursas import Kursas
from modules.python_kursas import PythonKursas

# inicijuoti Kursas objektą su norimomis savybėmis+
# Faile main.py inicijuoti PythonKursas objektą su norimomis savybėmis+
# Paleisti abiejų objektų metodą destyti()+

zmogus1 = Kursas("Java", "Gintautas", "6 mėnesiai")
zmogus1.destyti()
print("------------------------------")
zmogus2 = PythonKursas("Python", "Donatas", "4 mėnesiai")
zmogus2.destyti()