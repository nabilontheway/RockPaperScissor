#! /bin/bash

echo "This Script Will Setup Python Virtual Environment."
read -p "Press Enter to continue"
function setup() {
    
    python3 -m venv .venv
    #spinner
    echo "Task completed!"
    echo "Run Command: source .venv/bin/activate"
    
}

# # Function to display a spinner
# spinner() {
#     local pid=$1
#     local delay=0.1
#     local spinstr='|/-\\'
#     local i=0

#     while kill -0 $pid 2>/dev/null; do
#         printf "\r${spinstr:$i:1}"
#         i=$(( (i+1) % ${#spinstr} ))
#         sleep $delay
#     done
#     printf "\r" # Clear the spinner line
# }

setup