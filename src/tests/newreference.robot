*** Settings ***
Resource  resource.robot

*** Test Cases ***
Create New Book Reference Successfully
    Input New Book Command
    Input Reference Details  Sukunimi, Etunimi  Otsikko  Julkaisija  2000  9780596520687  
    Input Exit Command
    Run Application
    Output Should Contain  Uusi kirjaviite on lisätty!

*** Keywords ***
