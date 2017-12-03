########
# 4.0
########

# bit-wise operators: 
# x << y: Returns x with bits shifted to left by y places. Same as x * (2 ** y).
# x >> y: Returns x with bits shifted to right by y places. Sams as x // (2 ** y).
# x & y: Bitwise "and". Each bit of output is 1 if corresponding bits of both x and y is 1, otherwise 0. 
# x | y: Bitwise "or". Each bit of output is 1 if either corresponding bit is 1, otherwise 0.
# ~x: Returns complement of x. Same as (-x - 1).
# x ^ y: Bitwise XOR. 1 if either but not both corresponding bits is 1, otherwise 0.

# x & (x - 1): erases lowest set bit of x
# x & ~(x - 1): access lowest set bit of x

########
# 4.1
########

#O(n)
def parity_check(num):
  result = 0
  while num:
    result += num & 1
    num >>= 1
  return result % 2

#O(k)
def parity_check_2(num):
  result = 0
  while num:
    result ^= 1
    num &= (num - 1)
  return result

def parity_check_3(num):
  mask_size = 16
  bit_mask = 0xFFFF
  return (precomputed_parity[x >> (3 * mask_size)] ^
          precomputed_parity[(x >> (2 * mask_size)) & bit_mask] ^
          precomputed_parity[(x >> mask_size) & bit_mask] ^
          precomputed_parity[x & bit_mask])

def parity_check_4(num):
  x ^= x >> 32
  x ^= x >> 16
  x ^= x >> 8
  x ^= x >> 4
  x ^= x >> 2
  x ^= x >> 1
  return x & 0x1








