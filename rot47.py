_join = "".join
_rot47 = str.maketrans(_join(map(chr,range(33,127))),_join(map(chr,list(range(33+47,127))+list(range(33,33+47)))))
rot47 = lambda s: s.translate(_rot47)
