#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use Digest::MD5 qw(md5 md5_hex md5_base64);
use XML::XPath;
use XML::XSLT;
use XML::LibXML;
use XML::XPath::XMLParser;
use XML::LibXML::NodeList;
use File::Spec;

# x Lory
use DateTime;  # --> http://stackoverflow.com/questions/2203678/how-can-i-print-a-datetime-in-the-xsdatetime-format-in-perl
use Date::Format;

use Switch;
use function;

#####################################  file db xml
# path db films
my $filmsXml = "../xml/films.xml";
# path db serie tv
my $seriesXml = "../xml/series.xml";
# path db utenti
my $usersXml = "../xml/users.xml";
# path db commenti
my $commentsXml = "../xml/comments.xml";
#########################################


########################################################################
###   max id of film


########################################################################
###   delete user

=f

my $id=3;

my $node = function->findFilm("//collection/film[\@id=\"$id\"]");

my $root

for my $channel_node ($root->findnodes('//channel')) {
   for my $child_node (reverse $channel_node->childNodes()) {
      $channel_node->removeChild($child_node);
      $channel_node->appendChild($child_node);
   }
}

=cut

###########  oppure:

=u

my $parser = XML::LibXML->new;

my $doc = $parser->parse_file( "../xml/films.xml" );
my $root = $doc->getDocumentElement();

my $id = 3;

my $book = $root->findnodes("//collection/film[\@id=3]");

print $book;

#$book->parent()->removeChild($book);

foreach my $node ( $book->get_nodelist){
 $node->parent()->removeChild($node);
}

#my $i = $book->get_nodelist;

#$i->setAttribute("io","ko");




=cut


########################################################################
###   inserimento user

=m

my $maxId = function->getMaxId("user");

$maxId = "$maxId" + 1;
my $name = "Francesco";
my $surname = "Bonin";
my $username = "francy";
my $password = "guerra";
my $email = "fra\@gmail.com";
my $avatar = "../avatar/4.png";
my $dateRegistration = "2009-07-26T21:32:52";
my $admin = "false";



my $parser = XML::LibXML->new;
my $doc = $parser->parse_file( $usersXml );
# extract the root element
my $root = $doc->getDocumentElement();


# string with the new element
my $newNode = "\t<user id=\"$maxId\">\n\t\t<name>$name</name>\n\t\t<surname>$surname</surname>\n\t\t<username>$username</username>\n\t\t<password>$password</password>\n\t\t<email>$email</email>\n\t\t\<avatar>$avatar</avatar>\n\t\t<dateRegistration>$dateRegistration</dateRegistration>\n\t\t<admin>$admin</admin>\n\t</user>\n";
print $newNode;

# check if it's well formed and create the node
my $fragment = $parser->parse_balanced_chunk($newNode);
# insert the new child
$root->appendChild($fragment);
# return it to text
my $newText = $doc->toString;
print $newText;

=cut

### oppure

=o

my $parser = XML::LibXML->new;
my $doc = $parser->parse_file( $usersXml );
my $root = $doc->getDocumentElement();

$root->appendTextChild('user', '5');

=cut

### oppure

=oo

my $parser = XML::LibXML->new();
my $doc = $parser->parse_file( $usersXml );
my $root = $doc->getDocumentElement();

my $new_element= $doc->createElement("user");
$new_element->appendText('testing');

$root->appendChild($new_element);

print $root->toString(1);


=cut



#my $maxId = function->getMaxId("film");

#$maxId = "$maxId" + 1;

#print $maxId;










########################################################################
###   max id of film

=begin

my $xp = XML::XPath->new(filename => $filmsXml);

my $path = "film";

my $query = "/collection/$path/\@id[not(. <=../preceding-sibling::$path/\@id) and not(. <=../following-sibling::$path/\@id)]";
print $query ."\n";

my $maxId = $xp->findnodes( $query );

print $maxId;

=cut



########################################################################
### dato l'array con gli id dei film in ordine dal + recente al - recente, cercare il titolo dei rispettivi film  

=begin 

my @sortId = function->sortIdFilmByDate();

my $i;
for($i = 0; $i < 5; $i++) {
	my $id = "$sortId[$i]";
	print $id;
	my $nodeset = function->findFilm("//collection/film[\@id=$id]/title/text()");
	print "ha\n";
	
	print $nodeset;

}

=cut



########################################################################
######################## prove per restituire i film più recenti (dal + recente al - recente)
=begin

# se voglio tutti i film
my $nodeset = function->findFilm();

my $id;
my $date;
my %hash;

my $buffer;

foreach my $node ($nodeset->get_nodelist) {
	$id = $node->findvalue('@id')->string_value."\n";
	$date= $node->find('date/text()')->string_value."\n";
	$date =~ s/-//g;
	$hash{$id}= $date;
}


my @sortId = reverse sort { $hash{$a} <=> $hash{$b} } keys %hash;



print $sortId[0];
print $sortId[1];
print $sortId[2];
print $sortId[3];
print $sortId[4];

=cut





########################################################################
###### prove finzione getPassword per login

#function->getPassword("jack");

#my $user = function->getUser( "//collection/user[name/text()=\"Giacomo\"]/surname/text()" );
#print $user ."\n";





########################################################################
###### prove funzione per recuperare film 

# cerco un film a partire da un id
#my $id = "2";

# se voglio un film specifico secondo la query indicata:
#my $nodeset = function->findFilm( "//collection/film[\@id=\"$id\"]");

# se voglio tutti i film
#my $nodeset = function->findFilm();


# come recuperare i valpori del film cercato nel db  [ x LUCA: qui recuperi i vari valori]
#foreach my $node ($nodeset->get_nodelist) {
#	print $node->find('title')->string_value."\n";
#	print $node->find('photo')->string_value."\n";
#}




	
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
	