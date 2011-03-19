
Quick Instructions
======================

1. copy your CSV in the script's same directory, suppose the CSV file's name is A.csv
2. run `python gen_fields_mapping.py -i A.csv`
3. A *fields_mapping.py* will be generated in the same directory
4. edit it to fit your needs(See the instructions in the top of the file)
5. run `python shared_contacts_profiles.py -i A.csv -o OUTFILE -a ADMIN_USER` (or You can
   run `python shared_contacts_profiles.py -i A.csv -o OUTFILE -a ADMIN_USER --dry_run` to
   dry run.
6. See the output of the step 5 and check the *OUTFILE* to see the added contacts



Installation
=================

The script requires the GData Python client library version 2.0.6 or higher.
Download location:
  http://code.google.com/p/gdata-python-client/downloads/list

Installation procedure:
  http://code.google.com/apis/gdata/articles/python_client_lib.html



Requirements
==================

- Python 2.4 or higher

- ElementTree Python library (builtin with Python 2.5 and higher):
  http://pypi.python.org/pypi/elementtree/

- GData Python client library version 2.0.6 or above; available at:
  http://code.google.com/p/gdata-python-client/

- the login and password of a Google Apps domain administrator account


Links
============

- GData Python client library
  http://code.google.com/p/gdata-python-client/

- Google Apps APIs discussion group
  http://groups.google.com/group/google-apps-apis


- Script Home
  https://github.com/towerjoo/shared_contact

Thanks
===============

  http://code.google.com/p/google-shared-contacts-client/
