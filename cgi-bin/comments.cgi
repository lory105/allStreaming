#!/usr/bin/perl
# script per la visualizzazione dei commenti

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


# se l'utente non è loggato lo redirigo alla home
if( function->isLogged() eq "false"){
  	my $page=new CGI;
	print $page->redirect("index.cgi");
}

# altrimenti stampo i commenti
else{
    function->header();
    function->left("Commenti");

    function->right();

    function::printAllComments();

    function->footer();
}