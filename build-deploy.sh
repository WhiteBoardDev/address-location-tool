#!/bin/bash

################################################################################
#### Does a build by creating a simple tar.gz of the installation.
################################################################################

BUILD_DIR=./build


if [ -d $BUILD_DIR ]; then
  rm -rf $BUILD_DIR
fi

mkdir $BUILD_DIR
tar cvzf $BUILD_DIR/address-location-tool.tar.gz ./src ./conf ./installation


################################################################################
#### Deploys locally using the installation script
################################################################################

./installation/install.sh $BUILD_DIR/address-location-tool.tar.gz localbuild
