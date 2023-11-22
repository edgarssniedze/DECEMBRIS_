# 4.uzdevums
vardnica = {}
with open("kautkas.json",'rb') as fails:
      for linija in fails:
            (a, b) = linija.split()
            vardnica[int(a)] = b