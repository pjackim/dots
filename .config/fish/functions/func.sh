#!/bin/bash


# 1 - name
# 2 - arry of commands

makeFunc () {
    touch "$1.fish"
    echo "" > "$1.fish"
    
    cmd=()
    for var in "$@"
    do
        cmd+=("$var")
    done

    echo ${cmd[1]}

    echo "function ${cmd[0]}" > "$1.fish"

    length=${#cmd[@]}
    

    for (( j=1; j<=${length}; j+=2 ));
    do
        apnd "    ${cmd[$j]} ${cmd[$j+1]}" "$1.fish"
    done


    apnd "end" "$1.fish"
}

makeCDFunc () {
    touch "$1.fish"
    echo "function $1" > "$1.fish"
    apnd "    if count \$argv > /dev/null" "$1.fish"
    apnd "        cd \$HOME/$2\$argv" "$1.fish"
    apnd "    else" "$1.fish"
    apnd "        cd \$HOME/$2 \$argv" "$1.fish"
    apnd "    end" "$1.fish"   
    apnd "end" "$1.fish"
}

makeEmptyFunc () {
    touch "$1.fish"
    echo "function $1" > "$1.fish"
    apnd "    if count \$argv > /dev/null" "$1.fish"
    apnd "        " "$1.fish"
    apnd "    else" "$1.fish"
    apnd "        " "$1.fish"
    apnd "    end" "$1.fish"   
    apnd "end" "$1.fish"
}

apnd () {
    echo "$1" >> $2
}

# 1 - Name
CreateShortCut () {
    cwd=$(pwd)
    fishfunctions
    touch "$1.fish"
    echo "function $1" > "$1.fish"
    apnd "cd $cwd"
    apnd "end"
}

if [ $# -eq 0 ]
then
    echo "need args"
    exit
fi

name=$1
cmd=()

if [ $# -eq 1 ]
then
    makeEmptyFunc $name
    exit
fi


if [ $# -eq 2 ]
then
    makeCDFunc $name $2
else
    cnt=1
    for var in "$@"
    do
        if [ $cnt -ne 1 ]
        then
            cmd+=("$var")
            #echo $var
        fi
        cnt=$((cnt+1))
    done
    #echo $cmd
    makeFunc $name $cmd
fi




#fileName="$name.fish"
#touch $fileName

#echo "function $name" > $fileName

#if [[ $cmd == "cd" ]]
#then
#    arg="$HOME/$arg"
#else
#    arg="$arg "
#fi 

#if [[ $type -eq 0 ]] #regular line
#then

#    echo "    $cmd $arg\$argv" >> $fileName
#fi

#if [[ $type -eq 1 ]] #function call
#then
#    echo "    $cmd $arg" >> $fileName
#fi

#if [[ $type -eq 2 ]] #idk yer
#then
#    echo "    $cmd $arg\$argv" >> $fileName
#fi




#echo "end" >> $fileName
