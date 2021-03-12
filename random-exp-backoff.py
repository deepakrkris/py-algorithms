import random
import os
import sys
import resource

class Backoff:
    """Full Jitter Backoff implementation."""

    def __init__(self, base, cap):
        """Init."""
        self.base = base
        self.cap = cap

    def expo(self, n):
        """Backoff function."""
        return min(self.cap, pow(2, n) * self.base)


class ExpoBackoffFullJitter(Backoff):
    """Full Jitter Backoff implementation."""

    def backoff(self, n):
        """Full jitter backoff function."""
        base = self.expo(n)
        fulljitter = random.uniform(0, base)
        # print("Backoff: %s - Full Jitter Backoff: %s" % (base, fulljitter))
        return fulljitter

p = ExpoBackoffFullJitter(10, 10)

print (p.backoff(10))