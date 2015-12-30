#!/bin/bash

SOURCE_LOCATION=https://github.com/WhiteBoardDev/address-location-tool/archive/0.1.tar.gz

BIN_DIR=/opt/address-location-tool

curl -o $TMPDIR/address-location-tool.tar.gz $SOURCE_LOCATION

test -d $BIN_DIR && echo "Installation Detected, auto removing"
if [ -d $BIN_DIR]; then
  rmdir -rf $BIN_DIR
fi

mkdir $BIN_DIR
tar -xvzf $TMPDIR/address-location-tool.tar.gz -C $BIN_DIR
