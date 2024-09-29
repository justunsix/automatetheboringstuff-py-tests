#!/bin/bash
set -e

# Localisation configuration for Toronto, Canada
ln -sf /usr/share/zoneinfo/America/Toronto /etc/localtime
mv /etc/locale.gen /etc/locale.gen.old
echo -e "en_CA.UTF-8 UTF-8\nen_US.UTF-8 UTF-8" > /etc/locale.gen
echo "LANG=en_CA.UTF-8" > /etc/locale.conf
locale-gen

# Track VM creation time
date > /etc/vagrant_provisioned_at

# Update system
pacman --noconfirm -Syyu
# Install
# - git pip python make - for repository and language
# - vim - optional for editing
# - base-devel - required for building some python packages
# - pandoc - need by Langchain for document conversion during model load
pacman --noconfirm -S git python python-pip make vim base-devel pandoc

echo -e "-- OS Localization and OS Update Complete"