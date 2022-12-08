*** Settings ***
Library  ../RobotLibrary.py

*** Keywords ***
Input New Book Command
    Input  01

Input List Command
    Input  1

Input Export Command
    Input  2

Input Exit Command
    Input  4

Input Reference Details
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  ${isbn}
    Input  ${author}
    Input  ${title}
    Input  ${publisher}  
    Input  ${year}  
    Input  ${isbn}
