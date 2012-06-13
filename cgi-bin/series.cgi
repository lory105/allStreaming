#!/usr/bin/perl
# script per la visalizzazione delle serie TV

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


function->header();
function->left("Serie");
function->right();
       
print <<BODY;
		<div id="center_side">
			<h1>Serie Tv disponibili</h1>
BODY

my $nodeset=function->findSerie();
foreach my $node ($nodeset->get_nodelist) {
	my $serie=$node->find('title')->string_value;
	my $id=$node->getAttribute('id');
	my $dynamic = "<a href=\"serie.cgi?id=$id\">$serie</a> <hr></hr>";
	print $dynamic;
}
print <<BODY;
		</div>
BODY

function->footer();
