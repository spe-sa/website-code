#!/usr/bin/env bash
# start shell script

# source environment

source ../../env/bin/activate
../manage.py loaddata data/JD_Data_Dump/auth_users.json
../manage.py loaddata data/JD_Data_Dump/mainsite.json
../manage.py loaddata data/JD_Data_Dump/spe_links.json
../manage.py loaddata data/JD_Data_Dump/spe_events.json
../manage.py loaddata data/JD_Data_Dump/spe_polls.json
../manage.py loaddata data/JD_Data_Dump/spe_blog.json
../manage.py loaddata data/JD_Data_Dump/cms_export.json
