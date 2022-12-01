*** Settings ***
Resource  resource.robot
Test Setup  Add New Reference  Kirjoittaja Yksi, Kirjoittaja Kaksi  Otsikko  Julkaisija  2000  0000  

*** Test Cases ***
Export All References Succesfully To A Bibtex File
    Input Export Command
    Input  Tiedostonimi
    Run Application
    Output Should Contain  Viitteet viety tiedostoon: Tiedostonimi.bib!

*** Keywords ***
