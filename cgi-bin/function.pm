#!/usr/bin/perl

package function;

use CGI;
use strict;
use warnings;




sub header {
print "Content-type: text/html\n\n";
print <<HEADER;
	<?xml version="1.0" encoding="iso-8859-1"?>
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
			<title>AllStreaming</title>
			<link rel="shortcut icon" href="images/logo.ico" type="image/x-icon" />
			<link rel="icon" href="images/logo.ico" type="image/x-icon" />
			<link rel="stylesheet" href="../styles/style.css" type="text/css" />
		</head> 
	
HEADER

}

sub footer {

print <<FOOTER;
	<div class="pushfooter"></div>
	</div>
	</br>
		<div id="footer">
			<a href="#">allStreaming.com </a>-
			<a href="#">About Us </a>-
			<a href="#"> Contact Us</a>
		</div>
    </body>
</html>

FOOTER
	
}

1;
