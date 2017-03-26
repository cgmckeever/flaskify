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

Allows for compartmentalized application resources. [Read more](https://realpython.com/blog/python/python-virtual-environments-a-primer/)

`pip install virtualenv`

## Flask

The Packages

`pip install ipython`
`pip install flask`
`pip install flask-wtf`
`pip install flask-sqlalchemy`
`pip install sqlalchemy-migrate`

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

# References

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- https://github.com/pallets/flask/wiki/Large-app-how-to
- http://flask.pocoo.org/docs/0.12/tutorial/
- https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one













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