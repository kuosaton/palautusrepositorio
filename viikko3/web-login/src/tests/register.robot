*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  joulupukki
    Set Password  joulu123
    Set Password Confirmation  joulu123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  abcd1234
    Set Password Confirmation  abcd1234
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  abc
    Set Password  abcd123
    Set Password Confirmation  abcd123
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  def
    Set Password  abcdefghijklmnopqrst
    Set Password Confirmation  abcdefghijklmnopqrst
    Submit Credentials
    Register Should Fail With Message  Password must contain both letters (a-z) and numbers (0-9)

Register With Nonmatching Password And Password password_confirmation
    Set Username  ghi
    Set Password  validpassword1234
    Set Password Confirmation  validpasword1234
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Given username already exists

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page