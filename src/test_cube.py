from Cube import Cube


def test_Init():
    cube = Cube()
    assert(cube.cube == 'OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR')
    del(cube)
    return True


def test_Stringify():
    cube = Cube()
    assert(str(cube) == '      O|O|O\n      O|O|O\n      O|O|O\nG|G|G|W|W|W|B|B|B|Y|Y|Y\nG|G|G|W|W|W|B|B|B|Y|Y|Y\nG|G|G|W|W|W|B|B|B|Y|Y|Y\n      R|R|R\n      R|R|R\n      R|R|R\n')
    del(cube)
    return True


def test_U():
    cube = Cube()
    cube.U()
    assert(cube.cube == 'OOOOOOOOOWWWBBBYYYGGGGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR')
    del(cube)
    return True


def test_Ui():
    cube = Cube()
    cube.Ui()
    assert(cube.cube == 'OOOOOOOOOYYYGGGWWWBBBGGGWWWBBBYYYGGGWWWBBBYYYRRRRRRRRR')
    del(cube)
    return True


def test_D():
    cube = Cube()
    cube.D()
    assert(cube.cube == 'OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYYYYGGGWWWBBBRRRRRRRRR')
    del(cube)
    return True


def test_Di():
    cube = Cube()
    cube.Di()
    assert(cube.cube == 'OOOOOOOOOGGGWWWBBBYYYGGGWWWBBBYYYWWWBBBYYYGGGRRRRRRRRR')
    del(cube)
    return True


def test_L():
    cube = Cube()
    cube.L()
    assert(cube.cube == 'YOOYOOYOOGGGOWWBBBYYRGGGOWWBBBYYRGGGOWWBBBYYRWRRWRRWRR')
    del(cube)
    return True

if __name__ == '__main__':
    print(test_Init())
    print(test_Stringify())
    print(test_U())
    print(test_Ui())
    print(test_D())
    print(test_Di())
    print(test_L())
