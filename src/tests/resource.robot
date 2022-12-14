*** Settings ***
Library  ../RobotLibrary.py

*** Keywords ***
Input New Book Command
    Input  0
    Input  0

Input New Article Command
    Input  0
    Input  1

Input New Inproceedings Command
    Input  0
    Input  2

Input List Command
    Input  1

Input Export Command
    Input  2

Input Delete Command
    Input  4

Input Keyword Command
    Input  5

Input Doi Command
    Input  6

Input New Filter Command
    Input  7

Input Delete Filter Command
    Input  8

Input Get All Information Command
    Input  9

Input Exit Command
    Input  10

Input Book Reference Details
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  ${isbn}
    Input  ${author}
    Input  ${EMPTY}
    Input  ${title}
    Input  ${publisher}  
    Input  ${year}  
    Input  ${isbn}

Input Book Reference Two Authors Details
    [Arguments]  ${author1}  ${author2}  ${title}  ${publisher}  ${year}  ${isbn}
    Input  ${author1}
    Input  ${author2}
    Input  ${EMPTY}
    Input  ${title}
    Input  ${publisher}  
    Input  ${year}
    Input  ${EMPTY}

Input Article Reference Details
    [Arguments]  ${author}  ${title}  ${publisher}  ${year}  ${journal}  ${volume}  ${number}  ${pages}
    Input  ${author}
    Input  ${EMPTY}
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
    Input  ${EMPTY}
    Input  ${title}
    Input  ${publisher}
    Input  ${year}
    Input  ${book_title}
    Input  ${pages}

Input One Filter Details
    [Arguments]  ${first_filter}
    Input  ${first_filter}
    Input  ${EMPTY}

Input Two Filters Details
    [Arguments]  ${first_filter}  ${second_filter}
    Input  ${first_filter}
    Input  ${second_filter}
    Input  ${EMPTY}

Input Delete Details
    [Arguments]  ${reference}
    Input  ${reference}

Input Keyword Details
    [Arguments]  ${keyword}
    Input  ${keyword}
    Input  ${EMPTY}

Input Reference All Information Details
    [Arguments]  ${id}
    Input  ${id}

Input Reference By Doi Details
    [Arguments]  ${doi}
    Input  ${doi}
