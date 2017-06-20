#!/usr/bin/env python

# Makefile python script to generate starting dataset.
# NOTE: can't guarantee this will be run on a *nix system,
# so we do everything in python to ensure compatibility

import urllib, os, sys, tarfile, shutil


# setup some vars
url = 'https://urldefense.proofpoint.com/v2/url?u=https-3A__s3.amazonaws.com_demo-2Ddatasets_beer-5Freviews.tar.gz&d=DwMFaQ&c=imBPVzF25OnBgGmVOlcsiEgHoG1i6YHLR0Sj_gZ4adc&r=8bgQeuykrF3aSX4ERnAE37e9TNni25ddf39sbnkKHrQ&m=hkI6yrD7SBn4Z9WO9Zt31KmSuYIswplFpvMihrHqFd4&s=PStqu-SKl1ZEMNBu4MLVtzHvrTddC9h1mM3NqDgmYmI&e='
dest = 'data/raw/'
tar = os.path.join(dest, 'beer_reviews.tar.gz')

# download file
print '>>> Downloading beer review dataset to %s, please wait...' %tar
urllib.urlretrieve (url, tar)
print '>>> Done!'

# extract file
print '>>> Extracting...'
assert tarfile.is_tarfile(tar), "File doesn't look to be a proper tar.gz, please check the source"
tar_file = tarfile.open(tar)
tar_file.extractall(path=dest)
tar_file.close()
print '>>> Done!'

# cleanup
os.remove(tar)
print '>>> Dataset available at %s' %os.path.join(dest, 'beer_reviews')
