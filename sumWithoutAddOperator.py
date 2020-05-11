a=3
b=-4

mask = 0xffffffff
 
while (b & mask) > 0:
    carry = ( a & b ) << 1
    a = (a ^ b)
    b = carry
print((a & mask) if b > 0 else a)

