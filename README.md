# Pöndetiimi

[![workflow](https://github.com/PyryL/pondetiimi/actions/workflows/main.yml/badge.svg)](https://github.com/PyryL/pondetiimi/actions)
[![codecov](https://codecov.io/gh/PyryL/pondetiimi/branch/main/graph/badge.svg?token=AHLKDBZ3U2)](https://codecov.io/gh/PyryL/pondetiimi)
[![GitHub](https://img.shields.io/github/license/PyryL/pondetiimi)](LICENSE.md)

[Ohjelmistotuotanto](https://ohjelmistotuotanto-hy.github.io/miniprojekti/)-kurssin projektityö.

## Release

[Release 1.0.0](https://github.com/PyryL/pondetiimi/releases/tag/v1.0.0)

## Dokumentaatio

* [Product backlog](https://docs.google.com/spreadsheets/d/1GRM8AXspv3U0oPStXTyR-001euZUgXl-X6GAkoWaCAw/edit#gid=0)
* [Definition of Done](https://github.com/PyryL/pondetiimi/blob/main/documentation/definition_of_done.md)
* [Testikattavuusraportti](https://codecov.io/gh/PyryL/pondetiimi)
* [Tietokantakaavio](https://github.com/PyryL/pondetiimi/blob/main/documentation/SQLschema.md)
* [Loppuraportti](https://docs.google.com/document/d/1NGq4D4_lWeWqwAMPBDuQXn7lVAadm7DpNlLkhF85MLM/edit)

## Asennus ja käynnistys

Asenna tarvittavat riippuvuudet komennolla:

```
poetry install
```

Sovellus käynnistyy komennolla:

```
poetry run invoke start
```

## Muut toiminnot

### Testaus

```
poetry run invoke test
```

### Testikattavuus ja testikattavuusraportti:

```
poetry run invoke coverage
```

```
poetry run invoke coverage-report
```

### Pylint

Laatutarkastukset:

```
poetry run invoke lint
```

## Lisenssi

<img src='documentation/gplv3-or-later.svg'></img>

[GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.html)
