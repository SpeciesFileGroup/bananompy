import vcr
import bionompy


@vcr.use_cassette("test/vcr_cassettes/test_suggest.yaml")
def test_suggest():
    res = bionompy.suggest('Mary Agnes Chas')
    assert 'Q3822242' == res[0]['wikidata']


@vcr.use_cassette("test/vcr_cassettes/test_suggest_private.yaml")
def test_suggest_private():
    res = bionompy.suggest('Mary Agnes Chas', is_public=False)
    assert 'Q3822242' != res[0]['wikidata']
