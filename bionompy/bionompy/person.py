from bionompy.utils.bionompy_utils import bionom_get, BASEURL


def get(person_id, csv=None, specimens=None, page=None, limit=None):
    """
    Get a person or their specimens
    
    :param person_id: [str] An ORCID or WikiData identifier
    :param specimens: [bool] Return the person's specimens
    :param csv: [bool] For specimens, whether to return a csv
    :param page: [int] The result page number
    :param limit: [int] The result limit

    Usage::

        from bionompy import person

        # Get Mary Agnes Chase's profile
        person.get('Q3822242')

        # Get Mary Agnes Chase's specimens
        person.get('Q3822242', specimens=True)

        # Get Mary Agnes Chase's specimens in comma-separated value format
        person.get('Q3822242', specimens=True, csv=True)
    """
    if csv and specimens:
        extension = '.csv'
    else:
        extension = '.jsonld'

    if specimens:
        endpoint = f"{person_id}/specimens{extension}"
    else:
        page = None
        limit = None
        endpoint = f"{person_id}{extension}"
    
    url = BASEURL + endpoint
    args = {
        'page': page,
        'limit': limit
    }
    out = bionom_get(url, args)
    return out


def search(
    q,
    families_collected=None,
    families_identified=None,
    date=None,
    strict=False,
    callback=None,
    page=0,
    limit=30,
    **kwargs
):
    """
    Search Bionomia people

    :param q: [str] A single human name
    :param families_collected: [str] Comma-separated list of taxonomic families collected
    :param families_identified: [str] Comma-separated list of taxonomic families identified
    :param date: [str] Filters to alive during date (format: YYYY-MM-DD, YYYY-MM, or YYYY)
        e.g., Captain John Smith was alive from 1580-01-01 through 1631-06-21, so setting date to any value between
            their birth/death date will include Captain John in the search results
    :param strict: [bool] Must include vs should include on families_identified, families_collected, date
    :param callback: [str] A string to produce a JSONP response instead of a JSON-LD response
    :param page: [int] The result page number
    :param limit: [int] The result limit

    Usage::

        from bionompy import person
        person.search(q='Mary Agnes Chase')

        # Filter the search by families collected
        person.search(q='Mary Agnes Chase', familiies_collect='Poaceae', strict=True)
    """
    url = BASEURL + "users/search"
    args = {
        "q": q,
        "families_collected": families_collected,
        "families_identified": families_identified,
        "date": date,
        "strict": strict,
        "callback": callback,
        "page": page,
        "limit": limit
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