def a299():
    n = int(input())
    s = input()
    x = s.find('|')
    y = s.rfind('|')
    z = s.find('*')

    if (x < z) and (z < y):
        print('in')
    else:
        print('out')

if __name__ == '__main__':
    a299()
