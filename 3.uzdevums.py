# 3.uzdevums
with open ('jebkas.csv', 'rb') as fails:
    fails1 = fails.read()

saraksts =  [fails1] # parveido par masivu
garums =  len(saraksts)
print(garums) # masiva garums

print(saraksts[0]) # pirma elementa saturs
print(saraksts[:4]) # :4 jo sakas ar 0 
