# Fill-Paper
This repo is for filling arxiv's meta info into paper of my google spreadsheet.

## Command

```bash
# set fill-paper in bin
$ make ~/bin
$ git clone https://github.com/wataoka/fill-paper.git
$ mv fill-paper ~/bin

# setup env
$ cd ~/bin/fill-paper
$ pipenv install

# setup for command
$ chmod 777 ~/bin/fill-paper/fill-paper.sh
$ echo 'alias fill-paper="~/bin/fill-paper/fill-paper.sh"' >> ~/.zshrc
$ source ~/.zprofile

# use fill-paper command
$ fill-paper
```