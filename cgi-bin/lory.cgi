#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use Digest::MD5 qw(md5 md5_hex md5_base64);
use XML::XPath;

use function;


function->getPassword("jack");

my $user = function->getUser( "//collection/user[name/text()=\"Giacomo\"]/surname/text()" );
print $user ."\n";

#########################################################################

#my $file="../xml/films.xml";
#my $xp = XML::XPath->new(filename => $file);

my $id = "2";
my $nodeset = function->findFilm( "//collection/film[\@id=\"$id\"]");
#my $nodeset = function->findFilm();



foreach my $node ($nodeset->get_nodelist) {
	print $node->find('title')->string_value."\n";
	

}

	

	
########################################################################
# per ricordare:
	
#foreach my $book ($xp->find( '//collection/film[@id=1]' )->get_nodelist){ 
#foreach my $book ($xp->find( $query )->get_nodelist){
#				print "ID:";
#				print $book->findvalue('@id')."\n";
#				print "TITLE:"; 
#               print $book->find('title')->string_value."\n"; 
#               print "date:"; 
#               print $book->find('date')->string_value."\n"; 
#               print "\n"; 
#}
	