#SingleInstance, Force
SetWorkingDir, %A_ScriptDir%

; pretty simple home made code
+Space::
    debug := FileOpen("*", "w")
    debug.WriteLine("Copying clipboard into history: ")
    debug.WriteLine(clipboard)
    history := clipboard
    debug.WriteLine("Copying highlighted text into clipboard")
    Send ^c
    selected := clipboard
    debug.WriteLine("Clipboard updated: ")
    debug.WriteLine(clipboard)
    debug.WriteLine("Keeping the active editor in memory")
    WinGetTitle, editor_title, A
    WinGetText, editor_text, A
    debug.WriteLine("Launching python client request")
    RunWait, python ./net/manager.py %clipboard%
    debug.WriteLine("Reading database response")
    FileRead, clipboard, temp.txt
    if (ErrorLevel = 0)
    {
        debug.WriteLine(clipboard)
        debug.WriteLine("Deleting temporary file...")
        ; FileDelete, temp.txt
        if (SubStr(clipboard, 1, 5) = "ERROR")
        {
            MsgBox,,"ERROR",%clipboard%
        }
        else
        {
            Send ^v
        }
    }
    else{
        debug.WriteLine("No response issued")
    }
    debug.WriteLine("Replacing clipboard with former value...")
    clipboard := history
    debug.WriteLine("Request completed!")
    return

+Esc::
    ExitApp
