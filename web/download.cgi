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


#
# core paths
#

# get base dir of this script
BASE_DIR=`dirname $0`
# LIB_DIR: Library directory.
LIB_DIR=$BASE_DIR/lib
# DATA_DIR: Directory which stores any generated files.
DATA_DIR=$BASE_DIR/data
# CONF_DIR: Directory which contains configuration files.
CONF_DIR=$BASE_DIR/conf
# PKG_DIR: The directory which stores any generated software packages to 
# be served.
PKG_DIR=$DATA_DIR/built_pkg
# SRCPKG_DIR: The directory which contains the source packages to be 
# further processed, which will produce complete packages and stored 
# under the PKG_DIR directory.
SRCPKG_DIR=$DATA_DIR/src_pkg

# WORK_DIR: The working directory containing
RUN_DIR=$RUN_DIR/run



#
# include libraries.
#
. ${LIB_DIR}/bashlib
. ${LIB_DIR}/http
. ${LIB_DIR}/core



# import configuration
. $CONF_DIR/imvipdlsvr.conf






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
	emit_http_statuscode 404
fi

# FIXME make sure the 'app distribution channel code' has correct format.
if ! is_app_distrib_code_valid "$channel"; then
	emit_http_statuscode 404
fi


# now both client and channel codes are present.



#
# handle android download request
#
function handle_android_req() {
	echo "hi"
}



# check if the static file is present, and try to handle that
handle_file_download



case "$client" in

	android)
		handle_android_req
		;;

	# unknown client.
	*)
		handle_unknown_cli
		;;

esac



# serve the already signed .apk if it is already packaged.
# FIXME implements me


# built a signed .apk if it does not exist.




#
# serve the file to client.
#

# determine the file size
target_file="${DATA_DIR}/android-1.0.0.apk"
target_filesize=$(stat -c %s $target_file)
# some HTTP header stuffs..
if [ 1 -eq 0 ]; then

echo "Content-type: application/octet-stream"
echo "Content-length: $target_filesize"
echo ""
# ... and the file stream!
cat $target_file


exit 0

fi



echo "Content-type: text/html"
echo ""

echo "hello world from imvipdlsvr<br/>"
echo $BASE_DIR


echo "<br/><br/>"
echo "client=${client}<br/>"
echo "channel=${channel}<br/>"
echo "target_file=$target_file<br/>"
echo "target_filesize=$target_filesize<br/>"

