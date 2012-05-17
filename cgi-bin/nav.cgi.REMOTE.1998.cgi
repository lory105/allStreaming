#!/usr/bin/perl
use CGI;
use strict;
use warnings;

my $query= new CGI;
print $query->header;
print "hello people in my head\n";
