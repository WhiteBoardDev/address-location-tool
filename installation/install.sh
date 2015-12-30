#!/bin/bash

VERSION=0.2
SOURCE_LOCATION=https://codeload.github.com/WhiteBoardDev/address-location-tool/tar.gz/$VERSION

BIN_DIR=/opt/alt
CONF_DIR=/etc/alt/conf
ALT_TMP_DIR=$TMPDIR/alttmp
EXTRACTED_SUBFOLDER=address-location-tool-$VERSION

####################################################################
######    Part 1
######  Download artifact and prepare for installation
####################################################################
if [ -d $ALT_TMP_DIR ]; then
  rm -rf $ALT_TMP_DIR
fi

mkdir $ALT_TMP_DIR
curl -o $TMPDIR/address-location-tool.tar.gz $SOURCE_LOCATION
tar -xvzf $TMPDIR/address-location-tool.tar.gz -C $ALT_TMP_DIR

ls $ALT_TMP_DIR


####################################################################
######    Part 2
######  BIN folder installation
####################################################################
test -d $BIN_DIR && echo "Installation Detected, auto removing"
if [ -d $BIN_DIR ]; then
  rm -rf $BIN_DIR
fi

mkdir $BIN_DIR

cp -R $ALT_TMP_DIR/$EXTRACTED_SUBFOLDER/src/* $BIN_DIR/

####################################################################
######    Part 3
######  Configuration File installation
####################################################################

echo "Creating new configuration templates"
if [ ! -d $CONF_DIR ]; then
  mkdir -p $CONF_DIR
fi

cp $ALT_TMP_DIR/$EXTRACTED_SUBFOLDER/conf/* $CONF_DIR/
