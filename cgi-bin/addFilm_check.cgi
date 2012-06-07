#!/usr/bin/perl
# eseguo il check dei campi inseriti nella form per l'inserimento di un nuovo film

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );

