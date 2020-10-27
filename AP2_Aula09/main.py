from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

p1 = Pessoa(1, "Maria", "Praça Teste", "(99) 99999-9999")
f = Fisica(1, p1.nome, p1._endereco, p1.getFone, "421.361.950-85", 35, 74.7, 1.77)

p2 = Pessoa(2, "José Adv", "Rua Teste 2", "(00) 00000-0000")
j = Juridica(2, p2.nome, p2._endereco, p2.getFone, "36.605.238/0001-98", "12345", 22)

p1.imprimeNome()
print(p1.getFone())

f.imprimeCPF()
print(f.getIMC())

p2.imprimeNome()
print(p2.getFone())

j.imprimeCNPJ()
j.getNF()
