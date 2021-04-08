import math
import cmath #for complex numbers e.g sin(3 + 5j)
import numpy


#ABCD matrix elements generator i.e, A, B, C or D, returns are double
def matrixParameter(letter, betaLength, z0):
    if letter == "A":
        return math.cos(betaLength)
    elif letter == "B":
        return (z0*math.sin(betaLength))*1j
    elif letter == "C":
        return ((1/z0)*math.sin(betaLength))*1j
    elif letter == "D":
        return math.cos(betaLength)
    else:
        print("Invalid letter")
        return

betaLengthL1 = 0.7*math.pi 
betaLengthL2 = math.pi 
betaLengthL3 = 0.5*math.pi 

z0_line1 = 75
z0_line2 = 50
z0_line3 = 35

#the full ABCD matrix generator function, returns a matrix
def matrixGenerator(bl, z0):
    return numpy.array([
             [matrixParameter(letter="A", betaLength=bl, z0=z0), 
              matrixParameter(letter="B",betaLength=bl, z0=z0)],
             [matrixParameter(letter="C",betaLength=bl, z0=z0),  
              matrixParameter(letter="D",betaLength=bl, z0=z0)]
            ], dtype=complex)

line1ABCD = matrixGenerator(bl=betaLengthL1, z0=z0_line1)
line2ABCD = matrixGenerator(bl=betaLengthL2, z0=z0_line2)
line3ABCD = matrixGenerator(bl=betaLengthL3, z0=z0_line3)
#print(line3ABCD)



#to find the combined ABCD, matrix multiply the 3
# It is important to note that the order of the
# matrix multiplication must be the same as the
# order of in which the two port networks are
# arranged in the circuit. Matrix multiplication is
# not commutative
l1_l2_ABCD = numpy.dot(line1ABCD, line2ABCD)
cascadedABCD = numpy.dot(l1_l2_ABCD, line3ABCD)
#print(cascadedABCD)

# #how to get individual elements of matrix, where c_A is cascaded A
c_A = cascadedABCD[0][0]
c_B = cascadedABCD[0][1]
c_C = cascadedABCD[1][0]
c_D = cascadedABCD[1][1]


c_z0 = 160 #are we sure the combined Z0 is just the series resistance

def s11():
    numerator = c_A + c_B/c_z0 - c_C*c_z0 - c_D
    denominator = c_A + c_B/c_z0 + c_C*c_z0 + c_D
    return numerator/denominator

def s21():
    numerator = 2
    denominator = c_A + c_B/c_z0 + c_C*c_z0 + c_D
    return numerator/denominator

print(s11())
print(s21())

# modulus = abs(s21())
# phase = cmath.phase(s21())

print(cmath.polar(s11()))
print(cmath.polar(s21()))

print("s11 magnitude is: ", abs(s11()))
print("s11 phase in degrees is: ", numpy.degrees(cmath.phase(s11())))

print("s21 magnitude is: ", abs(s21()))
print("s21 phase in degrees is: ", numpy.degrees(cmath.phase(s21())) )