#!/usr/bin/env bats

@test "f commands passing" {
   eval "echo | f commands"
   [ $? -eq 0 ] 
}

@test "f list equal to standard ls" { 
   [[ $(echo | f list ~)  == $(ls ~) ]]
}

@test "f swap ~/fTerm-dev/test/swap/a ~/fTerm-dev/test/swap/b" {
    # read files to swap
    a=$(cat ~/fTerm-dev/test/swap/a)
    b=$(cat ~/fTerm-dev/test/swap/b)

    # swap files
    echo | f swap ~/fTerm-dev/test/swap/a ~/fTerm-dev/test/swap/b
    
    # check that files are swapped
    [[ "$(cat ~/fTerm-dev/test/swap/a)" == $b ]] && [[ "$(cat ~/fTerm-dev/test/swap/b)" == $a ]]
}

@test "f read a file" {
    [ "$(cat ~/fTerm-dev/test/read/a.txt)" == "hello" ]
}

@test "f help commands" {
    [ "$(echo | f help commands)" == "[f] List all fTerm commands, tabulated." ]
}

@test "f temp passing" {
    eval "echo | f temp"
    [ $? -eq 0 ]
}

@test "f delete" {
    touch ~/fTerm-dev/test/delete/a
    [ echo | f delete ~/fTerm-dev/test/delete/a -eq ""]
}

@test "f addline + f removeline" {
   a=$(cat ~/fTerm-dev/test/addline,removeline/a)
   echo | f addline ~/fTerm-dev/test/addline,removeline/a hello
   b=$(cat ~/fTerm-dev/test/addline,removeline/a)
   echo | f removeline cat ~/fTerm-dev/test/addline,removeline/a 0
   c=$(cat ~/fTerm-dev/test/addline,removeline/a)
   [[ a="" ]] && [[ b="hello" ]] && [[ c="" ]]
}
