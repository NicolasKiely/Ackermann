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
        # Number of function calls
        self.call_count = 0

        self.use_cache = use_cache
        if use_cache:
            # Cache of evaluated (m,n) => f(m,n) pairs
            self.cache = {}


    def evaluate(self, m, n):
        ''' Evaluates ackermann function recursively '''
        # Increment call count
        self.call_count += 1

        if self.use_cache:
            # Check cache
            if (m, n) in self.cache:
                return self.cache[(m, n)]

        if m == 0:
            results = n + 1

        elif n == 0:
            results = self.evaluate(m-1, 1)
        
        else:
            results = self.evaluate(m-1, self.evaluate(m, n-1))

        if self.use_cache:
            # Save to cache
            self.cache[(m, n)] = results

        return results


def print_usage():
    print 'Program Usage:'
    print '\tpython %s <brute|cache> <m> <n>' % sys.argv[0]
    print 'Where:'
    print '\t<brute|cache> specifies whether to enable the cache'
    print '\t<m> is the first parameter of the Ackermann function'
    print '\t<n> is the second parameter of the Ackermann function'

# Acceptable arguments for setting cache
acceptable_nocache_args = ('brute', 'no', 'n')
acceptable_yescache_args = ('cache', 'yes', 'y')

# Message shown when bad ackermann argument passed
bad_number_msg = 'Error, expected positive integer %s argument, got "%s"'


# main()
if __name__ == '__main__':
    # Check number of arguments
    if len(sys.argv) != 4: 
        print_usage()
        exit()

    # Check cache argument
    par_cache = sys.argv[1].lower()
    if par_cache in acceptable_nocache_args:
        use_cache = False

    elif par_cache in acceptable_yescache_args:
        use_cache = True

    else:
        # Could not parse first argument
        print 'Error, could not understand cache arg %s'
        print 'To use the cache, valid strings are: '
        print '\t' + ', '.join(acceptable_yescache_args)
        print 'To not use the cache, valid strings are: '
        print '\t' + ', '.join(acceptable_nocache_args)

        print
        print_usage()
        exit()

    # Check m and arguments
    ack_pars = [0, 0]
    for i, name in enumerate(('<m>', '<n>')):
        try:
            # Cast parameter to integer
            par = sys.argv[2+i]
            ack_pars[i] = int(par)

            # Make sure parameter is positive
            if ack_pars[i] < 0:
                raise ValueError

        except ValueError:
            # Handle casting error
            print bad_number_msg % (name, par)
            print
            print_usage()
            exit()

    # Argument parsing done, now setup ackermann function and evaluate
    ack = Ackermann(use_cache)
    results = ack.evaluate(*ack_pars)

    # Show results
    print 'Ackermann(%d, %d) is: %d' % (ack_pars[0], ack_pars[1], results)
    print 'Number of calls: %d' % ack.call_count
