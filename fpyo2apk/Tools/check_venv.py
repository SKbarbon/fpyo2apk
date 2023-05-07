



def is_on_venv ():
    import os
    if os.environ.get('VIRTUAL_ENV') is not None:
        return True
    else:
        return False