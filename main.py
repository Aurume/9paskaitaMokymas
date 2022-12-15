# Pagrindiniame projekto kataloge sukurti failą main.py +
# Faile main.py importuoti PythonKursas modulį (failą) +

from modules.kursas import Kursas
from modules.python_kursas import PythonKursas

# inicijuoti Kursas objektą su norimomis savybėmis+
# Faile main.py inicijuoti PythonKursas objektą su norimomis savybėmis+
# Paleisti abiejų objektų metodą destyti()+

mano_objektas = Kursas("Java", "Gintautas", "6 mėnesiai")
mano_objektas.destyti()
print("------------------------------")
kitas_objektas = PythonKursas("Python", "Donatas", "4 mėnesiai")
kitas_objektas.destyti()