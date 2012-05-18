#!/usr/bin/perl
use CGI;
use strict;
use warnings;

my $query= new CGI;
#print $query->header;

my $text="hello people in my head\n";

$text=~ tr/+/ /;

print $text;

