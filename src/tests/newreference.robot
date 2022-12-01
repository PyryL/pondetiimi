*** Settings ***
Resource  resource.robot

*** Test Cases ***
Create New Reference Successfully
    Input New Command
    Input Reference Details  Kirjoittaja Yksi  Otsikko  Julkaisija  2000  0000  
    Output Should Contain  Uusi viite lisätty!

*** Keywords ***
