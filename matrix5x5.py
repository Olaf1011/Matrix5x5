import busio
import board
import adafruit_is31fl3731

i2c = busio.I2C(board.SCL, board.SDA)

display = adafruit_is31fl3731.Matrix(i2c)

class matrix:
    def clear():
        display.fill(0)
    def Red(x = 0, y = 0):
        redX = [[6,5,4,3,2],[4,5,6,0,1],[3,2,1,0,15],[13,12,11,10,9],[14,15,8,9,10]]
        redY = [[7,7,7,7,7],[8,8,8,7,7],[8,8,8,8,7],[7,7,7,7,7],[7,0,0,0,0]]
        return(redX[x][y],redY[x][y])

    def Green(x = 0, y = 0):
        greenX = [[5,4,4,3,2],[3,4,5,0,1],[2,1,1,0,15],[12,11,10,9,9],[13,15,9,10,11]]
        greenY = [[4,4,5,5,5],[1,1,1,5,5],[1,1,2,2,2],[1,1,1,1,2],[1,5,5,5,5]]
        return(greenX[x][y], greenY[x][y])

    def Blue(x = 0, y = 0):
        blueX = [[5,5,4,3,2],[3,4,5,0,1],[2,2,1,0,15],[12,11,10,10,9],[13,15,9,10,11]]
        blueY = [[5,6,6,6,6],[2,2,2,6,6],[2,3,3,3,3],[2,2,2,3,3],[2,6,6,6,6]]
        return(blueX[x][y],blueY[x][y])

    #x coor, y coor, Red 0 - 255, Green 0 - 255, Blue 0 - 255
    def fill(y = None, x = None, r = None, g = None, b = None):
        if(x == None or y ==  None):
            display.fill(255)
        else:
            if(x > 5 or y > 5 or x < 1 or y < 1):
               print("Oi dickhead to big of a value")
            else:
                x -= 1
                y -= 1
                if (r != None):
                    red = matrix.Red(x , y);
                    display.pixel(red[0],int(red[1]),r)

                #Green colour
                if (g != None):
                    green = matrix.Green(x , y);
                    display.pixel(green[0],green[1],g)

                #Blue colour
                if (b != None):
                    blue = matrix.Blue(x , y);
                    display.pixel(blue[0],blue[1],b)