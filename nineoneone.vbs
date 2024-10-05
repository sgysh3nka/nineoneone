Do
Set WMP = WScript.CreateObject("MediaPlayer.MediaPlayer","WMP_")
WMP.Open "%TMP%\nineoneone\911.mp3"
WMP.Play
WScript.Sleep 1000
Loop
