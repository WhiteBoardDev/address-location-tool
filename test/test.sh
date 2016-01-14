#!/bin/bash


function error_exit
{
    echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
    exit 1
}

function testNodeDoesNotExist {
  GET_RESULT=$(curl https://luminous-heat-4042.firebaseio.com/hosts/alt-test.json | grep alt-test)

  if [[ -n $GET_RESULT ]]; then
    error_exit "Node Exists!"
  fi
}

function testNodeDoesExist {
  GET_RESULT=$(curl https://luminous-heat-4042.firebaseio.com/hosts/alt-test.json | grep alt-test)
  if [[ ! -n $GET_RESULT ]]; then
    error_exit "Node Does not Exist!"
  fi
}


curl -X DELETE https://luminous-heat-4042.firebaseio.com/hosts/alt-test.json
testNodeDoesNotExist

cd ../installation
./remove.sh
cd ..
./build-deploy.sh
./build-deploy.sh

cd ./test
cp ./conf/* /etc/alt/conf/

cd /opt/alt
python app.py alt


testNodeDoesExist

echo "test passed!"
