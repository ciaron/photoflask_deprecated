# photoflask

Create conda env
  * conda create -n photo
  * conda install flask

Activate:
  * source activate photo

Install this module via pip 
  * pip install --editable .

Run:

  * export FLASK_APP=photoflask
  * export FLASK_DEBUG=true
  * flask run

# LAYOUT OF FOLDERS AND FILES

The gallery/photo layout should look like this (in the static/ folder)

* gallery1
  * title.txt (optional - defaults to 'gallery1')
  * description.txt (optional)
  * image1.jpg|png
  * image2.jpg|png
  * image3.jpg|png
  * image1.txt (optional - title defaults to image filename, minus extension, i.e. 'image1')

* gallery2
  * title.txt (optional - defaults to 'gallery2')
  * description.txt (optional)

* gallery3
  * title.txt (optional - defaults to 'gallery3')
  * description.txt (optional)

# FORMAT OF IMAGE DESCRIPTION FILES (i.e. <imageN>.txt)
```
The Title of the Image
--
This is the description of this image. It can be as long as you like, but might be truncated
```



Galleries and images are displayed in alphanumeric order. The simplest way to change this order is to add '0_', '1_' etc to the start of the filename
