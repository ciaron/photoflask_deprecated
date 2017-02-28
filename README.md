Create conda env
    conda create -n photo
    conda install flask

Activate:
    source activate photo

Install this module via pip 
    pip install --editable .

Run:

export FLASK_APP=photoflask
export FLASK_DEBUG=true
flask run
