# save the last 5 elements
from collections import deque
pre_lines = deque(maxlen=5)
def test1_3():
    for x in range(20):
        pre_lines.append(x)
#        print(pre_lines)
    pre_lines.appendleft(123321)
    print(pre_lines.popleft())

# find the nth largest or smallest elements
def test1_3():
    import heapq
    a = list(range(5,10)) + list(range(5))
    print(heapq.nlargest(6, a))
    print(heapq.nsmallest(6, a))
    heapq.heapify(a)
    print(heapq.heappop(a))
    heapq.heappush(a, 1.5)
    print(a)

# implement a priority queue
class PriorityQ:
    def __init__(self):
        self._q = []
        self._n = 0
    def pop(self):
        return heapq.heappop(self._q)
    def push(self, x):
        heapq.heappush(self._q, x)

# one key maps to several values
def test1_6():
    from collections import defaultdict
    dd = defaultdict(list)
    for key, val in c:
        dd[key].append(val)

# make the dict ordered
def test1_7():
    from collections import OrderedDict
    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    d['v'] = 3
    for k,v in d.items():
        print(k,'=>',v)

# calculation over dict
def test1_8():
    prices = {
            'a':1,
            'b':2,
            'c':3,
            'd':4
            }
    print(max(prices, key=prices.__getitem__))
    print(min(prices, key=prices.__getitem__))

# find same elements between two dicts
def test1_9():
    a = dict(x=1, y=2, z=3)
    b = dict(x=10, y=2, w=10)
    print(a.keys() & b.keys())
    print(a.items() & b.items())
    print({x:a[x] for x in a.keys() - b.keys()})

# remove the deplicates keeping orders
def dedup(items):
    memo = set()
    for x in items:
        if x not in memo:
            memo.add(x)
            yield x

# find the elements of the most times
def test1_12():
    from collections import Counter
    a = []
    [a.extend([x for _ in range(x)]) for x in range(6)]
    c = Counter(a)
    print(c)
    print(c.most_common(2))

# sort by common key
def test1_13():
    from operator import itemgetter
    a = [(x,x+1) for x in range(10)]
    print(sorted(a, key=itemgetter(1,0)))

# sort by common attr
def test1_14():
    from operator import attrgetter
    class c:
        def __init__(self, x, y):
            self.x, self.y = x, y

    a = [c(x, y) for x in range(10) for y in range(9, -1, -1)]
    print(sorted(a, key=attrgetter('x', 'y')))

# group by
def test1_15():
    a = []
    [a.extend([x for _ in range(x)]) for x in range(6)]
    from itertools import groupby
    print(list(groupby(a)))

# filter
def test1_16():
    v = ['1', '-1', '-', 'N', '5.1']
    from operator import methodcaller
    print(list(filter(methodcaller('isdigit'), v)))

# namedtuple
def test1_18():
    from collections import namedtuple
    a = namedtuple('a', ['x', 'y'])
    print(a(x=1, y=2))


# concat dicts together
def test1_20():
    from collections import ChainMap
    a = dict(x=1, y=2, z=3)
    b = dict(x=10, y=2, w=10)
    c = ChainMap(a, b)
    for k in c:
        print(k,'=>', c[k])


if __name__ == '__main__':
    test1_20()
