import numpy as np
#Δ
"""
Definere antall variabler med usikkerhet
skrive utrykk
"""
def gjelendeSiffer(num):
    num1 = num.replace('.','')
    num1 = num1.lstrip('0')
    return len(num1)

#helpAns = input('Do you need help? [y/n] ')
antallVariabler = int(input('Hvor mange variabler er det? '))

variables_rel = {}
variables_abs = {}
variables_maal = {}

for i in range(antallVariabler):
    var = input('Skriv variabelnavn: ')
    var = var.replace(' ', '')
    usikkerhet_maal = float(input(f'Måling på {var}: '))
    ans = input('Har du relativ eller absolutt usikkerhet? [r/a] ')
    if ans == 'r':
        usikkerhet_rel = float(input(f'Relativ usikkerhet for {var}: '))
        usikkerhet_abs = usikkerhet_rel * usikkerhet_maal
    if ans == 'a':
        usikkerhet_abs = float(input(f'Absolutt usikkerhet for {var}: '))
        variables_abs[var] = usikkerhet_abs
        usikkerhet_rel = usikkerhet_abs / usikkerhet_maal
    variables_abs[var] = usikkerhet_abs
    variables_rel[var] = usikkerhet_rel
    variables_maal[var] = usikkerhet_maal



utrykk = input('''Skriv utrykket:

''')
utrykk = utrykk.replace(' ', '')
utrykk = utrykk.replace('/', '*')
utrykk_ledd = utrykk.split('+')
produkter = []

for i in range(len(utrykk_ledd)-1):
    utrykk_ledd[i] = utrykk_ledd[i].split('*')

for ledd in utrykk_ledd:
    for produkt in ledd:
        exp = produkt.find('^')
        if not exp == -1:
            l = produkt.split('^')
            var = l[0]
            expNum = int(l[1])
            variables_rel[var] = variables_rel[var]*expNum
            variables_maal[var] = variables_maal[var]**expNum

ledd_maal_list = []
ledd_usikkerhet_rel = []
for ledd in utrykk_ledd:
    ledd_maal = 0
    ledd_usikkerhet = 0
    for produkt in ledd:
        l = produkt.split('^')
        var = l[0]
        ledd_maal += variables_maal[var]
        ledd_usikkerhet += variables_rel[var]
    ledd_maal_list.append(ledd_maal)
    ledd_usikkerhet_rel.append(ledd_usikkerhet)

usikkerhet = 0
maal = 0
for i in range(len(ledd_usikkerhet_rel)-1):
    usikkerhet += ledd_usikkerhet_rel[i] * ledd_maal_list[i]
    maal += ledd_maal_list[i]

usikkerhet = round(usikkerhet, - int(np.floor(np.log10(usikkerhet))))
maal = round(maal, - int(np.floor(np.log10(usikkerhet))))
if usikkerhet == int(usikkerhet):
    usikkerhet = int(usikkerhet)

print('')
print(f'{maal} ± {usikkerhet}')
