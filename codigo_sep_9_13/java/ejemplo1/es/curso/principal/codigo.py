'''
Created on 12-sep-2024

@author: Anton
'''

def test():
    f = open("fichero.txt", "w")
    f.write("hola mundo")
    f.close()

if __name__ == '__main__':
    test()
    