para cada elemento si el 8vo caracter del nombre /2 da resto 0 (es par)
guarda en path el directorio / nombre del archivo
a esto le aplico copy desde el path hasta donde lo quiero copiar
sino son impares
-----------------------------------------------------------------------
$out | foreach {
    if (($_.Name[7]%2) -eq 0)
{
$_.Name
 
Write-Output "Es par"
  
$path = $.DirectoryName+"\"+$.Name

  $path
  Copy-Item -Path $path -Destination .\Desktop\NewPicture
    }
else{
        $_.Name
        Write-Output "es impar"
    }
}

SI MULTIPLICAS UN STRING POR UN NUMERO SE IMPRIME ESA CANTIDAD DE STRINGS.
SI LO TOMAS COMO UNA VARIABLE ENCERRANDO ENTRE ()
EJ:
3 + #= ###
1..10 | foreach{
write-host ("#" * $_) }

#
##
###
####
#####
######
#######
########
#########
##########