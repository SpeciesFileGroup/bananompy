import vcr
import bananompy
from dateutil.parser import parse


@vcr.use_cassette("test/vcr_cassettes/test_person_search.yaml")
def test_search_person_basic():
    "person.search - basic test"
    res = bananompy.person.search('Mary Agnes Chase', families_collected='Poaceae', families_identified='Poaceae', strict=True)
    assert "dict" == res.__class__.__name__
    assert 'Mary+Agnes+Chase' in res['as:first']
    assert res['opensearch:totalResults'] > 0


@vcr.use_cassette("test/vcr_cassettes/test_person_search2.yaml")
def test_search_person_basic2():
    "person.search - basic test 2"
    res = bananompy.person.search('smith', families_collected='scarabaeidae', strict=True)
    assert 'Andrew B.T. Smith' == res['dataFeedElement'][0]['item']['name']


@vcr.use_cassette("test/vcr_cassettes/test_person_search_strict.yaml")
def test_search_person_strict():
    "person.search - strict test"
    strict_false = bananompy.person.search('Mary Agnes Chase', families_collected='Poaceae', families_identified='Poaceae', strict=False)
    strict_true = bananompy.person.search('Mary Agnes Chase', families_collected='Poaceae', families_identified='Poaceae', strict=True)
    assert strict_false['opensearch:totalResults'] > strict_true['opensearch:totalResults']


@vcr.use_cassette("test/vcr_cassettes/test_person_families_collected.yaml")
def test_search_person_families_collected():
    "person.search - families collected"
    res = bananompy.person.search('Thomas McElrath', families_collected='Acholeplasmataceae', strict=True)
    assert 0 == res['opensearch:totalResults']


@vcr.use_cassette("test/vcr_cassettes/test_person_families_identified.yaml")
def test_search_person_families_identified():
    "person.search - families identified"
    res = bananompy.person.search('Thomas McElrath', families_identified='Acholeplasmataceae', strict=True)
    assert 0 == res['opensearch:totalResults']


@vcr.use_cassette("test/vcr_cassettes/test_person_search_page_limit.yaml")
def test_search_person_page_limit():
    "person.search - pagination test"
    res = bananompy.person.search('Mary Agnes Chase', page=2, limit=1)
    assert res['opensearch:itemsPerPage'] == 1
    assert 'page=2' in res['as:current']


# NOTE: Date filters on alive during date. Increment birth date by 1 day to include them in the search results
@vcr.use_cassette("test/vcr_cassettes/test_person_date.yaml")
def test_search_person_date():
    "person.search - date test"
    search_date = '1580-01-02'
    res = bananompy.person.search('Smith', date=search_date, strict=True)
    for r in res['dataFeedElement']:
        search_date = parse(search_date)
        birth = parse(r['item']['birthDate'])
        death = parse(r['item']['deathDate'])
        assert (search_date >= birth and search_date <= death)


@vcr.use_cassette("test/vcr_cassettes/test_person_callback.yaml")
def test_search_person_callback():
    "person.search - callback test"
    res = bananompy.person.search('Mary Agnes Chase', callback='aldkfjlasfoewhfaefoiefoaef')
    assert 'aldkfjlasfoewhfaefoiefoaef' in res


@vcr.use_cassette("test/vcr_cassettes/test_person_get_profile.yaml")
def test_person_get():
    "person.get - profile test"
    res = bananompy.person.get('0000-0001-7618-5230')
    assert 'Shorthouse, David Peter' == res['alternateName'][0]


@vcr.use_cassette("test/vcr_cassettes/test_person_get_persons_specimens.yaml")
def test_person_wikidata_specimens():
    "person.get - person's specimens test"
    res = bananompy.person.get('Q3822242', specimens=True)
    assert 'PRESERVED_SPECIMEN' == res['@reverse']['identified'][0]['basisOfRecord']


@vcr.use_cassette("test/vcr_cassettes/test_person_get_persons_specimens_csv.yaml")
def test_person_orcid_specimens_csv():
      res = bananompy.person.get('0000-0001-7618-5230', specimens=True, csv=True)
      assert 'action,gbifID,datasetKey' in res

