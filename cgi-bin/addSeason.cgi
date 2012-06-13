#!/usr/bin/perl
# script per l'inserimento di una nuova stagione ad una data serie TV 

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


# se non è l'admin lo redirigo alla home
if( function->checkIsAdmin() eq "false" ){
  	my $page=new CGI;
	print $page->redirect("index.cgi");
}


# altrimenti eseguo l'operazione
else{
    my $var=new CGI;
    my $id = $var->param('id');
    function::addSeason({ idSerie=>$id });
    print $var->redirect("serie.cgi?id=$id");
}