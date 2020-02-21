print('Her viser jeg konvertering mellom heltll og flytall')
x=float(input('Skriv inn et flyttall (desimaltall):'))
print('Konvert med int() ble tallet',int(x))
print('Heltallet konvertert tilbake til flyttall:',float(int(x)))
print('Det opprinnelige flytallet avrundet med round():',round(x))
print('Jeg kan også bruke round() til å avrunde til et bestemt antall desimaler')
print('F.eks blir round(',x,',2) til',round(x,2),'da jeg ber om 2 desimaler')
y=int(input('Hvor mange desimaler ønsker du? '))
print('Opprinnelig flyttall med',y,'desimaler:',round(x,y))



