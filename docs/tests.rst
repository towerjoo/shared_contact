========================================
Test Importing Using this Scripts
========================================

1. copy *tests/sample.csv* to the same directory with the script
2. run `python gen_fields_mapping.py -i sample.csv`
3. A *fields_mapping.py* will be generated in the same directory
4. edit it to fit your needs(The file shold be like *tests/fields_mapping.sample.py*)
5. run `python shared_contacts_profiles.py -i A.csv -o OUTFILE -a ADMIN_USER` (or You can
   run `python shared_contacts_profiles.py -i A.csv -o OUTFILE -a ADMIN_USER --dry_run` to
   dry run.
6. See the output of the step 5 and check the *OUTFILE* to see the added contacts

.. Note::

    Please note changes can take up to 24 hours to be reflected in the 
    email address auto-complete and the contact manager.

    
