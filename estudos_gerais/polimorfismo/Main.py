from ClasseUtilitaria import Utilitaria
from ClasseConcreta1 import ClasseConcreta1
from ClasseConcreta2 import ClasseConcreta2
from ClasseHerdaAbstrata import HerdaAbstrata

Utilitaria.metodoUtilitario(ClasseConcreta1)
print()
Utilitaria.metodoUtilitario(ClasseConcreta2)
print()
print(HerdaAbstrata.metodoAbstratoSoma())
HerdaAbstrata.metodoAbstratoImprime()