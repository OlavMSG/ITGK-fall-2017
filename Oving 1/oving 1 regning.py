Stoff=input('Si et stoff du er i besittelse av: ')
print('Hva er molvekt i gram for ',Stoff,end="")
x=float(input(':'))
print('Hvor mange gram ',Stoff,' har du?',end="")
y=float(input(''))
A=6.0022e23
svar=y/x*A
print('Du har',svar,'molekyler av',Stoff)

