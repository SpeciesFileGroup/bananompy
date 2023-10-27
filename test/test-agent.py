import vcr
import bananompy
import re
import pytest
from bananompy.utils.bananompy_utils import MustAcknowledgeTemporaryIdentifiers


@vcr.use_cassette("test/vcr_cassettes/test_agent_search_random.yaml")
def test_agent_search_random():
    res = bananompy.agent.search(ack_temp_ids=True)
    assert re.match(r'^[0-9]+$', res[0]['id'])


@vcr.use_cassette("test/vcr_cassettes/test_agent_search_mary.yaml")
def test_agent_search_mary():
    res = bananompy.agent.search(q='Mary', ack_temp_ids=True)
    for r in res:
        assert 'Mary' in r['name']


@vcr.use_cassette("test/vcr_cassettes/test_agent_get.yaml")
def test_agent_get():
    res = bananompy.agent.get(1, ack_temp_ids=True)
    assert 'gbif_id' in res[0]
    assert 'https://gbif.org/occurrence/' in res[0]['url']


@vcr.use_cassette("test/vcr_cassettes/test_agent_get_exception.yaml")
def test_agent_get_exception():
    with pytest.raises(MustAcknowledgeTemporaryIdentifiers):
        res = bananompy.agent.get(1)


@vcr.use_cassette("test/vcr_cassettes/test_agent_search_exception.yaml")
def test_agent_get_exception():
    with pytest.raises(MustAcknowledgeTemporaryIdentifiers):
        res = bananompy.agent.search(q='Mary')