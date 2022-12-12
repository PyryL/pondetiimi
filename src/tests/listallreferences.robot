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

*** Keywords ***
