''' Evaluates Ackermann function

Adopted from here: http://www.eprg.org/computerphile/recursion.htm

Usage:
    python Ackermann.py <brute|cache> <m> <n>
    Where
        <brute|cache> specifies whether to enable the cache
        <m> is the first parameter of the Ackermann function
        <n> is the second parameter of the Ackermann function
'''

import sys


class Ackermann(object):
    ''' Wrapper class for the ackerman function '''
    def __init__(self, use_cache):
        ''' Initialize, setup cache if use_cache==True '''
        self.use_cache = use_cache

        if use_cache:
            # Cache of evaluated (m,n) => f(m,n) pairs
            self.cache = {}
            # Number of function calls
            self.call_count = 0


    def evaluate(self, m, n):
        ''' Evaluates ackermann function recursively '''
        # Increment call count
        self.call_count += 1

        if m == 0:
            return n + 1

        if n == 0:
            return self.evaluate(m-1, 1)

        return self.evaluate(m-1, self.evaluate(m, n-1))


def print_usage():
    print 'Usage:'
    print '\tpython %s <brute|cache> <m> <n>'
    print 'Where:'
    print '\t<brute|cache> specifies whether to enable the cache'
    print '\t<m> is the first parameter of the Ackermann function'
    print '\t<n> is the second parameter of the Ackermann function'

# main()
if __name__ == '__main__':
    if len(sys.argv) != 4: 
        print_usage()
        exit()
