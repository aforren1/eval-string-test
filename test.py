import os
from eval_string import eval_string as es

# tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
# print('start tot_m: %d, used_m: %d, free_m: %d' % (tot_m, used_m, free_m))

for i in range(100000):
    y = i
    ret = es('x = y')
    
    if ret != 0:
        raise RuntimeError('Err code!')

    if 'x' not in locals():
        raise RuntimeError('No x!')
    
    if x != i:
        raise RuntimeError('Wrong result!')

# tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
# print('end tot_m: %d, used_m: %d, free_m: %d' % (tot_m, used_m, free_m))
