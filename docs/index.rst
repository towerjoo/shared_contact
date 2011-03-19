.. Shared Contacts documentation master file, created by
   sphinx-quickstart on Tue Mar 15 07:30:37 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Shared Contacts's documentation!
===========================================

Contents:

.. toctree::
   :maxdepth: 2

   usage
   all_fields
   mapping_config
   tests
   implementation

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


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

