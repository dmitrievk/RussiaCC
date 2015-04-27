__author__ = 'tian'


from .Builder import WebPageDistance


"""
############
# Overview #
############

To use this distance comparator, you should
(0) Import this lab
(1) Build a comparator
(2) Compare web page as strings using the comparator built in (2)


###########
# Details #
###########

For (0) You can
> from WebPageDistance import WebPageDistance

For (1) you can
> scorer = WebPageDistance()
This is equal to
> scorer = WebPageDistance(metric='lcs')
Which compare exact LCS (longest common sub-sequence) of s1 and s2,
  and return length of LCS over length of s1 plus length of s2.
However, it can only handle cases where len(s1)*len(s2) <= 10*7 in a second.

So another scorer is available as
> scorer = WebPageDistance(metric='shift3b')
Which uses shift3b (see http://siderite.blogspot.com/2007/04/super-fast-and-accurate-string-distance.html)
  algorithm to compare an approximate LCS length, and return length of LCS over length of s1 plus length of s2.
This score has a parameter named max_offset (default value is 50).
Larger max_offset means better approximation but slower computation (The running time is (len(s1)+len(s2))*max_offset)
  you can set max_offset in
> scorer = WebPageDistance(metric='shift3b', max_offset=65)

*NOTE* Please use only one scorer for all comparison.
The results from different scorers are not comparable and mixing them is meaningless.
Also shift3b is highly recommended.

For (2) you can
> s1 = 'abc'
> s2 = 'def'
> score = scorer(s1,s2)
Please note that score satisfies
  i. score >= 0 and score is a real number
 ii. the larger score means more similar strings pair s1 and s2
iii. the score may not be normalized, which means the maximal possible score may not be 1 (may be larger or smaller)

###########
# Example #
###########

from WebPageDistance import WebPageDistance

scorer = WebPageDistance(metric='shift3b', max_offset=65)

s1 = 'abc'
s2 = 'def'
s3 = 'xyz'
s4 = 'xxz'

score_12 = scorer(s1, s2)
score_34 = scorer(s3, s4)

if score_12 >= score_34:
    print('s1 and s2 are more similar than s3 and s4')
else:
    print('s3 and s4 are more similar than s1 and s2')

"""