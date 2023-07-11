# Squiggle.tv Patch

This is the patch version of squiggle.tv.

## COMMON ISSUES

### POSTGRES

Ensure the postgres libraries are installed.

https://stackoverflow.com/a/28938258

### PYTHON HEADER ISSUES

Ensure the python3 devel headers are installed

i.e. ubuntu/debian:

```bash
sudo apt-get install python3-devel
```

https://www.google.com/search?client=firefox-b-d&q=install+python3+devel

### REALPATH

Install realpath. 

#### LINUX

```bash
apt-get install realpath
```

#### MACOS

```bash
brew install coreutils # https://stackoverflow.com/a/30267480

alias realpath=grealpath
```


## Getting started

You require Python3 for this.

```bash

python3 -m venv venv

. venv/bin/activate

pip install -e ./app

./run.sh
```

_Note that you may run into a gcc error related to psycopg2 when installing the app on macos, in this case exporting the following variables may help_

```
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"
```

_Note you may also need to install postgres / libq-dev or similar_

## Walkthrough to exploit

1. go to the site and be redirected to a default provider and site, in this case google.com/teapot
2. try `/file:///etc/passwd` or a similar LFI and notice it works
3. no flag this time, the site will simply let a user read any file on your computer.

## Testing

There are no tests, simply fix the code to the best of your ability using your own judgement.
