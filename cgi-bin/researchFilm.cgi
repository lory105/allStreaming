#!/usr/bin/perl
# script per la ricerca dei film

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
use Switch;

function->header();
function->left("Film");
function->right();
       
my $var=new CGI;
my $type = $var->param('type');
       
print <<BODY;
		<div id="center_side">
BODY

if ($type eq "Year"){
    my $year = $var->param('value');
	
    switch ($year){
	    case "pre-2001"{
	        print "<h1>Film disponibili anno $year</h1>";
	        $year="2001";
		    my $nodeset=function->findFilm( "//collection/film[substring(date, 1, 4) < $year]");
		    if(($nodeset->size()) == 0 ){
	            print "<p>Nessun film disponibile.</p>";
		    }
		    foreach my $node ($nodeset->get_nodelist) {
                my $film=$node->find('title')->string_value;
			    $film=function->convert($film);
			    my $id=$node->getAttribute('id');
			    my $dynamic = "<a href=\"film.cgi?id=$id\" tabindex=\"5\">$film</a> <hr />";
			    print $dynamic;
		   }
		   last;
	    }
	    
        case "all"{
            print "<h1>Tutti i fillm</h1>";
		    my $nodeset=function->findFilm( "//collection/film");
		    if(($nodeset->size()) == 0 ){
	           print "<p>Nessun film disponibile.</p>";
		    }
		    foreach my $node ($nodeset->get_nodelist) {
                my $film=$node->find('title')->string_value;
			    $film=function->convert($film);
			    my $id=$node->getAttribute('id');
			    my $dynamic = "<a href=\"film.cgi?id=$id\" tabindex=\"5\">$film</a> <hr />";
			    print $dynamic;
		   }
	       last;
	   }
	
	   default {
	       print "<h1>Film disponibili anno $year</h1>";
	       my $nodeset=function->findFilm( "//collection/film[date = $year]");
		   if(($nodeset->size()) == 0 ){
		      print "<p>Nessun film disponibile.</p>";
		   }
		   foreach my $node ($nodeset->get_nodelist) {
		      my $film=$node->find('title')->string_value;
		      $film=function->convert($film);
		      my $id=$node->getAttribute('id');
		      my $dynamic = "<a href=\"film.cgi?id=$id\" tabindex=\"5\">$film</a> <hr />";
		      print $dynamic;
	       }
	       last;
	   }
    }
}
else{
    my $family = $var->param('value');
	print "<h1>Film genere $family</h1>";
	my $set=function->findFilm( "//collection/film[family = \"$family\"]");
	foreach my $node ($set->get_nodelist) {
		my $film=$node->find('title')->string_value;
		$film= function->convert($film);
		my $id=$node->getAttribute('id');
		my $dynamic = "<a href=\"film.cgi?id=$id\" tabindex=\"5\">$film</a> <hr />";
		print $dynamic;
	}
}

print <<BODY;
</div>
BODY

function->footer();
