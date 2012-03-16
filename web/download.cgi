#!/bin/bash

# This scripts handles user requests for serving signed .apk packages
# for release for the specified client platform and application 
# distribution channel code.
#
# This script will build a signed packaged for the specified platform
# with the specified channel code if it is NOT made before. If it is
# already built, it will be served immediately.
#
# @author cyril
# since 0.1.0
#


# get base dir of this script
BASE_DIR=`dirname $0`
# LIB_DIR: Library directory.
LIB_DIR=$BASE_DIR/lib
# OUTPUT_DIR: Directory which stores any generated files.
OUT_DIR=$BASE_DIR/output



# include libraries.
. ${LIB_DIR}/bashlib
. ${LIB_DIR}/core




##
## Main application.
##

# obtain pamameters from URL.
client=`param cli`
client=`imvip_get_client "$client"`	# rectify parameter
#
channel=`param ch`


# parameters check.
# if any parameter is missing, return a 404 (NOT FOUND) response.
if [ "x$client" = "x" -o "x$channel" = "x" ]; then
	echo "Status: 404 Not Found";
	echo ""
	exit 0
fi


# now both client and channel codes are present.


# serve the already signed .apk if it is already packaged.
# FIXME implements me


# built a signed .apk if it does not exist.




# serve the file



echo "Content-type: text/html"
echo ""

echo "hello world from imvipdlsvr<br/>"
echo $BASE_DIR


echo "<br/><br/>"
echo "client=${client}<br/>"
echo "channel=${channel}<br/>"
