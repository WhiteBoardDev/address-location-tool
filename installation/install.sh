#!/bin/bash

SOURCE_LOCATION=https://codeload.github.com/WhiteBoardDev/address-location-tool/tar.gz/0.1

BIN_DIR=/opt/alt
CONF_DIR=/etc/alt/conf


curl -o $TMPDIR/address-location-tool.tar.gz $SOURCE_LOCATION

test -d $BIN_DIR && echo "Installation Detected, auto removing"
if [ -d $BIN_DIR ]; then
  rm -rf $BIN_DIR
fi

mkdir $BIN_DIR
tar -xvzf $TMPDIR/address-location-tool.tar.gz -C $BIN_DIR  --strip-components=1
