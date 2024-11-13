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

Login After Successful Registration
    Set Username  marneuscalgar
    Set Password  ihatetyranids1
    Set Password Confirmation  ihatetyranids1
    Submit Credentials
    Register Should Succeed
    Go To Main Page
    Click Button  Logout

    Set Username  marneuscalgar
    Set Password  ihatetyranids1
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  heretic
    Set Password  ilikechaos
    Set Password Confirmation  ilikechaos
    Submit Credentials
    Register Should Fail With Message  Password must contain both letters (a-z) and numbers (0-9)
    Go To Login Page
    Set Username  heretic
    Set Password  ilikechaos
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

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