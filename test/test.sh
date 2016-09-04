#!/usr/bin/env bats

@test "f commands" {
   eval "echo | f commands"
   [ $? -eq 0 ] 
}

@test "f list" { 
   [[ $( echo | f list ~ )  == $(ls ~) ]]
}

@test "f swap" {
    # read files to swap
    a=$(cat ~/fTerm-dev/test/swap/a)
    b=$(cat ~/fTerm-dev/test/swap/b)

    # swap files
    echo | f swap ~/fTerm-dev/test/swap/a ~/fTerm-dev/test/swap/b
    
    # check that files are swapped
    [[ $(cat ~/fTerm-dev/test/swap/a) == b ]] && [[ $(cat ~/fTerm-dev/test/swap/b) == a ]]
}
