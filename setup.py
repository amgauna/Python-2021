$ pip install --upgrade requests
$ pip wheel --global-option bdist_ext --global-option -DFOO wheel
$ pip install --no-index --find-links=/tmp/wheelhouse SomePackage

# write the file
(shiny_new_env)$ pip freeze > requirements.txt

# show the contents
(shiny_new_env)$ cat requirements.txt
