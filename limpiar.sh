#!/bin/bash
sed -i 's/\s//g' ./datos/datos.txt
sed -i 's/^Messagereceivedfromtopic:\/cp2uqqleflejegvcrcelsil4oslwib\///g' ./datos/datos.txt
sed -i 's/\/attrs->payload:/;/g' ./datos/datos.txt

#borro los espacios
#borro parte del texto y la apikey
#borro mas texto




