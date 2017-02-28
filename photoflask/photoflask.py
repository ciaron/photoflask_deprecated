import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , photoflask.py

#app.config.from_envvar('PHOTOFLASK_SETTINGS', silent=True)

@app.route('/')
def index():
    # get directories at top level
    root, dirs, files = os.walk(app.static_folder)
    #return os.walk(app.static_folder).next()
    return app.static_folder + "<br/>Dirs: " + " ".join(dirs) + "<br/>Files: " + " ".join(files)

"""
# Print directory tree nicely
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
"""
