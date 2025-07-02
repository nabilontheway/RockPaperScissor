#! /bin/bash

PATH = $(path)
VENV_PATH = "/Users/sun/Documents/Projects/RockPaperScissor/.venv"

function setup() {
    
    python3 -m venv .venv
    source "${VENV_PATH}/bin/activate"
    
}
function path(){
    return pwd
}

setup