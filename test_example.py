from hack import restar, lista, texto, texto_upper


def test_compare_subtract():

    r = restar()

    token = False

    if r == 1:

        token = True

    res = isinstance(r, int)

    assert (r, int, token) == (res, int, True)

def test_compare_list():

    r = lista()

    token_ls = False

    token_len = False

 

    if r == ["foo","bar","charlie"]:

        token_ls = True

    

    if len(r) == 3:

        token_len = True

 

    assert(token_ls, token_len) == (True, True)
    
def test_compare_string():

    check = "hola"

    assert texto(check) == "hola"
    
def test_compare_upper():

    txt = "hola"

    assert texto_upper(txt) == "HOLA"
