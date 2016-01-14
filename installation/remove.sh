#!/bin/bash

TO_REMOVE=(/opt/alt /etc/alt/conf /etc/cron.hourly/alt-cron /var/log/alt.log)


for component_to_remove in ${TO_REMOVE[@]}; do
  printf "removing $component_to_remove..."
  rm -rf $component_to_remove
  printf "done\n"
done
