#!/bin/bash


DEFAULT_SOURCE_LOCATION="https://codeload.github.com/WhiteBoardDev/address-location-tool/tar.gz/master"
SOURCE_LOCATION=$1

if [ -z $SOURCE_LOCATION ]; then
  SOURCE_LOCATION=$DEFAULT_SOURCE_LOCATION
fi
printf "Using Source Location: $SOURCE_LOCATION \n"

BIN_DIR=/opt/alt
CONF_DIR=/etc/alt/conf
BACKUP_TMP_DIR=/tmp/alttmp
ALT_TMP_DIR=$TMPDIR/alttmp
REQUIRED_PYTHON_MODULES=(requests netifaces)

printf "\nStarting ALT installation \n"

####################################################################
######  Check system requirements
####################################################################
printf "Checking Required Installations...."
REQUIRED_BINS=(easy_install curl python gcc make)
for required_bin in ${REQUIRED_BINS[@]}; do
  if ! hash $required_bin 2>/dev/null; then
    printf "\n\n$required_bin is not installed! aborting!\n\n"
    exit -1
  fi
done

printf 'done \n'

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
if [[ $SOURCE_LOCATION == ht* ]]; then
  printf "downloading artifact from $SOURCE_LOCATION \n"
  curl -o $ALT_TMP_DIR/address-location-tool.tar.gz $SOURCE_LOCATION
else
  printf "copying artifact from $SOURCE_LOCATION \n"
  cp $SOURCE_LOCATION $ALT_TMP_DIR/address-location-tool.tar.gz
fi

tar -xvzf $ALT_TMP_DIR/address-location-tool.tar.gz -C $ALT_TMP_DIR

####################################################################
######  BIN folder installation
####################################################################

EXTRACTED_SUBFOLDER=$ALT_TMP_DIR
if [ -d $ALT_TMP_DIR/address-location-tool-master ]; then
  EXTRACTED_SUBFOLDER=$ALT_TMP_DIR/address-location-tool-master
  printf "Setting extracted folder $EXTRACTED_SUBFOLDER \n"
fi

test -d $BIN_DIR && printf "Installation Detected, auto removing...."
if [ -d $BIN_DIR ]; then
  rm -rf $BIN_DIR
  printf "done\n"
fi

mkdir $BIN_DIR

cp -R $EXTRACTED_SUBFOLDER/src/* $BIN_DIR/

####################################################################
######  Configuration File installation
####################################################################

printf "Creating new configuration templates...."
if [ ! -d $CONF_DIR ]; then
  mkdir -p $CONF_DIR
fi

cp $EXTRACTED_SUBFOLDER/conf/* $CONF_DIR/
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
