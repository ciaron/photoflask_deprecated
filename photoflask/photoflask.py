import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , photoflask.py

#app.config.from_envvar('PHOTOFLASK_SETTINGS', silent=True)

allowed_types=['jpg', 'png', 'jpeg']

def get_image_info(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    del(data[1]) # delete the '--' line
    return data # a list of lines from the file.

@app.route('/')
def index():

    content = os.path.join(app.static_folder, 'content')

    galleries = {}

    # get directories at top level
    root, dirs, files = os.walk(content).next()

    for gallery in dirs: # each top-level dir is a gallery
        r,d,filelist = os.walk(os.path.join(root, gallery)).next()

        galleries[gallery] = {}

        # remove anything from filelist that isn't an image
        # if it's the title or description file, add those to the dict

        title = gallery
        desc = ''

        if 'title.txt' in filelist:
            with open(os.path.join(root, gallery, 'title.txt'), 'r') as t:
                for line in t:
                    title = line
        if 'description.txt' in filelist:
            pass

        # remove non-image files from the list
        #for f in filelist:
        #    ext = os.path.basename(f).split('.')[-1]
        #    if ext.lower() not in allowed_types: # i.e. not an image
        #        filelist.remove(f)

        images = {}
        for f in filelist:
            ext = os.path.basename(f).split('.')[-1]
            if ext.lower() in allowed_types: # i.e. not an image

                info = os.path.join(root, gallery, os.path.basename(f).split('.')[0]+'.txt')
                if os.path.exists(info):
                    imgdata=get_image_info(info)
                else:
                    imgdata=["notitle","nodesc"]

                images[f] = {'title':imgdata[0], 'description':imgdata[1:], 'path':url_for('static', filename=os.path.join('content',gallery,f))}

            
        galleries[gallery]={'title':title, 'description':desc, 'images':images}

    return render_template('show_galleries.html', galleries=galleries)
    #return str(galleries)

