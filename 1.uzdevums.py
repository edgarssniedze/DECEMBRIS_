# 1.uzdevums
ievade = input("Ievadi datnes nosaukumu:") # Ievades lauks
garums = int(input("Ievadi tavuprāt garumu:"))

if garums > 0:
  try:                    # parbauda vai datne pastav
    with open(ievade,'rb') as fails:
      fails1 = fails.read()

    print(len(fails1))

    print(fails1[:10])
    print(fails1[:1],fails1[-1:])

    if garums == len(fails1):
        print('Sakrīt')
        print(fails1)
    else:
        print(fails1[:garums])
  except FileNotFoundError:
    print("Datne nav atrasta")

else:
  print("garumam jābūt pozitīvam skaitlim")