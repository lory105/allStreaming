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

my $var=new CGI;
my $id = $var->param('id');
my $nodeset=function->findSerie( "//collection/serie[\@id=\"$id\"]");
foreach my $node ($nodeset->get_nodelist) {
	print "<div id=\"center_side\">"."\n";
	print "<div id=\"random_film\">"."\n";
	my $title=$node->find('title')->string_value;
	print "<h1>$title</h1>"."\n";
	my $img=$node->find('images')->string_value;
	print "<img src=\"../$img\" class=\"preview\"/>";
	my $description = $node->find('description')->string_value;
	print "<p>$description</p></br>";
	my $seasons=$node->find('season');
	foreach my $try ($seasons->get_nodelist) {
	  my $numb=$try->find('number')->string_value;
	  print "<p><b>Stagione $numb</b></p>";
	  my $episodes=$numb->find('link');
	  foreach my $episode ($episodes->get_nodelist) {
		  my $single=$episode->find('link')->string_value;
		  print "<p>$single</p>";
	  }
	}
	print "</div>";
}    
function->loadComments();
print <<BODY;
		</div>
BODY

function->footer();
