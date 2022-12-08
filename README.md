# Pöndetiimi

![workflow](https://github.com/PyryL/pondetiimi/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/PyryL/pondetiimi/branch/main/graph/badge.svg?token=AHLKDBZ3U2)](https://codecov.io/gh/PyryL/pondetiimi)

[Ohjelmistotuotanto](https://ohjelmistotuotanto-hy.github.io/miniprojekti/)-kurssin projektityö.

## Dokumentaatio

* [Product backlog](https://docs.google.com/spreadsheets/d/1GRM8AXspv3U0oPStXTyR-001euZUgXl-X6GAkoWaCAw/edit#gid=0)
* [Definition of Done](https://github.com/PyryL/pondetiimi/blob/main/documentation/definition_of_done.md)
* [Testikattavuusraportti](https://codecov.io/gh/PyryL/pondetiimi)

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
