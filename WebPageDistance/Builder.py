__author__ = 'tian'

from .metric import lcs, shift3b


def WebPageDistance(**kwargs):
    def f(p1, p2):
        assert type(p1) == str
        assert type(p2) == str

        metric = kwargs.get('metric', 'lcs')

        if metric == 'lcs':
            return lcs(p1, p2) / max(1, len(p1) + len(p2))
        elif metric == 'shift3b':
            return shift3b(p1, p2, **kwargs) / max(1, len(p1) + len(p2))
        else:
            assert False

    return f
