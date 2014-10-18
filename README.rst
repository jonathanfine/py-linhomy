Python Linear Homology
======================

Support for linear homology (an emerging area in mathematics that
involves geometry, topology and combinatorics).

Fibonacci subsets
-----------------

These are used in the (candidate) formula for linear homology Betti
numbers.  Let W be a set containing a Fibonacci number of elements,
such as the ways of writing some number n as a sum of a sequence of
1's and 2's.  The formula for linear homology requires us, for each
element w of W, to produce a subset sub(w) of W.  These are the words
w' in W that are *subordinate* to w.

This work will be developed in the fib-subset branch.
