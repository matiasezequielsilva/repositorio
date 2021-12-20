Get-ChildItem C:\TestingPowershell -recurse 
| Where {$_.Name -match "typeA"} | Remove-Item