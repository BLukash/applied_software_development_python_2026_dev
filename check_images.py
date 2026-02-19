import urllib.request
import urllib.error
import ssl

# Disable SSL verification for simpler testing
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    # Exception Hierarchy / Common Exceptions
    ("https://intellipaat.com/blog/wp-content/uploads/2018/12/7.png", "exception handling - intellipaat"),
    ("https://intellipaat.com/mediaFiles/2018/12/2.jpg", "exception handling diagram - intellipaat"),
    ("https://intellipaat.com/blog/wp-content/uploads/2018/12/6.png", "exception handling 3 - intellipaat"),
    ("https://www.guru99.com/images/Pythonnew/Python18.1.png", "exception - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python18.2.png", "exception 2 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python18.3.png", "exception 3 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python18.4.png", "exception 4 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python18.5.png", "exception 5 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python18.6.png", "exception 6 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python18.7.png", "exception 7 - guru99"),

    # Package Structure
    ("https://cdn.programiz.com/sites/tutorial2program/files/packages-in-python.png", "package structure - programiz"),
    ("https://cdn.programiz.com/sites/tutorial2program/files/PackageModuleStructure.jpg", "package module structure - programiz"),

    # Modules / Import
    ("https://www.guru99.com/images/2/062620_0748_PythonImpor1.png", "import module - guru99"),
    ("https://www.guru99.com/images/2/062620_0748_PythonImpor2.png", "import module 2 - guru99"),
    ("https://www.guru99.com/images/2/062620_0748_PythonImpor3.png", "import module 3 - guru99"),
    ("https://upload.wikimedia.org/wikipedia/commons/c/c5/Python-embedding-and-extending.png", "embedding extending - wikimedia"),

    # Python Docs
    ("https://docs.python.org/3/_images/pathlib-inheritance.png", "pathlib inheritance - python docs"),
    ("https://docs.python.org/3/_images/social_previews/summary_library_exceptions_cda5f1b3.png", "exceptions social preview - python docs"),
    ("https://docs.python.org/3/_images/social_previews/summary_tutorial_modules_2da1f578.png", "modules social preview - python docs"),
    ("https://docs.python.org/3/_images/social_previews/summary_reference_import_dba6a9f9.png", "import social preview - python docs"),

    # Python Logo / Standard Library
    ("https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg", "python wordmark - wikimedia"),
    ("https://upload.wikimedia.org/wikipedia/commons/1/1f/Python_logo_01.svg", "python logo - wikimedia"),
    ("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png", "python logo png - wikimedia"),
    ("https://docs.python.org/3/_static/py.svg", "python logo - python docs"),

    # W3Schools
    ("https://www.w3schools.com/python/img_tryexcept.png", "try except - w3schools"),

    # Name Main
    ("https://www.guru99.com/images/Pythonnew/Python19.1.png", "name main - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python19.2.png", "name main 2 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python19.3.png", "name main 3 - guru99"),

    # Additional Guru99 module images
    ("https://www.guru99.com/images/Pythonnew/Python15.1.png", "modules 1 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python15.2.png", "modules 2 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python15.3.png", "modules 3 - guru99"),

    # Docstring
    ("https://www.guru99.com/images/Pythonnew/Python14.1.png", "docstring 1 - guru99"),
    ("https://www.guru99.com/images/Pythonnew/Python14.2.png", "docstring 2 - guru99"),

    # Additional sources
    ("https://dotnettutorials.net/wp-content/uploads/2020/02/word-image-79.png", "exception hierarchy - dotnettutorials"),
    ("https://dotnettutorials.net/wp-content/uploads/2020/02/word-image-80.png", "exception types - dotnettutorials"),
    ("https://dotnettutorials.net/wp-content/uploads/2020/02/word-image-81.png", "exception handling - dotnettutorials"),

    # Specific exception hierarchy diagrams
    ("https://dotnettutorials.net/wp-content/uploads/2023/06/word-image-35016-1.png", "exception hierarchy - dotnettutorials 2023"),
    ("https://dotnettutorials.net/wp-content/uploads/2023/06/word-image-35016-2.png", "exception classes - dotnettutorials 2023"),

    # Scaler / InterviewBit images
    ("https://d1m75rqqgiw2fn.cloudfront.net/wp-data/2021/04/02151831/image-45.png", "python diagram - scaler cf"),
    ("https://d1m75rqqgiw2fn.cloudfront.net/wp-data/2020/12/14112405/image-33.png", "python modules - scaler cf"),

    # Geekflare / similar
    ("https://geekflare.com/wp-content/uploads/2023/02/Python-Exception-Handling-1200x675.png", "exception handling - geekflare"),
]

for url, desc in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, context=ctx, timeout=10)
        ct = resp.headers.get('Content-Type', '')
        cl = resp.headers.get('Content-Length', '?')
        if 'image' in ct or url.endswith('.svg'):
            print(f"OK  | {ct:30s} | {cl:>10s} bytes | {desc:45s} | {url}")
        else:
            print(f"NOT_IMAGE | {ct:30s} | {desc:45s} | {url}")
    except Exception as e:
        print(f"FAIL | {str(e)[:50]:50s} | {desc:45s} | {url}")
