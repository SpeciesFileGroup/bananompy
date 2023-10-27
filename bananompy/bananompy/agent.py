from bananompy.utils.bananompy_utils import bionom_get_agent_specimens, bionom_get_agent_list, MustAcknowledgeTemporaryIdentifiers


def get(agent_id, page=1, ack_temp_ids=False):
    """
    Get specimens with a temporary agent_id

    WARNING: Agent string IDs are temporary and refreshed periodically (e.g., next week you might not get the same results)
        The Bionomia website also goes down every 2 weeks for an hour while new agent strings are loaded

    :param q: [str] Part of a human name
    :param page: [int] The result page number
    :param ack_temp_ids: [bool] Set to True to acknowledge that you understand that agent identifier are temporary and that the Bionomia website goes down while new agent strings are loaded

    Usage::

        from bananompy import agent

        # get specimens for agent_id=1
        agent.get(1)

        # search agent strings
        agent.get(1, page=2)
    """
    if ack_temp_ids == False:
        raise MustAcknowledgeTemporaryIdentifiers()
    url = f'https://bionomia.net/agent/{agent_id}'
    args = {
        "page": page,
    }
    out = bionom_get_agent_specimens(url, args)
    return out


def search(q=None, ack_temp_ids=False):
    """
    Search agent strings (or get a random list of agent strings if no q param is provided)

    WARNING: Agent string IDs are temporary and refreshed periodically (e.g., next week you might not get the same results)
        The Bionomia website also goes down every 2 weeks for an hour while new agent strings are loaded

    :param q: [str] Part of a human name
    :param ack_temp_ids: [bool] Set to True to acknowledge that you understand that agent identifier are temporary and that the Bionomia website goes down while new agent strings are loaded

    Usage::

        from bananompy import agent

        # get a random list of agent strings
        agent.search()

        # search agent strings
        agent.search(q='Carol')
    """
    if ack_temp_ids == False:
        raise MustAcknowledgeTemporaryIdentifiers()
    url = 'https://bionomia.net/agents'
    args = {
        "q": q,
    }
    out = bionom_get_agent_list(url, args)
    return out
