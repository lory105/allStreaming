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
function->left("Home");
function->right();

my $var=new CGI;
my $id = $var->param('id');
#my $nodeset=function->findUser( "//user[\@id=\"$id\"]");
print "<div id=\"center_side\">"."\n";

my $nodeset = function::findItem({ type=>"user", query=>"//collection/user[\@id=\"$id\"]" });

foreach my $node ($nodeset->get_nodelist) {
	my $name=$node->find('name')->string_value;
	my $surname=$node->find('surname')->string_value;
	my $avatar=$node->find('avatar')->string_value;
	my $dateRegistration=$node->find('dateRegistration')->string_value;
	my $username=$node->find('username')->string_value; 
	print "<h1>Utente: $username</h1>"."\n";
	print "<img src=\"../images/avatars/$username.jpg\" class=\"grav2\"/> "."\n";
	print "<div class=\"user\"><p><b>Nome:</b> $name</p><hr></hr>"."\n";
	print "<p><b>Cognome:</b> $surname</p><hr></hr>"."\n";
	print "<p><b>Data di registrazione:</b> $dateRegistration</p><hr></hr></div>"."\n";
}  
print "</div>"."\n";
print "</div>"."\n";

function->footer();
