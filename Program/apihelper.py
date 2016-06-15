def info(object, spacing=10, collapse=0):
    u"""Wypisuje metody i ich notatki dokumentacyjne.
    Argumentem moze byc modul, klasa, lista, slownik, czy tez lancuch znakow."""

    methodList = [e for e in dir(object) if callable(getattr(object, e))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\textbackslash{}n".join(["%s %s" %
                                    (method.ljust(spacing),
                                    processFunc(unicode(getattr(object,method). __doc__)))
                                    for method in methodList])
    if __name__ == "__main__":
        print info.__doc__
