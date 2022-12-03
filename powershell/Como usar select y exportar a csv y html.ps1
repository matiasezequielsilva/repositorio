$lastProcess = Get-Process | where{$_.PM -gt 100mb -and $_.CPU -gt 1000 } | select name, id, handlecount
$Last3ProcessToCsv = $lastProcess| select -last 3 | export-csv -Path C:\TestingPowershell\LastProcess.Csv -NoTypeInformation
$last3ProcessToHtml = $lastProcess | select -last 3 | convertTo-html | out-file -FilePath C:\TestingPowershell\LastProcess.html