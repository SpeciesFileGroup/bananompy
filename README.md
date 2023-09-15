# Bionompy

This is a Python wrapper on the [Bionomia](https://bionomia.net) API. Code follow the spirit/approach of the [pygbif](https://github.com/gbif/pygbif/graphs/contributors) package, and indeed much of the wrapping utility is copied 1:1 from that repo, thanks [@sckott](https://github.com/sckott) and other [contributors](https://github.com/gbif/pygbif/graphs/contributors).

## Installation

Add this line to your application's requirements.txt:

```python
bionompy
```

And then execute:

    $ pip install -r requirements.txt

Or install it yourself as:

    $ pip install bionompy

## Usage


Import the library:
```
import bionompy
```

---
### Suggest Collector Names
Get collector name suggestions with a limit of 5:
```python
bionompy.suggest('Smith, Ja', limit=5) #  => MultiJson object
```
Filter suggestions to only public profiles
```python
bionompy.suggest('Smith, Ja', is_public=True) #  => MultiJson object
```
Filter suggestions to only people that have occurrences associated with them:
```python
bionompy.suggest('Smith, Ja', has_occurrences=True) #  => MultiJson object
```

---
### Search Collectors
Search for a collector by name:
```python
bionompy.person.search('Mary Agnes Chase') #  => MultiJson object
```

Filter the people search by taxonomic families_collected or taxonomic families_identified. If strict is set to true, then matches must include the taxonomic families.
```python
bionompy.person.search('Mary Agnes Chase', families_collected='Poaceae', strict=True) #  => MultiJson object
```
```python
bionompy.person.search('Mary Agnes Chase', families_identified='Poaceae', strict=True) #  => MultiJson object
```

Filter the search by whether the person was living on the specimen collection/identification date. If strict is set to true, it requires that they were alive on the date.
```python
bionompy.person.search('Smith', date='1580-01-02', strict=True) #  => MultiJson object
```

Setting the callback parameter returns [JSON-P](https://en.wikipedia.org/wiki/JSONP) wrapped in the provided callback string.
```python
bionompy.person.search('Smith', callback='myFunction') #  => JSON-P object
```

Use the page parameter for pagination of the search results:
```python
bionompy.person.search('Smith', page=2) #  => MultiJson object
```

---
### Search Occurrences
Search for occurrences by [GBIF](https://gbif.org) [datasetID](https://www.gbif.org/dataset/f86a681d-7db8-483b-819a-248def18b70a) and [occurrenceID](https://www.gbif.org/occurrence/1804069383):
```python
bionompy.occurrence.search('f86a681d-7db8-483b-819a-248def18b70a', '7a1daa39-8d7c-d7c4-968f-799d58b3c7b0') #  => MultiJson object
```
Setting the callback parameter returns [JSON-P](https://en.wikipedia.org/wiki/JSONP) wrapped in the provided callback string.
```python
bionompy.occurrence.search('f86a681d-7db8-483b-819a-248def18b70a', '7a1daa39-8d7c-d7c4-968f-799d58b3c7b0', callback='myFunction') #  => JSON-P object
```

---
### Collectors
Get a person's profile by their [ORCID](https://orcid.org/) or [WikiData](https://wikidata.org) identifiers:
```python
bionompy.person.get('0000-0001-7618-5230') #  => JSON-LD object
```
---
### Specimens
Get a person's specimens by their [ORCID](https://orcid.org/) or [WikiData](https://wikidata.org) identifiers. Use the page parameter for pagination.
```python
bionompy.person.get('0000-0001-7618-5230', specimens=True) #  => JSON-LD object
```

```python
bionompy.person.get('0000-0001-7618-5230', specimens=True, csv=True) #  => comma-separated values
```
---
### Occurrences
Get an occurrence with a [GBIF](https://www.gbif.org/occurrence/search) occurrenceID:
```python
bionompy.occurrence.get('477976412') #  => JSON-LD object
```
---
### Parsing human names
**Note:** [Bionomia](https://bionomia.net) provides a RESTful API for the human name parsing [dwc_agent](https://rubygems.org/gems/dwc_agent) gem which uses the [namae](https://rubygems.org/gems/namae) gem, and you likely will get better performance using those gems directly if parsing a large number of human names. A similar library in Python to the namae Ruby gem is [nameparser](https://github.com/derek73/python-nameparser).

Parse authorships with names separated by `;` and each authorship set separated by `\r\n`:
```python
bionompy.parse(names='Henry Robert Nicollon des Abbayes; Groom Q\r\nMrs. John Errol Chandos Aberdeen') #  => MultiJson object
```

---
### Agent Strings
Agent strings are people names from occurrence labels that have not been associated with a person's identifier yet.

**Note:** There is no restful API for agent strings, so these methods use beautifulsoup4 and the lxml parser to scrape the values from the Bionomia website.

Get a random list of agent strings:
```python
bionompy.agent.search()
```

Search for an agent string with the query, q:
```python
bionompy.agent.search(q='Mary Agnes')
```

Get an agent string's occurrences by ID (***Warning:*** The agent string identifiers are temporary and can periodcially change when new agent strings are imported into Bionomia.)
```python
bionompy.agent.get('4746282')
```

---

## Development

After checking out the repo, change into the package directory `cd bionompy`, run `pip install .` to install the package, and `pip install -r requirements.txt` to install the dependencies. Then, run `pytest` to run the tests. You can also run `bin/console` for an interactive Python prompt that will allow you to experiment with the above example commands.

## Other Bionomia Libraries

* Ruby Gem: [bananomia](https://github.com/SpeciesFileGroup/bananomia)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/SpeciesFileGroup/bionompy. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://github.com/SpeciesFileGroup/bionompy/blob/main/CODE_OF_CONDUCT.md).

## License

The package is available as open source under the terms of the [NCSA/Illinois](https://github.com/SpeciesFileGroup/bionompy/blob/main/LICENSE.txt) license. You can learn more about the NCSA license on [Wikipedia](https://en.wikipedia.org/wiki/University_of_Illinois/NCSA_Open_Source_License) and compare it with other open source licenses at the [Open Source Initiative](https://opensource.org/license/uoi-ncsa-php/).

## Code of Conduct

Everyone interacting in the Bionompy project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/SpeciesFileGroup/bionompy/blob/main/CODE_OF_CONDUCT.md).
