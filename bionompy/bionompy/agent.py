from bionompy.utils.bionompy_utils import bionom_get_agent_specimens, bionom_get_agent_list


def get(agent_id, page=1):
    """
    Get specimens with a temporary agent_id

    WARNING: Agent string IDs are temporary and refreshed periodically (e.g., next week you might not get the same results)

    :param q: [str] Part of a human name
    :param page: [int] The result page number

    Usage::

        from bionompy import agent

        # get specimens for agent_id=1
        agent.get(1)

        # search agent strings
        agent.get(1, page=2)
    """
    url = f'https://bionomia.net/agent/{agent_id}'
    args = {
        "page": page,
    }
    out = bionom_get_agent_specimens(url, args)
    return out


def search(q=None):
    """
    Search agent strings (or get a random list of agent strings if no q param is provided)

    WARNING: Agent string IDs are temporary and refreshed periodically (e.g., next week you might not get the same results)

    :param q: [str] Part of a human name

    Usage::

        from bionompy import agent

        # get a random list of agent strings
        agent.search()

        # search agent strings
        agent.search(q='Carol')
    """
    url = 'https://bionomia.net/agents'
    args = {
        "q": q,
    }
    out = bionom_get_agent_list(url, args)
    return out
