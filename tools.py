import hashlib, pt
from json import dumps as package, loads as unpackage
def pub2addr(x): return pt.pubtoaddr(x)
def det_hash(x):#deterministically takes sha256 of dict, list, int, float, or string
    def det_list(l): return '[%s]' % ','.join(map(det, sorted(l)))
    def det_dict(x): return '{%s}' % ','.join(map(lambda p: det(p[0]) + ':' + det(p[1]), sorted(x.items())))
    def det(x): return {list: det_list, dict: det_dict}.get(type(x), str)(x)
    return hashlib.sha256(det(unpackage(package(x)))).hexdigest()
