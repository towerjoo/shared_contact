=======================
About Implementation
=======================

Problem
====================

Since different contacts providers provides different contacts format. So 
it becomes hard to import one into another one. 

Especially, for the Google Contacts which are used by millions of companies 
and people.

This script is to make the importing to Google's Contact Service easily
from other contacts providers, e.g MS's Outlook, ect.

Solution
=================

Based on `google-shared-contacts-client`_ , I follow the solution below:

1. Define the Fields Mapping from Google's Standard fields name to Our customized fileds name
2. Use the mapping fields to get the data 
3. Use the `google-shared-contacts-client`_ script to handle the importing logic

Implementation
======================

gen_mapping_fields.py
-------------------------

To generate the mapping config automatically based on the contacts to import.

See the comments in the source code.

shared_contacts_profiles.py
-------------------------

Most codes are borrowd from `google-shared-contacts-client`_. And I made
some change in Line 877.

See the comments in the source code.

.. _google-shared-contacts-client: http://code.google.com/p/google-shared-contacts-client/
