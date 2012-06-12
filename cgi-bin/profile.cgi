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


# se l'utente non è loggato
if( function->isLogged() eq "false"){ 
    my $page=new CGI;
    print $page->redirect("index.cgi");
}


function->header();

my $var=new CGI;
my $id = $var->param('id');

my $user = function::findItem({ type=>"user", query=>"//collection/user[\@id=$id]" })->get_node(1);
my $username = $user->find('username')->string_value;

function->left("Profilo", $username );
function->right();


#my $nodeset=function->findUser( "//user[\@id=\"$id\"]");
print "<div id=\"center_side\">"."\n";

my $nodeset = function::findItem({ type=>"user", query=>"//collection/user[\@id=\"$id\"]" });

foreach my $node ($nodeset->get_nodelist) {
	my $name=$node->find('name')->string_value;
	my $surname=$node->find('surname')->string_value;
	my $avatar=$node->find('avatar')->string_value;
	my $dateRegistration=$node->find('dateRegistration')->string_value;
	my $username=$node->find('username')->string_value; 
	
	print "<h1>Utente: $username</h1>";
	
	my $session = CGI::Session->load();
	
	print "<img src=\"../images/avatars/$username.jpg\" class=\"grav2\"/> "."\n";
	if( (function->checkIsAdmin() eq "true" && $session->param('id') != $id) || ( $session->param('id') == $id && function->checkIsAdmin() eq "false") ){
	        print<<PROFILE;
	      <br></br>
         <form method="post" action="removeItem.cgi">
             <input name="type" value="user" type="hidden">
             <input name="id" value="$id" type="hidden">
             <input type="submit" value="Rimuovi Iscrizione">
         </form>
PROFILE
	}
	print "<div class=\"user\"><p><b>Nome:</b> $name</p><hr></hr>"."\n";
	print "<p><b>Cognome:</b> $surname</p><hr></hr>"."\n";
	print "<p><b>Data di registrazione:</b> $dateRegistration</p><hr></hr></div>"."\n";
}  
print "</div>"."\n";
print "</div>"."\n";

function->footer();
