#!/bin/bash

VERSION=0.2
SOURCE_LOCATION=https://codeload.github.com/WhiteBoardDev/address-location-tool/tar.gz/$VERSION



BIN_DIR=/opt/alt
CONF_DIR=/etc/alt/conf
BACKUP_TMP_DIR=/tmp/alttmp
ALT_TMP_DIR=$TMPDIR/alttmp
EXTRACTED_SUBFOLDER=address-location-tool-$VERSION
REQUIRED_PYTHON_MODULES=(requests netifaces)

printf "\nStarting ALT installation Version $VERSION \n"

####################################################################
######  Check system requirements
####################################################################
printf "Checking Required Installations"
REQUIRED_BINS=(easy_install curl python gcc make)
for required_bin in ${REQUIRED_BINS[@]}; do
  if ! hash $required_bin 2>/dev/null; then
    printf "\n\n$required_bin is not installed! aborting!\n\n"
    exit -1
  fi
done

####################################################################
######  Download artifact and prepare for installation
####################################################################

if [ -d $TMPDIR]; then
  ALT_TMP_DIR=$BACKUP_TMP_DIR
fi

if [ -d $ALT_TMP_DIR ]; then
  rm -rf $ALT_TMP_DIR
fi

mkdir $ALT_TMP_DIR
curl -o $TMPDIR/address-location-tool.tar.gz $SOURCE_LOCATION
tar -xvzf $TMPDIR/address-location-tool.tar.gz -C $ALT_TMP_DIR 2>/dev/null

####################################################################
######  BIN folder installation
####################################################################
test -d $BIN_DIR && printf "Installation Detected, auto removing...."
if [ -d $BIN_DIR ]; then
  rm -rf $BIN_DIR
  printf "done\n"
fi

mkdir $BIN_DIR

cp -R $ALT_TMP_DIR/$EXTRACTED_SUBFOLDER/src/* $BIN_DIR/

####################################################################
######  Configuration File installation
####################################################################

printf "Creating new configuration templates...."
if [ ! -d $CONF_DIR ]; then
  mkdir -p $CONF_DIR
fi

cp $ALT_TMP_DIR/$EXTRACTED_SUBFOLDER/conf/* $CONF_DIR/
printf "done\n"

####################################################################
######  Install pip modules
####################################################################

printf "Preparing to install pip modules....\n"

#if pip is not installed
if ! hash pip 2>/dev/null; then
  echo "PIP is not installed....installing...."
  easy_install pip
  printf "done\n"
fi

for package in ${REQUIRED_PYTHON_MODULES[@]}; do
  printf "installing pip package $package..."
  pip install $package 2>/dev/null
  printf "done\n"
done


printf "ALT $VERSION successfully installed!\n"
