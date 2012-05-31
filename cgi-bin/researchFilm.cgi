#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


function->header();
function->left("film");
function->right();
       
my $var=new CGI;
my $type = $var->param('type');
       
print <<BODY;
		<div id="center_side">
BODY

if ($type eq "Year") {
	my $year = $var->param('value');
	print "<h1>Film disponibili anno $year</h1>";
	if($year == 'pre-2000') {
		$year="2000-1-1";
		my $nodeset=function->findFilm( "//collection/film[date < $year]");
		if(($nodeset->size()) == 0 ){
			print "<p>Nessun film disponibile.</p>";
		}
		foreach my $node ($nodeset->get_nodelist) {
			my $film=$node->find('title')->string_value;
			my $id=$node->getAttribute('id');
			my $dynamic = "<a href=\"film.cgi?id=$id\">$film</a> <hr></hr>";
			print $dynamic;
		}
	}
	else{
		my $nodeset=function->findFilm( "//collection/film[date = $year]");
		if(($nodeset->size()) == 0 ){
			print "<p>Nessun film disponibile.</p>";
		}
		foreach my $node ($nodeset->get_nodelist) {
		my $film=$node->find('title')->string_value;
		my $id=$node->getAttribute('id');
		my $dynamic = "<a href=\"film.cgi?id=$id\">$film</a> <hr></hr>";
		print $dynamic;
		}
	}
}
else{
		my $family = $var->param('value');
		print "<h1>Film genere $family</h1>";
		my $set=function->findFilm( "//collection/film[family = \"$family\"]");
		foreach my $node ($set->get_nodelist) {
			my $film=$node->find('title')->string_value;
			my $id=$node->getAttribute('id');
			my $dynamic = "<a href=\"film.cgi?id=$id\">$film</a> <hr></hr>";
			print $dynamic;
		}
}

print <<BODY;
</div>
BODY

function->footer();
