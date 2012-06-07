#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


# controllo x vedere se l'utente è loggato
my $session = CGI::Session->load();
if($session->is_expired || $session->is_empty){
    my $cgi = new CGI;
    print $cgi->header(-location => q[index.cgi]);
}


function->header();
function->left("Commenti");

function->right();

function::printAllComments();


function->footer();