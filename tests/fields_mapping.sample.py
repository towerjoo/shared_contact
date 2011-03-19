# coding: utf-8
'''
mapping from Google Contact standard field name to
our customized fields name. 
Edit it to make it fit your fields.

About Mapping:
-----------------
MAPPING = {
    "Goolge_Field" : "Our Field",
    ...
}

So we need to check and edit the left side of the dict(i.e Key)
to make the right side(i.e Value) match the left as possible.
'''
MAPPING = {
    "Name": "Name", 
    "Nickname": "Nickname", 
    "Organization 1 - Title": "Organization 1 - Title", 
    "Address 1 - Type": "Address 1 - Type", 
    "Address 1 - Formatted": "Address 1 - Formatted", 
    "E-mail 1 - Type": "E-mail 1 - Type", 
    "E-mail Address": "E-mail 1 - Value", #edited
    "Phone 1 - Type": "Phone 1 - Type", 
    "Primary Phone": "Phone 1 - Value", #edited
    "Phone 2 - Type": "Phone 2 - Type", 
    "Phone 2 - Value": "Phone 2 - Value", 
    "Phone 3 - Type": "Phone 3 - Type", 
    "Phone 3 - Value": "Phone 3 - Value", 
    "Phone 4 - Type": "Phone 4 - Type", 
    "Phone 4 - Value": "Phone 4 - Value", 
    "Organization 1 - Name": "Organization 1 - Name", 
    "Company": "Company Ref/Type", #edited
    "Website 1 - Type": "Website 1 - Type", 
    "Website Home-Page": "Website 1 - Value", #edited
    "Relation 1 - Type": "Relation 1 - Type", 
    "Custom Field 1 - Type": "Custom Field 1 - Type", 
    "Custom Field 2 - Type": "Custom Field 2 - Type", 
    "Custom Field 3 - Type": "Custom Field 3 - Type", 
    "Relation 1 - Value": "Relation 1 - Value", 
    "Custom Field 1 - Value": "Custom Field 1 - Value", 
    "Custom Field 2 - Value": "Custom Field 2 - Value", 
    "Custom Field 3 - Value": "Custom Field 3 - Value", 
    "Custom Field 4 - Type": "Custom Field 4 - Type", 
    "Custom Field 4 - Value": "Custom Field 4 - Value", 
    "Notes": "Notes", 
    "Subject": "Subject", 
    "Priority": "Priority"
}
