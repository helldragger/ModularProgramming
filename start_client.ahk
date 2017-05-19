#SingleInstance, On
#Include %A_ScriptDir%\AHKsock.ahk
sServer := "localhost"
sPort := 27015
OnExit, CloseAHKsock
Menu, Tray, Add
Menu, Tray, Add, Exit Gracefully, CloseAHKsock
AHKsock_ErrorHandler("AHKsockErrors")

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

query_algo(selection){
    If (i := AHKsock_Connect(sServer, 27015, "Recv")) {
        OutputDebug, % "AHKsock_Connect() failed with return value = " i " and ErrorLevel = " ErrorLevel
        ExitApp
    }
    Else
    {

    }
    return
}


CloseAHKsock:
    AHKsock_Close()
ExitApp

Recv(sEvent, iSocket = 0, sName = 0, sAddr = 0, sPort = 0, ByRef bData = 0, iLength = 0) {

    If (sEvent = "CONNECTED") {

        ;Check if the connection attempt was succesful
        If (iSocket = -1) {
            OutputDebug, % "Client - AHKsock_Connect() failed. Exiting..."
            ExitApp
        } Else OutputDebug, % "Client - AHKsock_Connect() successfully connected!"

    } Else If (sEvent = "DISCONNECTED") {

        OutputDebug, % "Client - The server closed the connection. Exiting..."
        ExitApp

    } Else If (sEvent = "RECEIVED") {

        ;We received data. Output it.
        OutputDebug, % "Client - We received " iLength " bytes."
        OutputDebug, % "Client - Data: " Bin2Hex(&bData, iLength)
    }
}

AHKsockErrors(iError, iSocket) {
    OutputDebug, % "Client - Error " iError " with error code = " ErrorLevel ((iSocket <> -1) ? " on socket " iSocket : "")
}

