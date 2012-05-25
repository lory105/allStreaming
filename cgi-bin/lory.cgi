#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use Digest::MD5 qw(md5 md5_hex md5_base64);
use XML::XPath;

use function;


###### prove finzione getPassword per login ############################

function->getPassword("jack");

my $user = function->getUser( "//collection/user[name/text()=\"Giacomo\"]/surname/text()" );
print $user ."\n";


########################################################################
########################################################################



# X LUCA
###### prove funzione per recuperare film ############################ 

# cerco un film a partire da un id
my $id = "2";

# se voglio un film specifico secondo la query indicata:
my $nodeset = function->findFilm( "//collection/film[\@id=\"$id\"]");

# se voglio tutti i film
#my $nodeset = function->findFilm();


# come recuperare i valpori del film cercato nel db  [ x LUCA: qui recuperi i vari valori]
foreach my $node ($nodeset->get_nodelist) {
	print $node->find('title')->string_value."\n";
	print $node->find('photo')->string_value."\n";
}


########################################################################
########################################################################
	



	
########################################################################
# da ricordare:
	
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
	