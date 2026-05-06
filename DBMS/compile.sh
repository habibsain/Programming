#! /bin/bash

gxx="g++"
gxxflag="-I . -Wall"
#src=../src/mem.c
src="hyperloglog.cpp"
target=$1
out=${target/.cpp/.x}

if [[ $# -eq 0 ]]; then
    echo "usage: ./compille file.c"
    exit 1   
fi

#flag:
#no flag

#simple compiler script to ease the process
if [[ $target =~ \.cpp$ && $# -eq 1 ]]; then
    
    $gxx $gxxflag $src $target -o $out

elif [[ $target =~ \.cpp$ && $2 -eq 1 ]]; then
    $gxx  $target -o $out

elif [[ $target == clean ]]; then
    rm *.x

else
    echo "usage: ./compille file.c flag(none = Includes mem.h; 1 = without mem.h)"
fi