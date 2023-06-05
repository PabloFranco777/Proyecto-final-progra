import random
import keyboard
from colorama import Fore

player = [0, 0]
end = [0, 0]

moves_counter = 0

prueba = [[" ", " ", " ", " ", " "], 
          [" ", " ", " ", " ", " "],
          [" ", " ", " ", " ", " "],
          [" ", " ", " ", " ", " "],
          [" ", " ", " ", " ", " "],]

current_row = 0
current_column = 0
try_counter = 0
rand_number = 2

prueba[4][0] = chr(3)
prueba[0][4] = "X"
current_row = 4
current_column = 0
past_row = current_row
past_column = current_column
player[0] = 4
player[1] = 0
end[0] = 0
end[1] = 4

def draw_board():
    print("Movimientos: ", moves_counter)
    print("Intentos: ", try_counter)
    print("Utilice las teclas WASD para moverse")
    for i in range(5):
        for j in range(5):
            print(Fore.BLUE+"|"+Fore.BLUE+"_"+Fore.BLUE+prueba[i][j].__str__()+Fore.BLUE+"_"+Fore.BLUE+"|", end=" ")
            
        print("\t")

def movements(current_row, current_column, type=False):
    
    lenRows = len(prueba)
    lenColumns = len(prueba[0])
    operation1 = 0
    multipler = [0, 0]
    operation2 = 0
    result = 0
    
    if type is False:
        for x in range(-1 if (current_row > 0)else 0, 2 if (current_row < lenRows-1)else 1):
            for y in range(-1 if (current_column > 0)else 0, 2 if (current_column < lenColumns-1) else 1):
                if (x != 0 or y != 0):
                    posx=current_row+x
                    posy=current_column+y
                    number = random.randint(1, 10)
                    if prueba[posx][posy] == " ":
                        prueba[posx][posy] = number
                        
                        if((current_row-posx)==1):
                            operation1+=number
                        elif((current_row-posx)==-1):
                            operation2+=number
                        elif((current_column-posy)==1):
                            multipler[1]=number
                        elif((current_column-posy)==-1):
                            multipler[0]=number
                    
        operation1*=multipler[0]
        operation2*=multipler[1]
        result=operation1-operation2
                

        return result

    for x in range(-1 if (current_row > 0)else 0, 2 if (current_row < lenRows-1)else 1):
        for y in range(-1 if (current_column > 0)else 0, 2 if (current_column < lenColumns-1) else 1):
            if (x is not 0 or y is not 0):
                if prueba[current_row+x][current_column+y] != "X":
                    prueba[current_row+x][current_column+y] = " "

print("\nBienvenido! su persona esta identificada con el corazon dentro del tablero\nUse las teclas WASD para moverse")
print("El objetivo es llegar a la letra 'X' completando correctamente las operaciones a lo largo del juego")
draw_board()
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP:
        print("Movimientos: ", moves_counter)
        print("Intentos: ", try_counter)
        print("Utilice las teclas WASD para moverse")
        print("Si desea detener el juego presione la tecla 'esc'")

        match event.name:
            case "w":
                if player[0] == 0:
                    print("No puedes moverte mas arriba")
                    continue
                player[0] -= 1
                moves_counter += 1
                prueba[current_row][current_column] = " "
                prueba[player[0]][player[1]] = chr(3)
                current_row = player[0]
                current_column = player[1]
                draw_board()

            case "a":
                if player[1] == 0:
                    print("No puedes moverte mas a la izquierda")
                    continue
                player[1] -= 1
                moves_counter += 1
                prueba[current_row][current_column] = " "
                prueba[player[0]][player[1]] = chr(3)
                current_row = player[0]
                current_column = player[1]
                draw_board()
            case "s":
                if player[0] == 4:
                    print("No puedes moverte mas abajo")
                    continue
                player[0] += 1
                moves_counter += 1
                prueba[current_row][current_column] = " "
                prueba[player[0]][player[1]] = chr(3)
                current_row = player[0]
                current_column = player[1]
                draw_board()
            case "d":
                if player[1] == 4:
                    print("No puedes moverte mas a la derecha")
                    continue
                player[1] += 1
                moves_counter += 1
                prueba[current_row][current_column] = " "
                prueba[player[0]][player[1]] = chr(3)
                current_row = player[0]
                current_column = player[1]
                draw_board()

            case "esc":
                break
            case other:
                print("Tecla no valida")

    if current_column == end[1] and current_row == end[0]:
        print("Felicidades! has ganado")
        break

    if moves_counter == 2 and try_counter < 8:
        try_counter += 1
        moves_counter = 0
        result = movements(current_row, current_column)
        print("Movimientos: ", moves_counter)
        print("Intentos: ", try_counter)
        print("Utilice las teclas WASD para moverse")
        print("Si desea detener el juego presione la tecla 'esc'")
        draw_board()
        print("Cual es el resultado de la operacion?\n")
        response = int(input())
        if response == result:
            print("Respuesta correcta")
            movements(current_row, current_column, True)
            past_column = current_column
            past_row = current_row
        else:
            print("Respuesta incorrecta")
            movements(current_row, current_column, True)
            prueba[current_row][current_column] = " "
            prueba[past_row][past_column] = chr(3)
            current_row = past_row
            current_column = past_column
            player[0] = current_row
            player[1] = current_column
        draw_board()
        
    if try_counter == 8:
        print("Fin del juego. No lograste llegar a la meta")
        break