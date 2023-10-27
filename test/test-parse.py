import vcr
import bananompy


@vcr.use_cassette("test/vcr_cassettes/test_parse.yaml")
def test_parse():
    "parse - basic test"
    res = bananompy.parse('Henry Robert Nicollon des Abbayes; Groom Q\r\nMrs. John Errol Chandos Aberdeen')
    assert 'Henry Robert Nicollon des Abbayes; Groom Q' == res[0]['original']


@vcr.use_cassette("test/vcr_cassettes/test_parse.yaml")
def test_parse_0_family_0():
    res = bananompy.parse('Henry Robert Nicollon des Abbayes; Groom Q\r\nMrs. John Errol Chandos Aberdeen')
    assert 'Abbayes' == res[0]['parsed'][0]['family']


@vcr.use_cassette("test/vcr_cassettes/test_parse.yaml")
def test_parse_0_given_0():
    res = bananompy.parse('Henry Robert Nicollon des Abbayes; Groom Q\r\nMrs. John Errol Chandos Aberdeen')
    assert 'Henry Robert Nicollon' == res[0]['parsed'][0]['given']


@vcr.use_cassette("test/vcr_cassettes/test_parse.yaml")
def test_parse_0_particle_0():
    res = bananompy.parse('Henry Robert Nicollon des Abbayes; Groom Q\r\nMrs. John Errol Chandos Aberdeen')
    assert 'des' == res[0]['parsed'][0]['particle']


@vcr.use_cassette("test/vcr_cassettes/test_parse.yaml")
def test_parse_0_family_1():
    res = bananompy.parse('Henry Robert Nicollon des Abbayes; Groom Q\r\nMrs. John Errol Chandos Aberdeen')
    assert 'Groom' == res[0]['parsed'][1]['family']


@vcr.use_cassette("test/vcr_cassettes/test_parse.yaml")
def test_parse_0_given_1():
    res = bananompy.parse('Henry Robert Nicollon des Abbayes; Groom Q\r\nMrs. John Errol Chandos Aberdeen')
    assert 'Q.' == res[0]['parsed'][1]['given']


@vcr.use_cassette("test/vcr_cassettes/test_parse.yaml")
def test_original_1():
    res = bananompy.parse('Henry Robert Nicollon des Abbayes; Groom Q\r\nMrs. John Errol Chandos Aberdeen')
    assert 'Mrs. John Errol Chandos Aberdeen' == res[1]['original']