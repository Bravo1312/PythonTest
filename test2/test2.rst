.. code:: robotframework

    *** Settings ***

    *** Test Case ***
    GetTime
        ${t}    get time
        log    ${t}
        sleep    2
        ${t}    get time
        log    ${t}

    TestIf
        ${a}    Set variable    10
        run keyword if    ${a}>=90    log    Very Good!
        ...    ELSE IF    ${a}>=70    log    Good!
        ...    ELSE IF    ${a}>=60    log    Just So So!  

    TestFor
        : FOR    ${i}    IN RANGE    10
        \    log    ${i}

    TestEvaluate
        ${d}    Evaluate    random.randint(1000, 9999)    random
        log    ${d}
