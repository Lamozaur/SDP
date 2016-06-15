try:
 fsock = open("c:/niemapliku.txt")
except IOError:
 print "Plik nie istnieje"
print "Ta linia zostanie zawsze wypisana"
try:
    import termios, TERMIOS
except ImportError:
    try:
        import msvcrt
    except ImportError:
        try:
            from EasyDialogs import AskPassword
        except ImportError:
            getpass = default_getpass
        else:
            getpass = AskPassword
    else:
        getpass = win_getpass
else:
    getpass = unix_getpass