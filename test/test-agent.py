import vcr
import bionompy
import re


@vcr.use_cassette("test/vcr_cassettes/test_agent_search_random.yaml")
def test_agent_search_random():
    res = bionompy.agent.search()
    assert re.match(r'^[0-9]+$', res[0]['id'])


@vcr.use_cassette("test/vcr_cassettes/test_agent_search_mary.yaml")
def test_agent_search_mary(q='Mary'):
    res = bionompy.agent.search('Mary')
    for r in res:
        assert 'Mary' in r['name']


@vcr.use_cassette("test/vcr_cassettes/test_agent_get.yaml")
def test_agent_get():
    res = bionompy.agent.get(1)
    assert 'gbif_id' in res[0]
    assert 'https://gbif.org/occurrence/' in res[0]['url']