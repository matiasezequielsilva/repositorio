RECORRE LA CARPETA PICTURES

Get-ChildItem -Recurse .\Pictures
-------------------------------------
Elije los archivos que contengan VW y el largo del nombre = 12 guardando en out
$out = Get-ChildItem -Recurse .\Pictures 
| where { $.Name -match "VW" -and $.Name.length -eq 12}