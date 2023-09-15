from bionompy.utils.bionompy_utils import bionom_get, BASEURL


def get(occurrence_id):
    """
    Search Bionomia occurrence

    :param occurrence_id: [str] Simple search parameter. The value for this parameter can be a simple word or a phrase.

    Usage::

        from bionompy import occurrence
        occurrence.get('477976412')
    """
    url = BASEURL + f"occurrence/{occurrence_id}.jsonld"
    args = {}
    out = bionom_get(url, args)
    return out


def search(dataset_id, occurrence_id, callback=None, page=0, limit=30, **kwargs):
    """
    Search Bionomia occurrence

    :param dataset_id: [str] A dataset identifier
    :param occurrence_id: [str] Simple search parameter. The value for this parameter can be a simple word or a phrase.
    :param callback: [str] A string to produce a JSONP response instead of a JSON-LD response
    :param page: [int] The result page number

    Usage::

        from bionompy import occurrence
        occurrence.search('f86a681d-7db8-483b-819a-248def18b70a', '7a1daa39-8d7c-d7c4-968f-799d58b3c7b0')

        # Return page 2 of the results
        occurrence.search('f86a681d-7db8-483b-819a-248def18b70a', '7a1daa39-8d7c-d7c4-968f-799d58b3c7b0', page=2)
    """
    url = BASEURL + "occurrences/search"
    args = {
        "dataset_id": dataset_id,
        "occurrence_id": occurrence_id,
        "callback": callback,
        "page": page
    }
    kwargs = {key: kwargs[key] for key in kwargs if key not in requests_argset}
    if kwargs is not None:
        xx = dict(
            zip([re.sub("_", ".", x) for x in kwargs.keys()], kwargs.values())
        )
        args.update(xx)
    kwargs = {key: kwargs[key] for key in kwargs if key in requests_argset}
    out = bionom_get(url, args, **kwargs)
    return out