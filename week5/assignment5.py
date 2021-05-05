import numpy as np

def binom_expansion ( xs ) : # (2 , 3)
    def expansion ( t1 , t2 ) : # (x -2) [1 -2] (x -3) [1 -3] (x^2 -5x +6) [1 , -5, 6]
        lt = len ( t1 )
        rt = np . zeros ( lt + len ( t2 ) -1)
        for j in range ( len ( t2 )):
            rt [j:j + lt ] += t1 * t2 [j]


        return rt
    ts = [ np . array ([1 , -x ]) for x in xs ] # [1 , -2] [1 , -3]

    mulnom = expansion ( ts [0] , ts [1])
    for i in range (2 , len ( ts )):
        mulnom = expansion ( mulnom , ts [i ])

    return mulnom

def solve ( mulnom ):
    mat = np . zeros ([ len ( mulnom ) -1, len ( mulnom ) -1])
    mat [0 , :] = - mulnom [1:]
    for i in range ( len ( mat ) -1) :# [x, y, z]
        mat [i +1 , i] = 1              #[1 , 0, 0]
                                        #[0 , 1 , 0]
    ev , _ = np . linalg.eig( mat )
    return ev

def funceval ( mulnom , x ):
    ax = mulnom [ -1]
    lm = len ( mulnom ) -1
    for i in range ( lm ):
        ax += mulnom [i ]*( x **( lm -i) )

    return ax


def calc(mulnom):
    str = ""
    for i in range(0, len(mulnom)-1):
        if mulnom[i] == 1:
            str += ("x^%d" % ((len(mulnom)-1-i)))
        elif mulnom[i] > 1:
            str += ("+%gx^%d" % (mulnom[i], (len(mulnom)-1-i)))
        else:
            str += ("%gx^%d" % (mulnom[i], (len(mulnom)-1-i)))
    str += ("+%g " % mulnom[len(mulnom)-1])

    return str

if __name__ == "__main__":
   
   mulnom = binom_expansion([-3, 3, -1.5, 1.5, 1, 0.3])
   print('f(x): ', calc(mulnom))

   x = solve(mulnom)

   print('x:',(solve(mulnom)))
   print('y = f(x):',funceval(mulnom, x))