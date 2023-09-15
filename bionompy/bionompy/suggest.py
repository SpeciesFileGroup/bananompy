from bionompy.utils.bionompy_utils import bionom_get, BASEURL


def suggest(q, is_public=None, has_occurrences=None, limit=None):
    """
    Suggest human names (autocomplete wiget)

    :param q: [str] Part of a human name
    :param is_public: [bool] Filters results to public or private profiles
    :param has_occurrences: [bool] Filters results to profiles with or without occurrrences

    :param limit: [int] The number of suggestions to return

    Usage::

        from bionompy import suggest
        suggest('Mary Agnes Chas')
    """
    url = BASEURL + f"user.json"
    args = {
        "q": q,
        "is_public": is_public,
        "has_occurrences": has_occurrences,
        "limit": limit
    }
    out = bionom_get(url, args)
    return out