import vcr
import bananompy


@vcr.use_cassette("test/vcr_cassettes/test_suggest.yaml")
def test_suggest():
    res = bananompy.suggest('Mary Agnes Chas')
    assert 'Q3822242' == res[0]['wikidata']


@vcr.use_cassette("test/vcr_cassettes/test_suggest_private.yaml")
def test_suggest_private():
    res = bananompy.suggest('Mary Agnes Chas', is_public=False)
    assert 'Q3822242' != res[0]['wikidata']
