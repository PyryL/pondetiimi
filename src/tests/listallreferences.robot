*** Settings ***
Resource  resource.robot

Test Setup  Add New Reference  Kirjoittaja Yksi, Kirjoittaja Kaksi  Otsikko  Julkaisija  2000  0000  

*** Test Cases ***
List All References Successfully
    Input List Command
    Input Exit Command
    Run Application
    Output Should Contain  Nro
    Output Should Contain  Kirjoittajat
    Output Should Contain  Otsikko
    Output Should Contain  Vuosi

Add One Filter Successfully
    Input New Filter Command
    Input One Filter Details  Yksi
    Input Exit Command
    Run Application
    Output Should Contain  Filttereiden syöttö lopetettu

Add Multiple Filters Successfully
    Input New Filter Command
    Input Two Filters Details  Yksi  Otsikko
    Input Exit Command
    Run Application
    Output Should Contain  Filttereiden syöttö lopetettu

Delete All Filters Successfully
    Input Delete Filter Command
    Input Exit Command
    Run Application
    Output Should Contain  Filtterit poistettu!

List Reference All Information Successfully
    Input Get All Information Command
    Input Reference All Information Details  0
    Input Exit Command
    Run Application
    Output Should Contain  Yksi
    Output Should Contain  Kaksi
    Output Should Contain  Otsikko
    Output Should Contain  Julkaisija
    Output Should Contain  2000
    Output Should Contain  0000
    Output Should Contain  YksiOtsikko2000

*** Keywords ***
