$out = Get-ChildItem -Recurse .\TestingPowershell 
| where{ $_.Name -match ".txt"}
$out 
| foreach { 
    $path = $_.DirectoryName+"\"+$_.Name
    
if ($($_.Name.TrimEnd(".txt"))[-1]%2 -eq 0)
{
        $_.Name
        
Move-Item -Path $path -Destination .\TestingPowershell\Folder1
    }
else{
        Move-Item -Path $path 
-Destination .\TestingPowershell\Folder2
    }
}