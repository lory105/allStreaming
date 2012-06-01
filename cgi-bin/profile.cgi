#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
use XML::XPath;
use XML::XPath::XMLParser;
use XML::LibXML;




function->header(); 
function->left("");
function->right();

print <<CENTER;
		<div id="center_side">
				<h1>Utente:</h1>

		</div>

CENTER

function->footer();
