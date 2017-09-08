#!/bin/bash  

#------------------------------------------------------------------------------
#
# Perform full system in Ubuntu after fresh installation.
# Expects to run as Superuser.
#
#------------------------------------------------------------------------------

apt-get -y update && apt-get -y upgrade && apt-get -y dist-upgrade && apt-get -y install -f
