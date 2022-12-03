$date= get-date
out-file -filepath C:\TestingPowershell\MasterFiles.txt -inputObject ("Archivos encontrados hasta el dia de la fecha: " + $date)
Get-ChildItem -recurse .\TestingPowershell | where{$_.Name -match "type" } | foreach {
$_.DirectoryName + "\" + $_.Name} | out-file -filepath C:\TestingPowershell\MasterFiles.txt -append