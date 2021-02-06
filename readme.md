```sh
export PROJECT=mydomain.com
git clone git@github.com:slava-vishnyakov/python-caprover $PROJECT
cd $PROJECT
git checkout orator
rm -rf .git
python3 randomize_ports.py
rm randomize_ports.py
git init
```
