from Cube import Cube


def testInit():
    cube = Cube()
    assert(cube.cube == 'OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR')
    del(cube)
    return True


def testStringify():
    cube = Cube()
    assert(str(cube) == 
    '      O|O|O\n      O|O|O\n      O|O|O\nG|G|G|W|W|W|B|B|B|Y|Y|Y\nG|G|G|W|W|W|B|B|B|Y|Y|Y\nG|G|G|W|W|W|B|B|B|Y|Y|Y\n      R|R|R\n      R|R|R\n      R|R|R\n')
    del(cube)
    return True


def testU():
    cube = Cube()
    cube.U()
    assert(cube.cube == 'OOOOOOOOOWWWBBBYYYGGGGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR')
    
    del(cube)
    return True


def testUi():
    cube = Cube()
    cube.Ui()
    assert(cube.cube == 'OOOOOOOOOYYYGGGWWWBBBGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR')
    del(cube)
    return True


def testD():
    cube = Cube()
    cube.D()
    assert(cube.cube == 'OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYYYYGGGWWWBBBRRRRRRRRR')
    del(cube)
    return True


def testDi():
    cube = Cube()
    cube.Di()
    assert(cube.cube == 'OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYWWWBBBYYYGGGRRRRRRRRR')
    del(cube)
    return True


if __name__ == '__main__':
    print(testInit())
    print(testStringify())
    print(testU())
    print(testUi())
    print(testD())
    print(testDi())