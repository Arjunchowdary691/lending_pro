
#sadhvuwefdherwuhfrwe hi feature21

import sys

# Obfuscated Fibonacci using lambda calculus
fib = (lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y))))(lambda f: lambda n: n if n < 2 else f(n-1) + f(n-2))

# Strange behavior: prints a Fibonacci sequence in an unusual way
print([fib(i) for i in range(10)])

# Self-modifying function that writes to its own source file
def self_modifying():
    with open(sys.argv[0], "a") as f:
        f.write("\n# This script just modified itself!\n")

self_modifying()

# This script just modified itself!
