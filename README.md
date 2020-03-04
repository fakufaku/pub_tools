pubtools
========

A bunch of tools to solve some specific problems when editing papers using latex.
The tools require python3.


`dedupe.py`
-----------

Automatically find repeated words like *the the*

`find_images.py`
----------------

Automatically finds the files for all the images included in a latex document.

Can be used with a pipe to consolidate all the images to a local folder.

```
mkdir ./figures
python find_images.py my_pub.tex | xargs -J % cp % figures/
```

`parenthesis_check.py`
----------------------

Program that checks the balance of parenthesis
