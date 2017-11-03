# RamPyPackage
Self-wrote-python-packaging (for testing)


OUR PACKAGE TREE HIERARCHY,



______________________
|RamPyPackage FOLDER |
|--------------------|
    |
    |--subdir1 FOLDER
    |        |---- subsubdir1 FOLDER
    |        |        |------ bottom_of_subsubdir1.py
    |        |        |______ __init__.py
    |        |
    |        |---- intermediate_from_subdir1.py
    |        |
    |        |---- intermediate_2_from_subdir1.py
    |        |
    |        |____ __init__.py
    |
    |--subdir2 FOLDER
    |        |---- bottom_of_subdir2.py
    |        |---- test.py
    |        |____ __init__.py
    |
    |__ __init__.py


    ** hey_stay_here_and_try_all_comb **


Hints :-

1. __all__ declaration is not necessary.
2. __init__.py should be there to import all necessary modules when
installing the package.
3. for importing the sub directories (not files),
    from . import subdir1
        is enough
4. for importing the sub file(module),
    from .sub_module import sub_module
        is better, if the sub_module is a class on the sub module file.
5. no need to start the importing of the sub-modules in our current script
   by starting from top package name.
        from Top_package.sub1.sub12 import sub12
            This is not necessary to include Top_package at the front.
            Just the below line is enough.
                from sub1.sub12 import sub12
