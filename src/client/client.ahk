#SingleInstance, On
; kudos to AHKsock author
#Include %A_ScriptDir%/net/communicator.ahk

; pretty simple home made code
>^Space::
    history := clipboard
    Send {L-Ctrl + c}
    selected := clipboard
    RunWait, python ./net/manager.py %clipboard%
    FileRead, response, net/temp.txt
    FileDelete, net/temp.txt
    Input response
    clipboard := history
    return
