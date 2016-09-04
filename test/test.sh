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
