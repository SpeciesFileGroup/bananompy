from bananompy.utils.bananompy_utils import bionom_get, BASEURL


def parse(names):
    """
    Parse human names

    :param names: [str] Human name(s) separated by \\r\\n

    Usage::

        from bananompy import parse
        parse('Henry Robert Nicollon des Abbayes; Groom Q\\r\\nMrs. John Errol Chandos Aberdeen')
    """
    url = BASEURL + f"parse"
    args = {
        "names": names
    }
    out = bionom_get(url, args)
    return out