#!/bin/sh


# BIN_DIR: Directory contains executables.
BIN_DIR=$BASE_DIR/bin

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

# RUN_DIR: The working directory containing
RUN_DIR=$RUN_DIR/run

# TMP_DIR: temporary directory
TMP_DIR=/tmp

# LOCAL_VERSION_INFO_DIR: contains the information for the latest 
# version of different client packages.
# each file should have a format: <client_name>
LOCAL_VERSION_INFO_DIR=$DATA_DIR/latest_ver

# LOG_DIR: Contains logs from program.
LOG_DIR=$BASE_DIR/log

LOG_FILE=$LOG_DIR/imvipdlsvr.log
