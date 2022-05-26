class Cube():

    def __init__(self) -> None:
        '''
         Initializes a cube in Format:
               O|O|O                          0| 1| 2
               O|O|O                          3| 4| 5
               O|O|O                          6| 7| 8
         G|G|G W|W|W B|B|B Y|Y|Y     9|10|11 12|13|14 15|16|17 18|19|20
         G|G|G W|W|W B|B|B Y|Y|Y    21|22|23 24|25|26 27|28|29 30|31|32
         G|G|G W|W|W B|B|B Y|Y|Y    33|34|35 36|37|38 39|40|41 42|43|44
               R|R|R                         45|46|47
               R|R|R                         48|49|50
               R|R|R                         51|52|53
        '''
        self.cube = 'OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR'


    def __str__(self) -> str:
        start = [0, 3, 6, 45, 48, 51]
        end = [2, 5, 8, 20, 32, 44, 47, 50, 53]
        cube = ''
        idx = 0
        for c in self.cube:
            if start.__contains__(idx):
                cube += '      '
            cube += c
            if end.__contains__(idx):
                cube += '\n'
            else:
                cube += '|'
            idx += 1
        return cube

    def U(self) -> None:
        cube = list(self.cube)
        temp1 = cube[9]
        temp2 = cube[10]
        temp3 = cube[11]

        cube[9] = cube[12]
        cube[10] = cube[13]
        cube[11] = cube[14]

        cube[12] = cube[15]
        cube[13] = cube[16]
        cube[14] = cube[17]

        cube[15] = cube[18]
        cube[16] = cube[19]
        cube[17] = cube[20]

        cube[18] = temp1
        cube[19] = temp2
        cube[20] = temp3

        temp1 = cube[0]
        temp2 = cube[1]
        temp3 = cube[2]

        cube[0] = cube[6]
        cube[1] = cube[3]
        cube[2] = temp1

        cube[6] = cube[8]
        cube[3] = cube[7]

        cube[8] = temp3
        cube[7] = cube[5]

        cube[5] = temp2
        self.cube = ''.join(cube)

    def Ui(self) -> None:
        cube = list(self.cube)
        temp1 = cube[9]
        temp2 = cube[10]
        temp3 = cube[11]

        cube[9] = cube[18]
        cube[10] = cube[19]
        cube[11] = cube[20]

        cube[18] = cube[15]
        cube[19] = cube[16]
        cube[20] = cube[17]
        
        cube[15] = cube[12]
        cube[16] = cube[13]
        cube[17] = cube[14]

        cube[12] = temp1
        cube[13] = temp2
        cube[14] = temp3

        temp1 = cube[0]
        temp2 = cube[1]
        temp3 = cube[2]

        cube[0] = temp3
        cube[1] = cube[5]
        cube[2] = cube[8]

        cube[8] = cube[6]
        cube[5] = cube[7]

        cube[7] = temp1
        cube[6] = cube[3]

        cube[3] = temp2

        self.cube = ''.join(cube)


    #! Restliche Felder bewegen sich auch -> muss noch implementiert werden
    def D(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[42]
        cube[34] = cube[43]
        cube[35] = cube[44]

        cube[42] = cube[39]
        cube[43] = cube[40]
        cube[44] = cube[41]

        cube[39] = cube[36]
        cube[40] = cube[37]
        cube[41] = cube[38]

        cube[36] = temp1
        cube[37] = temp2
        cube[38] = temp3
        self.cube = ''.join(cube)

    def Di(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[36]
        cube[34] = cube[37]
        cube[35] = cube[38]

        cube[36] = cube[39]
        cube[37] = cube[40]
        cube[38] = cube[41]

        cube[39] = cube[42]
        cube[40] = cube[43]
        cube[41] = cube[44]

        cube[42] = temp1
        cube[43] = temp2
        cube[44] = temp3
        self.cube = ''.join(cube)

    def L(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[0]
        temp2 = cube[3]
        temp3 = cube[6]

        cube[0] = cube[44]
        cube[3] = cube[32]
        cube[6] = cube[20]

        cube[44] = cube[45]
        cube[32] = cube[48]
        cube[20] = cube[51]

        cube[45] = cube[12]
        cube[48] = cube[25]
        cube[51] = cube[36]

        cube[12] = temp1
        cube[24] = temp2
        cube[36] = temp3
        self.cube = ''.join(cube)

    def Li(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[36]
        cube[34] = cube[37]
        cube[35] = cube[38]

        cube[36] = cube[39]
        cube[37] = cube[40]
        cube[38] = cube[41]

        cube[39] = cube[42]
        cube[40] = cube[43]
        cube[41] = cube[44]

        cube[42] = temp1
        cube[43] = temp2
        cube[44] = temp3
        self.cube = ''.join(cube)

    def R(self) -> None:
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[36]
        cube[34] = cube[37]
        cube[35] = cube[38]

        cube[36] = cube[39]
        cube[37] = cube[40]
        cube[38] = cube[41]

        cube[39] = cube[42]
        cube[40] = cube[43]
        cube[41] = cube[44]

        cube[42] = temp1
        cube[43] = temp2
        cube[44] = temp3
        self.cube = ''.join(cube)
        pass

    def Ri(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[36]
        cube[34] = cube[37]
        cube[35] = cube[38]

        cube[36] = cube[39]
        cube[37] = cube[40]
        cube[38] = cube[41]

        cube[39] = cube[42]
        cube[40] = cube[43]
        cube[41] = cube[44]

        cube[42] = temp1
        cube[43] = temp2
        cube[44] = temp3
        self.cube = ''.join(cube)

    def F(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[36]
        cube[34] = cube[37]
        cube[35] = cube[38]

        cube[36] = cube[39]
        cube[37] = cube[40]
        cube[38] = cube[41]

        cube[39] = cube[42]
        cube[40] = cube[43]
        cube[41] = cube[44]

        cube[42] = temp1
        cube[43] = temp2
        cube[44] = temp3
        self.cube = ''.join(cube)

    def Fi(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[36]
        cube[34] = cube[37]
        cube[35] = cube[38]

        cube[36] = cube[39]
        cube[37] = cube[40]
        cube[38] = cube[41]

        cube[39] = cube[42]
        cube[40] = cube[43]
        cube[41] = cube[44]

        cube[42] = temp1
        cube[43] = temp2
        cube[44] = temp3
        self.cube = ''.join(cube)

    def B(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[36]
        cube[34] = cube[37]
        cube[35] = cube[38]

        cube[36] = cube[39]
        cube[37] = cube[40]
        cube[38] = cube[41]

        cube[39] = cube[42]
        cube[40] = cube[43]
        cube[41] = cube[44]

        cube[42] = temp1
        cube[43] = temp2
        cube[44] = temp3
        self.cube = ''.join(cube)

    def Bi(self) -> None:
        pass
        cube = list(self.cube)
        temp1 = cube[33]
        temp2 = cube[34]
        temp3 = cube[35]

        cube[33] = cube[36]
        cube[34] = cube[37]
        cube[35] = cube[38]

        cube[36] = cube[39]
        cube[37] = cube[40]
        cube[38] = cube[41]

        cube[39] = cube[42]
        cube[40] = cube[43]
        cube[41] = cube[44]

        cube[42] = temp1
        cube[43] = temp2
        cube[44] = temp3
        self.cube = ''.join(cube)


if __name__ == '__main__':
    cube = Cube()
    print("Init:")
    print(cube)
    cube.L()
    print(cube)
    cube.U()
    print(cube)
    cube.L()
    print(cube)