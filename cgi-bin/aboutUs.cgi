#!/usr/bin/perl
# script riguardante le informazioni di allStreaming

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


function->header();
function->left("About Us");
function->right();


print<<CENTER;
<div id="aboutUs">


</div>
CENTER



function->footer();