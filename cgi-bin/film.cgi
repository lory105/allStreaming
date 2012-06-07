#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );

function->header();


my $var=new CGI;
my $id = $var->param('id');
my $node=function->findFilm( "//collection/film[\@id=\"$id\"]")->get_node(1);
my $title=$node->find('title')->string_value;

function->left("Film", $title );
function->right();

	print "<div id=\"center_side\">"."\n";
	print "<div id=\"random_film\">"."\n";

	print "<h1>$title</h1>"."\n";
	my $img=$node->find('image')->string_value;
	print "<img src=\"../$img\" class=\"preview\"/>";
	my $description = $node->find('description')->string_value;
	print "<p>$description</p></br>";
	my $address=$node->find('address');
	foreach my $try ($address->get_nodelist) {
	  my $linkname=$try->find('linkName')->string_value;
	  my $link=$try->find('link')->string_value;
	  print "<p><b>Link:</b> <a href=\"http://$link\" target=\"_blank\">$linkname</a></p>"; 
	}
	print "</div>";
  

my $session = CGI::Session->load();

if($session->is_expired || $session->is_empty){}
else{ 
	function::printCommentsVideo({ typeVideo=>"film", idVideo=>$id  }); 
	
}

print "</div></div>";

function->footer();
