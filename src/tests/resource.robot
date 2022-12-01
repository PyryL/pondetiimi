*** Settings ***
Library  ../RobotLibrary.py

*** Keywords ***
Input New Command
    Input  uusi

Input List Command
    Input  listaa

Input Export Command
    Input  vie

Input Reference Details
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  ${isbn}
    Input  ${author}
    Input  ${title}
    Input  ${publisher}  
    Input  ${year}  
    Input  ${isbn}
    Run Application
