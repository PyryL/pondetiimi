*** Settings ***
Library  ../RobotLibrary.py

*** Keywords ***
Input New Book Command
    Input  01

Input New Article Command
    Input  02

Input New Inproceedings Command
    Input  03

Input List Command
    Input  1

Input Export Command
    Input  2

Input Exit Command
    Input  4

Input Book Reference Details
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  ${isbn}
    Input  ${author}
    Input  ${title}
    Input  ${publisher}  
    Input  ${year}  
    Input  ${isbn}

Input Article Reference Details
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  ${journal}  ${volume}  ${number}  ${pages}
    Input  ${author}
    Input  ${title}
    Input  ${publisher}
    Input  ${year}
    Input  ${journal}
    Input  ${volume}
    Input  ${number}
    Input  ${pages}

Input Inproceedings Reference Details
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  ${book_title}  ${pages}
    Input  ${author}
    Input  ${title}
    Input  ${publisher}
    Input  ${year}
    Input  ${book_title}
    Input  ${pages}
