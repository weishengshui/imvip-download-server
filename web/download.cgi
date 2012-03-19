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


##
## core paths
##

# get base dir of this script
. ./base
. $BASE_DIR/boot

# import configuration
. $CONF_DIR/imvipdlsvr.conf



#
# include libraries.
#
. $LIB_DIR/log
. ${LIB_DIR}/bashlib
. ${LIB_DIR}/http
. ${LIB_DIR}/core
. ${LIB_DIR}/core.android



##
## Main application.
##

# obtain pamameters from URL.
client=`param cli`
client=`imvip_get_client "$client"`	# rectify parameter
#
channel=`param ch`

#version="1.0.0"




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
# handle file download request
#
handle_file_download



#
# serve the file to client.
#
if [ 1 -eq 0 ]; then
echo "Content-type: text/html"
echo ""

echo "IMVIP Download Server<br/><br/>"
echo $BASE_DIR

get_pkg_status
pkg_s=$?

echo "<br/><br/>"
echo "client=${client}<br/>"
echo "channel=${channel}<br/>"
echo "version=${version}<br/>"
echo "target_file=$target_file<br/>"
echo "target_filesize=$target_filesize<br/>"
echo "get_pkg_status=${pkg_s}<br/>"
echo "build_android_srcpkg_path=$(build_android_srcpkg_path)<br>"

get_android_pkg_genstate
r=$?
echo "get_android_pkg_genstate=$?"

fi
