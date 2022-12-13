*** Settings ***
Resource  resource.robot

*** Test Cases ***
Create New Book Reference Successfully
    Input New Book Command
    Input Book Reference Details  Sukunimi, Etunimi  Otsikko  Julkaisija  2000  9780596520687  
    Input Exit Command
    Run Application
    Output Should Contain  Uusi kirjaviite on lisätty!

Create New Article Reference Successfully
    Input New Article Command
    Input Article Reference Details  Sukunimi, Etunimi  Otsikko  Julkaisija  2000  Lehti  6  2  38-46
    Input Exit Command
    Run Application
    Output Should Contain  Uusi artikkeliviite on lisätty!

Create New Inproceedings Reference Successfully
    Input New Inproceedings Command
    Input Inproceedings Reference Details  Sukunimi, Etunimi  Otsikko  Julkaisija  2000  Kirjaotsikko  3-14
    Input Exit Command
    Run Application
    Output Should Contain  Uusi konferenssiviite on lisätty!

Delete Reference Successfully
    Input New Book Command
    Input Book Reference Details  Sukunimi, Etunimi  Otsikko  Julkaisija  2000  9780596520687
    Input Delete Command
    Input Delete Details  0
    Input Exit Command
    Run Application
    Output Should Contain  Viite poistettu!

*** Keywords ***
