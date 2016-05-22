#!/bin/bash

OS=$( uname -s )
if [[ -z ${OS} ]];
then
    echo "Sorry, but we cannot get your OS."
    echo "Let's try the virtual environment by yourself."
    return 1;
else
    echo "Your OS: ${OS}"
fi

# Add git-hook
$( ln -fs ../tools/pre-commit.sh .git/hooks/pre-commit )
$( chmod +x .git/hooks/pre-commit )

RESULT=$( virtualenv --version )
if [ ${RESULT} ]
then
    echo "Virtualenv has $RESULT version"
    virtualenv .venv -p python2.7
else
    echo "Installing virtualenv."
    pip install virtualenv
fi

echo "To activate the virtual environment run following command:"
case ${OS} in
    Darwin*|Linux*)
        echo ">> . .venv/bin/activate"
        ;;
    CYGWIN*|MSYS*)
        echo ">> .venv/Scripts/activate.bat"
        ;;
    MINGW*)
        echo ">> . .venv/Scripts/activate"
        ;;
    *)
        echo ">> Try googling... :("
        ;;
esac
