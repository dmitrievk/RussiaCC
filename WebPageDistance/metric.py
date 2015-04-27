__author__ = 'tian'


def lcs(s1, s2):
    # Longest Common sub-sequence

    l1 = len(s1)
    l2 = len(s2)

    g = [0] * (l2 + 1)

    for i in range(1, l1 + 1):
        f = [0] * (l2 + 1)
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                f[j] = g[j - 1] + 1
            else:
                f[j] = max(f[j - 1], g[j])
        g = f

    return g[l2]


def shift3b(s1, s2, **kwargs):
    # return a quick but dirty lcs (Longest Common sub-sequence)
    # see http://siderite.blogspot.com/2007/04/super-fast-and-accurate-string-distance.html
    # for reference

    l1 = len(s1)
    l2 = len(s2)

    max_offset = kwargs.get('max_offset', 50)
    if l1 == 0 or l2 == 0:
        return 0

    c1, c2 = 0, 0
    lcs = 0
    while c1 < l1 and c2 < l2:
        if s1[c1] == s2[c2]:
            lcs += 1
        else:
            if c1 < c2:
                c2 = c1
            else:
                c1 = c2
            for i in range(0, max_offset):
                if c1 + i < l1 and s1[c1 + i] == s2[c2]:
                    c1 += i
                    break
                if c2 + i < l2 and s1[c1] == s2[c2 + i]:
                    c2 += i
                    break

        c1 += 1
        c2 += 1

    return lcs