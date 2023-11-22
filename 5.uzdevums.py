import datetime as dt # importē bibliotēku

h = dt.datetime.now().hour # iegūstam pašreizējo stundu

if 0 <= h < 12:          # kods, lai izvēlētos pareizo tekstu
    teksts = "Labrīt!"
elif 12 <= h < 18:
    teksts = "Labdien!"
else:
    teksts = "Labvakar!"

print(teksts) # izvada atbilstošo tekstu
