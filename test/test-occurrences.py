import vcr
import bionompy


@vcr.use_cassette("test/vcr_cassettes/test_occurrence_search.yaml")
def test_search():
    "occurrence.search - basic test"
    res = bionompy.occurrence.search('f86a681d-7db8-483b-819a-248def18b70a', '7a1daa39-8d7c-d7c4-968f-799d58b3c7b0')
    assert 'PRESERVED_SPECIMEN' == res['dataFeedElement'][0]['item']['basisOfRecord']


@vcr.use_cassette("test/vcr_cassettes/test_occurrence_search_callback.yaml")
def test_search_callback():
    "occurrence.search - callback test"
    res = bionompy.occurrence.search('f86a681d-7db8-483b-819a-248def18b70a', '7a1daa39-8d7c-d7c4-968f-799d58b3c7b0', callback='asldfjasljdfasfa')
    assert 'asldfjasljdfasfa' in res


@vcr.use_cassette("test/vcr_cassettes/test_occurrence_get.yaml")
def test_occurrence():
    "occurrence - get occurrence test"
    res = bionompy.occurrence.get('477976412')
    assert 'PRESERVED_SPECIMEN' == res['basisOfRecord']
