pip install requests
pip install --upgrade requests
pip install pip-upgrader
pip install flask
pip install flake8
pip-review --auto
make install-pip-requirements 
pip install --upgrade --force-reinstall -r requirements.txt
pip freeze > requirements.txt
cat requirements.txt
pip install --user --requirement requirements.txt





