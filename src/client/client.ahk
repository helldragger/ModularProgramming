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
    FileRead, response, temp.txt
    if (ErrorLevel = 0)
    {
        debug.WriteLine(response)
        debug.WriteLine("Deleting temporary file...")
        FileDelete, temp.txt
        if (SubStr(response, 1, 5) = "ERROR")
        {
            MsgBox,,"ERROR",%response%
        }
        else
        {
            debug.WriteLine("Reactivate the editor")
            WinActivate, editor_title, editor_text
            debug.WriteLine("Writing response in place of highlighted text...")
            Loop, Parse, response, `n
            {
                ; A_Index holds the current loop-itteration
                SendInput, %A_LoopField%
                
            }
        
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
