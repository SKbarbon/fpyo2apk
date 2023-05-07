


def is_it_mac ():
    import sys
    if "darwin" in str(sys.platform):
        return True
    else:
        return False