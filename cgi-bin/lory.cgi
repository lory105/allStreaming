#!/usr/bin/perl

    use CGI;
    use strict;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session ( '-ip_match' );
  use CGI::Session;

    use warnings;
    use function;
    use Digest::MD5 qw(md5 md5_hex md5_base64);
    use XML::XPath;
    use XML::XSLT;
    use XML::LibXML;

  use function;
  use XML::XPath;
  use Digest::MD5 qw(md5 md5_hex md5_base64);

#use XML::XPath::XMLParser;
#use XML::LibXML::NodeList;
#use XML::LibXML::Node
use File::Spec;
#use XML::LibXML::PrettyPrint;
use XML::Twig;
use XML::LibXML::XPathContext;

# x Lory
use DateTime;  # --> http://stackoverflow.com/questions/2203678/how-can-i-print-a-datetime-in-the-xsdatetime-format-in-perl
use Date::Format;

use Switch;
use function;

use Encode;
use Unicode::String qw(utf8 latin1);

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
###   

my $idSerie = "2";
my $idSeason="3";
my $nameLink = "puu";
my $link = "poo";
my $empty;


my $string = "ioèo";

print $string;

print encode("utf8", $string);


=o
my $id= "4";
my $node=function->findFilm( "//collection/film[\@id=\"$id\"]")->get_node(1);
my $string=$node->find('description')->string_value;


print $string;
   
#print decode("iso-8859-1", $string); 


   # my $description= encode("utf8", $descriptionn);

#print function->getMaxId("season", $id );

#function::addEpisode({ idSerie=>$idSerie, idSeason=>$idSeason, title=>"haha", link=>"www" });

#function::addSeason({ idSerie=>$id });

#function::removeUser({ id=>"2" });


=o
my $idFilm = "1";
my $path = "film";
my $xp = XML::XPath->new(filename => $filmsXml);

my $query = "/collection/film[\@id=\"$idFilm\"]/address/\@idLink[not(. <=../preceding-sibling::address/\@idLink) and not(. <=../following-sibling::address/\@idLink)]";
#my $query1 = "/collection/$path/\@id[not(. <=../preceding-sibling::$path/\@id) and not(. <=../following-sibling::$path/\@id)]";

my $maxId = $xp->findnodes( $query );

print $maxId;





=O

my $idFilm= "5";
my $idLink= "1";

function::removeLink({ idFilm=>$idFilm, idLink=>$idLink });

=cut

=o  
$query = "//collection:film[\@id=\"$id\"]";

    $doc = $parser->parse_file( $file );

    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");

    my $node = $xpc->findnodes( $query, $doc )->get_node(1);
  
  print $node;
  print $node->find('title')->string_value;
  

    # extract the root element
    my $root = $doc->getDocumentElement();
 
    $root->removeChild( $node );
    # debug da togliere!!!
    print $root->toString();
    
    # write to file
    #open(OUT,'>:utf8',$file ) || die("Cannot open file");
    #print OUT $root->toString();
    #close(OUT);
=cut





#my @arr = function::sortIdItemByDate({ type=>"comment"});

#my $size= @arr;
#print $size;

#print function::sortIdItemByDate({ type=>"film"});

#print function::findItem({ type=>"comment", query=>"//collection/comment[typeVideo=\"serie\" and idVideo=\"2\"]" })->size();

#print function::findItem({ type=>"serie", query=>"//collection/serie[\@id=$id]" })->size();

#print function->countRegisteredUsers();

#print function->sortIdFilmByDate();


########################################################################
###   inserimento serie ok

=o

my $title = "Heroes";
my $image = "heroes.png";
my $description = "na bomba!!";

function::addSerie({ title=>$title, image=>$image, description=>$description });

=cut


########################################################################
###   delete film, serie, user ok

=o
    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $usersXml );
    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");
    my $id = 2;
    my $node = $xpc->findnodes("//collection:user[\@id=\"$id\"]", $doc )->get_node(1);
  
    # extract the root element
    my $root = $doc->getDocumentElement();
 
    $root->removeChild( $node );
    print $root->toString();

=cut


#function::removeItem({ type=>"film", id=>"3"});




########################################################################
###   inserimento link film ok

=O

#function->addFilmLink();

    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $filmsXml );
    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");
    my $id = 3;
    my $node = $xpc->findnodes("//collection:film[\@id=\"$id\"]", $doc )->get_node(1);
    my $oldNode = $node;


    my $name = "megaup";
    my $link = "www.mega.com";

    

    # extract the root element
    my $root = $doc->getDocumentElement();

    # string with the new element
    my $newAddressNode = "\t\t<address>\n\t\t\t<name>$name</name>\n\t\t\t<link>$link</link>\n\t\t</address>\n";
    print $newAddressNode;
    


    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newAddressNode);
    # insert the new child
    $node->appendChild($fragment);
    print $node->toString();
    
    $root->removeChild( $oldNode );
    $root->appendChild($node);
    print $root->toString();

=cut


=o

my $idFilm = "3";
my $nameLink = "maga";
my $link = "djs";

function::addFilmLinkf({ idFilm=>$idFilm, linkName=>$nameLink, link=>$link });

=cut  



########################################################################
###   inserimento film ok

=p

my $maxId = function->getMaxId("film");

$maxId = "$maxId" + 1;
my $title = "Io Sono Leggenda";
my $image = "../images/5.png";
my $description = "belllo cazzo!";
my $date = "2009-07-26";
my $family = "horror";


function::addFilm({ title=>$title, image=>$image, description=>$description, date=>$date, family=>$family });


=cut



########################################################################
###   inserimento user ok

=k

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


function::addUser({ name=>$name, surname=>$surname, username=>$username, password=>$password, email=>$email, avatar=>$avatar, dateRegistration=>$dateRegistration, admin=>$admin });


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
	