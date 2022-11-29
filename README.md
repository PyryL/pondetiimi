# Pöndetiimi

[Ohjelmistotuotanto](https://ohjelmistotuotanto-hy.github.io/miniprojekti/)-kurssin projektityö.

[ProductBacklog](https://docs.google.com/spreadsheets/d/1GRM8AXspv3U0oPStXTyR-001euZUgXl-X6GAkoWaCAw/edit#gid=0)

## Dokumentaatio

[ProductBacklog](https://docs.google.com/spreadsheets/d/1GRM8AXspv3U0oPStXTyR-001euZUgXl-X6GAkoWaCAw/edit#gid=0)

[Definition of Done](https://github.com/PyryL/pondetiimi/blob/main/documentation/definition_of_done.md)

## Asennus ja Käynnistys

Asenna tarvittavat riippuvuudet komennolla:

      poetry install

Sovellus käynnistyy komennolla:

      poetry run invoke start

## Muut toiminnot:

### Testaus:

      poetry run invoke test

### Testikattavuus ja testikattavuusraportti:

      poetry run invoke coverage

      poetry run invoke coverage-report

### Pylint

Laatutarkastukset:

      poetry run invoke lint

