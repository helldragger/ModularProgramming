#SingleInstance, On
#Include %A_ScriptDir%
; pretty simple home made code
>^Space::
    history := %Clipboard%
    Send {L-Ctrl + c}
    selected := %Clipboard%
    answer := query_algo(selected)
    If !(answer := -1)
    {
        Input answer
    }
    %Clipboard% := history
    return