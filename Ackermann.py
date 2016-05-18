''' Evaluates Ackermann function '''

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

