#Convertendo medidas

print('{:=^30}'.format('Convertendo M em CM'))
metros = float(input('Qual a medida em Metros? '))

cm = metros*100
mm = metros*1000
dm = metros*10
km = metros/1000

print('\n{:=^20}'.format('CONCLUSÃO'))
print('{:.2f}m >>> {:.2f}mm'.format(metros, mm))
print('{:.2f}m >>> {:.2f}cm'.format(metros, cm))
print('{:.2f}m >>> {:.2f}dm'.format(metros, dm))
print('{:.2f}m >>> {:.2f}km'.format(metros, km))