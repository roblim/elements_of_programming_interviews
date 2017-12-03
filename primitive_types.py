#bit-wise operators: 
# x << y: Returns x with bits shifted to left by y places. Same as x * (2 ** y).
# x >> y: Returns x with bits shifted to right by y places. Sams as x // (2 ** y).
# x & y: Bitwise "and". Each bit of output is 1 if corresponding bits of both x and y is 1, otherwise 0. 
# x | y: Bitwise "or". Each bit of output is 1 if either corresponding bit is 1, otherwise 0.
# ~x: Returns complement of x. Same as (-x - 1).
# x ^ y: Bitwise XOR. 1 if either but not both corresponding bits is 1, otherwise 0.

def parity_check(num):
  result = 0
  while num:
    result += num & 1
    num >>= 1
  return result % 2

  
