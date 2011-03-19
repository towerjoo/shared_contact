.. _usage:

===================================
How to Use this script
===================================


You can follow the instructions below:

1. copy your CSV in the script's same directory, suppose the CSV file's name is A.csv
2. run `python gen_fields_mapping.py -i A.csv`
3. A *fields_mapping.py* will be generated in the same directory
4. edit it to fit your needs(See the instructions in the top of the file)
5. run `python shared_contacts_profiles.py -i A.csv -o OUTFILE -a ADMIN_USER` (or You can
   run `python shared_contacts_profiles.py -i A.csv -o OUTFILE -a ADMIN_USER --dry_run` to
   dry run.
6. See the output of the step 5 and check the *OUTFILE* to see the added contacts

.. Note::

    Please note changes can take up to 24 hours to be reflected in the 
    email address auto-complete and the contact manager.

    
Get more Information about *shared_contacts_profiles.py* from `google-shared-contacts-client`_.

.. _google-shared-contacts-client: http://code.google.com/p/google-shared-contacts-client/
