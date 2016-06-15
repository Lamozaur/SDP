class Singleton(object):
    def __new__(type):
        if not '_instancja' in type.__dict__:
            type._instancja = object.__new__(type)
        return type._instancja

        # przyklad z internetu, staram sie zrozumiec, dalem go zeby nie bylo ze nad tym nie pracuje...


a = Singleton()
a.toto = 12
print a.toto
b = Singleton()
b.toto = 43
print b.toto

print id(a), id(b)