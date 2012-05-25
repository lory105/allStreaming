#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


function->header();
function->left("serie");
function->right();
       
print <<BODY;
		<div id="center_side">
			<h1>Serie Tv disponibili</h1>
BODY

my $nodeset=function->findSerie();
foreach my $node ($nodeset->get_nodelist) {
	my $serie=$node->find('title')->string_value;
	print "<a href=\"serie.cgi?\$serie\">$serie</a> <hr></hr>";

}
print <<BODY;
		</div>
BODY

function->footer();
