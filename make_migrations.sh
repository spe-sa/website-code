#!/usr/bin/env bash
# bash script to run makemigrations on all apps that have migrations folder

# --- MIKE EXAMPLE ---
#for x in */migrations
#   do folder=`echo $x | sed s/\\\/migrations//`
#echo $folder
#./manage.py makemigrations $foler
#done
# --- MIKE EXAMPLE ---

# New logic: only try migrations on folders not marked as bad folders
bad_folders=(data/ config/ google_tag_manager/ spe_contact/)
for x in */
    do
        if ! [[ ${bad_folders[*]} =~ "$x" ]]
        then
#            echo $x
#            echo "${x%?}"
            ./manage.py makemigrations ${x%?}
        fi
done
