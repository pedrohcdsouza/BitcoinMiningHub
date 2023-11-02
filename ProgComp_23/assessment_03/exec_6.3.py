#pedrohcdsouza arquive

seq  = '73167176531330624919225119674426574742355349194934'
seq += '96983520312774506326239578318016984801869478851843'
seq += '85861560789112949495459501737958331952853208805511'
seq += '12540698747158523863050715693290963295227443043557'
seq += '66896648950445244523161731856403098711121722383113'
seq += '62229893423380308135336276614282806444486645238749'
seq += '30358907296290491560440772390713810515859307960866'
seq += '70172427121883998797908792274921901699720888093776'
seq += '65727333001053367881220235421809751254540594752243'
seq += '52584907711670556013604839586446706324415722155397'
seq += '53697817977846174064955149290862569321978468622482'
seq += '83972241375657056057490261407972968652414535100474'
seq += '82166370484403199890008895243450658541227588666881'
seq += '16427171479924442928230863465674813919123162824586'
seq += '17866458359124566529476545682848912883142607690042'
seq += '24219022671055626321111109370544217506941658960408'
seq += '07198403850962455444362981230987879927244284909188'
seq += '84580156166097919133875499200524063689912560717606'
seq += '05886116467109405077541002256983155200055935729725'
seq += '71636269561882670428252483600823257530420752963450'

clsm = 0 #current longest sequence multiplication

for pos in range(0, len(seq)-4):
    multiplication = int(seq[pos]) * int(seq[pos+1]) * int(seq[pos+2]) * int(seq[pos+3]) * int(seq[pos+4])
    if multiplication > clsm:
        clsm = multiplication
        lseq = str(seq[pos])+str(seq[pos+1])+str(seq[pos+2])+str(seq[pos+3])+str(seq[pos+4]) #longest sequence
print(f"The bigger sequence is {lseq} and the multiplication of each number generates the value: {clsm}")
