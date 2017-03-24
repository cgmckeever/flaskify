# Pre-requisites

## Homebrew
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## Python 3 /usr/local/bin/python3
`brew install python3`

## PIP (maybe installed with Python)

Python package manager

`sudo easy_install pip`

## XCODE
`xcode-select --install`

## VirtualEnv

Allows for compartmentalized application resources

`pip install virtualenv`

## Flask

The Framework

`pip install ipython`
`pip install flask`
`pip install flask-wtf`
`pip install flask-sqlalchemy`

## autoenv

Allows for automatic boot of VirtualEnv

`brew install autoenv`
`echo "source $(brew --prefix autoenv)/activate.sh" >> ~/.bash_profile`

# Useful tips

## Python Path
`which python`

## Python Verson
`python --version`

## Start VirtualEnv
`virtualenv -p /usr/local/bin/python3 <NAME>`
`source <NAME>/bin/activate`

## Stop VirtualEnv
`deactivate`













===================

BASE_PATH=`dirname "${BASH_SOURCE}"`
PWD=`pwd`

if [[ "${BASE_PATH}" == "${PWD}" ]]
then
 declare -f -F deactivate &>/dev/null

 if [[ "${?}" == "0" ]]
 then
   deactivate
 fi
fi