#!/usr/bin/python

print

print "checking for requests"
try:
    import requests
except ImportError:
    print "you should install requests before continuing"

print "checking for pathlib"
try:
    import pathlib
except ImportError:
    print "you should install pathlib before continuing"

print "checking for tqdm"
try:
    import tqdm
except ImportError:
    print "you should install tqdm before continuing"

print "checking for nltk"
try:
    import nltk
except ImportError:
    print "you should install nltk before continuing"

print "checking for numpy"
try:
    import numpy
except ImportError:
    print "you should install numpy before continuing"

print "checking for scipy"
try:
    import scipy
except:
    print "you should install scipy before continuing"

print "checking for sklearn"
try:
    import sklearn
except:
    print "you should install sklearn before continuing"


print
print "downloading the Enron dataset (this may take a while)"
print "to check on progress, you can cd up one level, then execute <ls -lthr>"
print "Enron dataset should be last item on the list, along with its current size"
print "download will complete at about 423 MB"

import requests
import pathlib
import urllib
import os

from tqdm import tqdm

url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"

# Code adapted & modified from https://tobiasraabe.github.io/blog/how-to-download-files-with-python.html
# Check the above url for including validation while downloading files 

DOWNLOAD_FOLDER = pathlib.Path(os.path.dirname(os.getcwd()))

File = DOWNLOAD_FOLDER / url.split('/')[-1]

file_size_online = int(requests.head(url).headers.get('content-length', 0))


def download(resume_byte_pos = None):
    resume_header = ({"Range": "bytes={}-".format(resume_byte_pos)} if resume_byte_pos else None)

    r = requests.get(url, stream=True, headers=resume_header)

    initial_pos = resume_byte_pos if resume_byte_pos else 0
    
    mode = 'ab' if resume_byte_pos else 'wb'

    with open('../enron_mail_20150507.tar.gz', mode) as f:
        with tqdm(total=file_size_online, unit='B',
                unit_scale=True, unit_divisor=1024,
                desc='enron_mail_20150507.tar.gz', initial=initial_pos,
                ascii=True, miniters=1) as pbar:
            for chunk in r.iter_content(32 * 1024):
                f.write(chunk)
                pbar.update(len(chunk))

if File.exists():
    file_size_offline = File.stat().st_size
    if file_size_online != file_size_offline:
        print "File is incomplete. Resume download."
        download(file_size_offline)
    else:
        print "File is complete. Skip download."
        pass
else:
    print "File does not exist. Start download."
    download()


print "download complete!"
print
print "unzipping Enron dataset (this may take a while)"
import tarfile

os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tar.gz", "r:gz")
tfile.extractall(".")

print "you're ready to go!"
