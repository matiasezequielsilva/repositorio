en el foreach si la variable no se tiene en cuenta el .* con el TrimEnd(".png")
en este caso,el cursor queda en el ultimo caracter.
X lo que con un [-1] se mira el ultimo caracter
$out = Get-ChildItem -Recurse .\Pictures | 
where { $.Name -match "VW" -and $.Name.length -eq 12}
$out | 
foreach { if ($($_.Name.TrimEnd(".png"))[-1]%2 -eq 0)
{
    Write-Output "Es Par"
    $_.Name
    }
}