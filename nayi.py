import random as random

pasos_pies = [1,2,3,4,5,6,7,8,9,10,11,12,13]
pasos_caderas = [14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
pasos_torso = [20,24,25,27,28,30]
pasos_cabeza = [31,20,24,25,30]

var = True
while var:
    print('Indica las combinaciones:')
    print('A: pies, caderas, torso, cabeza')
    print('B: pies, caderas, torso')
    print('C: pies, caderas')

    pasos_nayi = input('indica la combinación que deseas: ')
    devolver = []
    if pasos_nayi == 'A':
        paso1 = random.choice(pasos_pies)
        devolver.append((paso1, 'pies'))
        paso2 = random.choice(pasos_caderas)
        devolver.append((paso2, 'caderas'))
        paso3 = random.choice(pasos_torso)
        devolver.append((paso3, 'torso'))
        paso4 = random.choice(pasos_cabeza)
        devolver.append((paso4, 'cabeza'))
    elif pasos_nayi == 'B':
        paso1 = random.choice(pasos_pies)
        devolver.append((paso1, 'pies'))
        paso2 = random.choice(pasos_caderas)
        devolver.append((paso2, 'caderas'))
        paso3 = random.choice(pasos_torso)
        devolver.append((paso3, 'torso'))
    elif pasos_nayi == 'C':
        paso1 = random.choice(pasos_pies)
        devolver.append((paso1, 'pies'))
        paso2 = random.choice(pasos_caderas)
        devolver.append((paso2, 'caderas'))

    print(f'sus pasos son {devolver}')
    continuar = int(input('desea otra combinación?: 1 para si, 0 para no: '))

    if continuar == 1:
        var = True
    else:
        var = False


    



