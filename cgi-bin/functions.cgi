#!/usr/bin/perl

use CGI;
use strict;
use warnings;

sub printerHead() {

print <<HEADER;
Content-type: text/html\n\n
<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>AllStreaming</title>
        <link rel="shortcut icon" href="images/logo.ico" type="image/x-icon" />
        <link rel="icon" href="images/logo.ico" type="image/x-icon" />
        <link rel="stylesheet" href="styles/style.css" type="text/css" />
        <meta http-equiv="refresh" content= "0; url= cgi-bin/index.cgi" />
    </head> 
HEADER
}
