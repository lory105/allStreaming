#!/usr/bin/perl

package function;

use CGI;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
#use CGI qw(:standard);
use strict;
use warnings;
use XML::XPath;
#use XML::XPath::XMLParser;
#use XML::LibXML;
use Digest::MD5 qw(md5 md5_hex md5_base64);
use XML::XSLT;
use Switch;

# x Lory
use DateTime;  # --> http://stackoverflow.com/questions/2203678/how-can-i-print-a-datetime-in-the-xsdatetime-format-in-perl
use Date::Format;




# path db films
my $filmsXml = "../xml/films.xml";
# path db serie tv
my $seriesXml = "../xml/series.xml";
# path db utenti
my $usersXml = "../xml/users.xml";
# path db commenti
my $commentsXml = "../xml/comments.xml";





sub header {
print "Content-type: text/html\n\n";
print <<HEADER;
	<?xml version="1.0" encoding="iso-8859-1"?>
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
			<title>AllStreaming</title>
			<link rel="shortcut icon" href="images/logo.ico" type="image/x-icon" />
			<link rel="icon" href="images/logo.ico" type="image/x-icon" />
			<link rel="stylesheet" href="../styles/style.css" type="text/css" />
			<script type="text/javascript" src="../javascript/validation.js"></script>
		</head> 
	
HEADER

}

sub menuNotLogged {
if($_[0] eq "home"){
print<<MENU
			<div id="navigation">Ti trovi in : Home</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="#"><b>Home</b></a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/signin.png"/><a href="registration.cgi">Registrazione</a><hr>
					</br>
				</div>
		</div>	
MENU
}
if($_[0] eq "serie"){
print<<MENU
			<div id="navigation">Ti trovi in : Serie TV</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi"><b>Serie Tv</b></a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/signin.png"/><a href="registration.cgi">Registrazione</a><hr>
					</br>
				</div>
		</div>	
MENU
	}
if($_[0] eq "film"){
print<<MENU
			<div id="navigation">Ti trovi in : Film</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi"><b>Film</b></a><hr>
					<img src="../images/signin.png"/><a href="registration.cgi">Registrazione</a><hr>
					</br>
				</div>
		</div>	
MENU
	}
if($_[0] eq "registration"){
print<<MENU
			<div id="navigation">Ti trovi in : Registratione</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/signin.png"/><a href="#"><b>Registrazione</b></a><hr>
					</br>
				</div>
		</div>	
MENU
	}

if($_[0] eq ""){
print<<MENU
			<div id="navigation">Ti trovi in : Commenti</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr>
					</br>
				</div>
		</div>	
MENU
	}

}

sub menu {
if($_[0] eq "home"){
print<<MENU
			<div id="navigation">Ti trovi in : Home</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="#"><b>Home</b></a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr>
					</br>
				</div>
		</div>	
MENU
}
if($_[0] eq "serie"){
print<<MENU
			<div id="navigation">Ti trovi in : Serie TV</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi"><b>Serie Tv</b></a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr>
					</br>
				</div>
		</div>	
MENU
	}
if($_[0] eq "film"){
print<<MENU
			<div id="navigation">Ti trovi in : Film</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi"><b>Film</b></a><hr>
					<img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr>
					</br>
				</div>
		</div>	
MENU
	}
if($_[0] eq "comment"){
print<<MENU
			<div id="navigation">Ti trovi in : Commenti</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/comment.png"/><a href="comments.cgi"><b>Commenti</b></a><hr>
					</br>
				</div>
		</div>	
MENU
	}

if($_[0] eq ""){
print<<MENU
			<div id="navigation">Ti trovi in : Commenti</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr>
					</br>
				</div>
		</div>	
MENU
	}

}

sub left {

  my $session = CGI::Session->load();
  my $user = $session->param('username');
  if($session->is_expired || $session->is_empty)
  {
	  print <<LEFT;
		<body>
			<div id="wrapper">
				<div id="header">
					<div id="login">
						<form method="post" action="login.cgi">
							<input type="text" name="username" value="User" size="12"/>
							<input type="password" name="password" value="Password" size="12"/>
							<button type="submit" id="sending">Login</button>
						</form>
					</div>
				</div>	
LEFT
menuNotLogged($_[1]);
  }
  else
  {
	print <<LEFT;
		<body>
			<div id="wrapper">
				<div id="header">
					<div id="login">
						<div class="userLogged">
LEFT
						print "<div class=\"avatar\"> <img src=\"../images/avatars/1.jpg\" class=\"grav\"/> </div>";
						print "<div class=\"name\">Benvenuto, <B>$user</B> <br><a href=\"logout.cgi\">Logout</a></div>";
	print <<LEFT;			
					</div>
				</div>
			</div>	
LEFT
menu($_[1]);
  }
}


sub right {
# year-from-dateTime(datetime)

print <<RIGHT;
			<div id="right_side">
			<div class="view">Ultimi video commentati</div>
				<div class="content_max_view">
RIGHT

my @sortIdComment = function::sortIdItemByDate({ type=>"comment"});
my $video;
my $x;

FOO: {
    # se non ci sono commenti nel DB
    my $arraySize = @sortIdComment;
    if( $arraySize==0 ){ print "Non ci sono commenti"; last FOO;}
    
    for($x = 0; scalar @sortIdComment >$x && $x < 5; $x++) {
            
	    my $idComment = "$sortIdComment[$x]";
	    my $node = function::findItem({ type=>"comment", query=>"//collection/comment[\@id=$idComment]" })->get_node(1);
    
	    my $typeVideo; my $idVideo;
	
        # dal singolo commento cerco a quale video si riferisce
    	$typeVideo = $node->find('typeVideo')->string_value;
	    $idVideo= $node->find('idVideo')->string_value;
    
        # cerco il video con l'id corrispondente 
        if( $typeVideo eq "film"){
            $video = function::findItem({ type=>$typeVideo, query=>"//collection/film[\@id=$idVideo]" })->get_node(1);
        }
        if( $typeVideo eq "serie"){
            $video = function::findItem({ type=>$typeVideo, query=>"//collection/serie[\@id=$idVideo]" })->get_node(1);
        }
    
        my $title = $video->find('title')->string_value;
	    print "<a href=\"$typeVideo.cgi?id=$idVideo\" >$title</a></br>";
    }
}

print <<RIGHT;
				</div>
			<div class="news">Novit&agrave;</div>
				<div class="content_max_view">
RIGHT

my @sortId = function::sortIdItemByDate({ type=>"film" });

# creo dinamicamente i link ai 5 film più recenti 
my $i;
for($i = 0; $i < 5; $i++) {
	my $id = "$sortId[$i]";
	my $nodeset = function::findItem({ type=>"film", query=>"//collection/film[\@id=$id]/title/text()" });
	print "<a href=\"film.cgi?id=$id\" >$nodeset</a></br>";

}

my $registeredUser = function->countRegisteredUsers();
print <<RIGHT;
				</div>
			<div class="news">Utenti iscritti</div>
			<div class="content_max_view">$registeredUser utenti</div>
		</div>		
RIGHT
}


sub footer {

print <<FOOTER;
	<div class="pushfooter"></div>
	</div>
	</br>
		<div id="footer">
			<a href="#">allStreaming.com </a>-
			<a href="aboutUs.cgi">About Us </a>-
			<a href="#"> Contact Us</a>
		</div>
    </body>
</html>

FOOTER
	
}


# ritorna gli id dell'item (film o comment) ordinati per data ( dal + recente al meno recente )
# es: function::sortIdFilmByDate({ type=>"film"});
sub sortIdItemByDate{
    my $parameters = shift;
    my $type = $parameters->{type};

    my $nodeset = function::findItem({ type=>$type, query=>"//collection/$type"});

    my $id;
    my $date;
    my %hash;

    my $buffer;

    foreach my $node ($nodeset->get_nodelist) {
    	$id = $node->findvalue('@id')->string_value."\n";
	    $date= $node->find('date/text()')->string_value."\n";
    	$date =~ s/-//g;  # toglie i trattini nelle date
    	$date =~ s/T//g;
    	$date =~ s/://g;
    	$hash{$id}= $date;
    }

    return reverse sort { $hash{$a} <=> $hash{$b} } keys %hash;
}




# aggiunge un nuovo utente
# come invocare funzione: attenzione sintassi!!!
# function::addUser({ name=>$name, surname=>$surname, username=>$username, password=>$password, email=>$email, avatar=>$avatar, dateRegistration=>$dateRegistration, admin=>$admin });
sub addUser{
    my $parameters = shift;
   
    my $maxId = function->getMaxId("user");
    $maxId = "$maxId" + 1;
    
    my $name = $parameters->{name};
    my $surname = $parameters->{surname};
    my $username = $parameters->{username};
    my $password = $parameters->{password};
    my $email = $parameters->{email};
    # $email =~ s/@/\@/g;                     # inserisce il simbolo "\" prima della "@"  forse non serve!!
    my $avatar = $parameters->{avatar};
    my $dateRegistration = $parameters->{dateRegistration};
    my $admin = $parameters->{admin};

    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $usersXml );
    # extract the root element
    my $root = $doc->getDocumentElement();

    # string with the new element
    my $newNode = "\t<user id=\"$maxId\">\n\t\t<name>$name</name>\n\t\t<surname>$surname</surname>\n\t\t<username>$username</username>\n\t\t<password>$password</password>\n\t\t<email>$email</email>\n\t\t\<avatar>$avatar</avatar>\n\t\t<dateRegistration>$dateRegistration</dateRegistration>\n\t\t<admin>$admin</admin>\n\t</user>\n";
    #print $newNode;

    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newNode);
    # insert the new child
    $root->appendChild($fragment);

    # write to file
    open(OUT,'>:utf8',$usersXml ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}


# aggiunge un nuovo film
# come invocare funzione: attenzione sintassi!!!
# function::addFilm({ title=>$title, image=>$image, description=>$description, date=>$date, family=>$family });
sub addFilm{
    my $parameters = shift;
    my $maxId = function->getMaxId("film");
    $maxId = "$maxId" + 1;
    
    my $title = $parameters->{title};
    my $image = $parameters->{image};
    my $description = $parameters->{description};
    my $date = $parameters->{date};
    my $family = $parameters->{family};
    
    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $filmsXml );
    # extract the root element
    my $root = $doc->getDocumentElement();

    # string with the new element
    my $newNode = "\t<film id=\"$maxId\">\n\t\t<title>$title</title>\n\t\t<image>$image</image>\n\t\t<description>$description</description>\n\t\t<date>$date</date>\n\t\t<family>$family</family>\n\t</film>\n";
    #print $newNode;

    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newNode);
    # insert the new child
    $root->appendChild($fragment);
    print $root->toString();
    
    # write to file
    open(OUT,'>:utf8',$filmsXml ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}



# aggiunge una nuova serie
# come invocare funzione: attenzione sintassi!!!
# function::addSerie({ title=>$title, image=>$image, description=>$description });
sub addSerie{
    my $parameters = shift;
    my $maxId = function->getMaxId("serie");
    $maxId = "$maxId" + 1;
    
    my $title = $parameters->{title};
    my $image = $parameters->{image};
    my $description = $parameters->{description};
    
    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $seriesXml );
    # extract the root element
    my $root = $doc->getDocumentElement();

    # string with the new element
    my $newNode = "\t<serie id=\"$maxId\">\n\t\t<title>$title</title>\n\t\t<image>$image</image>\n\t\t<description>$description</description>\n\t</serie>\n";

    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newNode);
    # insert the new child
    $root->appendChild($fragment);
    
    # write to file
    open(OUT,'>:utf8',$seriesXml ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}



# aggiunge un link ad un film
# da richiamare così, Attenzione sintassi!!!
# function::addFilmLinkf({ idFilm=>$idFilm, linkName=>$nameLink, link=>$link });
sub addFilmLinkf{    
    my $parameters = shift;
    my $idFilm = $parameters->{idFilm};
    my $linkName = $parameters->{linkName};
    my $link = $parameters->{link};

    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $filmsXml );
    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");
    # recupero il nodo del film da modificare
    my $newNode = $xpc->findnodes("//collection:film[\@id=\"$idFilm\"]", $doc )->get_node(1);
    my $oldNode = $newNode;

    # extract the root element
    my $root = $doc->getDocumentElement();

    # string with the new element
    my $newAddressNode = "\t\t<address>\n\t\t\t<linkName>$linkName</linkName>\n\t\t\t<link>$link</link>\n\t\t</address>\n";

    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newAddressNode);
    # insert the new child
    $newNode->appendChild($fragment);
    
    $root->removeChild( $oldNode );
    $root->appendChild($newNode);
    # debug da togliere!!!
    print $root->toString();
    
    # write to file
    open(OUT,'>:utf8',$filmsXml ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
    
}

# rimuove un fils, una serie o un utente
# riceve in input l'id dell'item da eliminare e il riferimento se è un film, una seire o un utente
# function::removeItem({ type=>"film", id=>"3"});
sub removeItem {

    my $parameters = shift;
    my $id = $parameters->{id};
    my $type = $parameters->{type};  # film, serie, o user

    my $parser = XML::LibXML->new;
    my $doc; my $query; my $file;
    
    switch ($type) {
	   case "film"  { $file = $filmsXml;  
	                  $query = "//collection:film[\@id=\"$id\"]"; last;
	   }
	   case "serie" { $file = $seriesXml; 
	                  $query = "//collection:serie[\@id=\"$id\"]"; last;
	   }
	   case "user"  { $file = $usersXml;
	                  $query = "//collection:user[\@id=\"$id\"]"; last;
	   }
	   #case "comment" { my $doc = $parser->parse_file( $usersXml ); }
    }
    
    $doc = $parser->parse_file( $file );

    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");

    my $node = $xpc->findnodes( $query, $doc )->get_node(1);
  
    # extract the root element
    my $root = $doc->getDocumentElement();
 
    $root->removeChild( $node );
    # debug da togliere!!!
    print $root->toString();
    
    # write to file
    open(OUT,'>:utf8',$file ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}


# funzione di ricerca film: se non riceve parametri (!$_[1]) ricerca tutti i film,
# altrimenti esegue la query ricevuta in $_[1]
# come invocare la funzione (attenzione sintassi query!!) : 
# function->findFilm( "//collection/film[\@id=\"$id\"]");
sub findFilm {

# creo un oggetto XPath e gli associo il file xml dove cercare
my $xp = XML::XPath->new(filename => $filmsXml);

my $query;

# se ricevo la query
if( $_[1]){ $query = $_[1]; }

# altrimenti cerco tutti i fiml
else{ $query = "//collection/film"; }

# debug da togliere!!!
# print "$query" . "\n";

#$xp->find()->get_nodelist;
#return $xp->find( $query )->get_nodelist;
#my $io = $xp->findnodes( $query );
#print $io;
return $xp->findnodes( $query );

}


# funzione di ricerca serie tv: se non riceve parametri (!$_[1]) ricerca tutte le serie,
# altrimenti esegue la query ricevuta in $_[1]
# come invocare la funzione (attenzione sintassi query!!) :
# function->findSerie( "//collection/serie[\@id=\"$id\"]");
sub findSerie {

# creo un oggetto XPath e gli associo il file xml dove cercare
my $xp = XML::XPath->new(filename => $seriesXml);

my $query;

# se ricevo la query
if( $_[1]){ $query = $_[1]; }

# altrimenti cerco tutti i fiml
else{ $query = "//collection/serie"; }

# debug da togliere!!!
#print "$query" . "\n";

return $xp->findnodes( $query );
}




# funzione di ricerca film, serie, user, comment. riceve in input la query e il tipo di item da cercare
# funzione richiamabile così:  
# function::findItem({ type=>"serie", query=>"//collection/serie[\@id=$id]" });
# function::findItem({ type=>"comment", query=>"//collection/comment[typeVideo=\"serie\" and idVideo=\"2\" ]" });
sub findItem {
    my $parameters = shift;
    my $type = $parameters->{type};
    my $query = $parameters->{query};
    my $file;
    
    switch ($type) {
	   case "film"    { $file = $filmsXml; last; }
	   case "serie"   { $file = $seriesXml; last; }
	   case "user"    { $file = $usersXml; last; }
	   case "comment" { $file = $commentsXml; last; }
    }
    
    # creo un oggetto XPath e gli associo il file xml dove cercare
    my $xp = XML::XPath->new(filename => $file);

    # debug da togliere!!!
    #print "$query" . "\n";

    return $xp->findnodes( $query );
}


# funzione di ricerca user: se non riceve parametri (!$_[1]) ricerca tutti gli user,
# altrimenti esegue la query ricevuta in $_[1] 
sub findUser {

# creo un oggetto XPath e gli associo il file xml dove cercare
my $xp = XML::XPath->new(filename => $usersXml);

my $query;
if( $_[1] ){ $query= $_[1]; }
else{ $query= "//collection/user"; }

return $xp->findnodes( $query );
}


# riceve in input lo username dell'utente che sta facendo il login, controlla nel db la presenza di tale username
# restituendone la password corrispondente che è criptata
sub getPassword() {

# $_[1] contiene lo username

# creo un oggetto XPath e gli associo il file xml dove cercare
my $xp = XML::XPath->new(filename => $usersXml);

my $username = $_[1];
my $query= "//collection/user[username/text()=\"$username\"]/password/text()";

my $crypted_password = $xp->find( $query );

return $crypted_password;
}



sub redirectTo {
	print $_[1]->header(-location=>"$_[2]");
}



# stampa gli ultimi X commenti inseriti
sub printAllComments{

     print <<COMMENTS;
	      <h2>Ultimi 20 commenti</h2>
		  <div id="commenti">
		  </br>
COMMENTS


    my @sortIdComment = function::sortIdItemByDate({ type=>"comment"});

    FOO: {
        # se non ci sono commenti nel DB
        my $arraySize = @sortIdComment;
        if( $arraySize==0 ){ print "Non ci sono commenti"; last FOO;}
        else{
            my $x;
            for($x = 0; scalar @sortIdComment >$x && $x < 20; $x++) {
            
	            my $idComment = "$sortIdComment[$x]";
	            my $node = function::findItem({ type=>"comment", query=>"//collection/comment[\@id=$idComment]" })->get_node(1);
	           
	            my $typeVideo = $node->find('typeVideo')->string_value;
	            my $idVideo = $node->find('idVideo');
	            my $idUser = $node->find('idUser');
                my $date = $node->find('date');
	            my $content = $node->find('content');
                
                my $query = "//collection/". $typeVideo ."[\@id=$idVideo]";
                my $video = function::findItem({ type=>$typeVideo, query=>$query })->get_node(1);
                my $titleVideo = $video->find('title');
                
                my $user = function::findItem({ type=>"user", query=>"//collection/user[\@id=$idUser]" })->get_node(1);
                my $username = $user->find('username');
                my $image = $user->find('image');
        
                print <<COMMENT
                <div class="commento">
				    <div class="userComment">
						  <img src="../images/avatars/$idUser.jpg" class="grav"/> 
						  <b><a href="profile.cgi?id=$idUser">$username</a></b>
						  <span ><u><a href="$typeVideo.cgi?id=$idVideo">$titleVideo</a></u></span>
						  <span class="data">$date</span>
				    </div>
				    <hr></hr>
				    <div class="userText">$content</div>
			    </div>
			    </br>
COMMENT
            }
            if( $x < 20 ){ print "Non ci sono altri commenti";}
        }
    }
}


# stampa tutti i commenti relativi ad un video
# es: function::printCommentsVideo({ typeVideo=>"serie", idVideo=>$id  });
sub printCommentsVideo{
    my $parameters = shift;
    my $typeVideo = $parameters->{typeVideo};
    my $idVideo = $parameters->{idVideo};
    
    print <<COMMENTS;
	      <h2>Commenti</h2>
		  <div id="commenti">
		  </br>
COMMENTS


    my $comments = function::findItem({ type=>"comment", query=>"//collection/comment[idVideo=$idVideo and typeVideo=\"$typeVideo\"]" });

    FOO:{
        if( $comments->size()==0 ){ print "Non ci sono commenti"; last FOO;}
    
        foreach my $node ($comments->get_nodelist) {
            my $content = $node->find('content');
            my $idUser = $node->find('idUser');
            my $date = $node->find('date');
            my $user = function::findItem({ type=>"user", query=>"//collection/user[\@id=$idUser]" })->get_node(1);
            my $username = $user->find('username');
            my $image = $user->find('image');
        
            print <<COMMENT
            <div class="commento">
				<div class="userComment">
						<img src="../images/avatars/$idUser.jpg" class="grav"/> 
						<b><a href="profile.cgi?id=$idUser">$username</a></b>
						<span class="data">$date</span>
				</div>
				<hr></hr>
				<div class="userText">$content</div>
			</div>
			</br>
COMMENT
        }
    }
}


## da togliere !!!!
sub loadComments {
	my $session = CGI::Session->load();
	  if($session->is_expired || $session->is_empty){
			
		}
	  else{
		  print <<COMMENTS;
		  <h2>Commenti</h2>
		  <div id="commenti">
			</br>
			
			<div class="commento">
				<div class="userComment">
						<img src="../images/avatars/1.jpg" class="grav"/> 
						<b><a href="profile.cgi?id=1">Lory</a></b>
						<span class="data">23/02/2012</span>
				</div>
				<hr></hr>
				<div class="userText">Proprio un bel film</div>
			</div>
			</br>
			
			<div class="commento">
				<div class="userComment">
						<img src="../images/avatars/1.jpg" class="grav"/> 
						<b><a href="profile.cgi?id=1">Lory</a></b>
						<span class="data">23/02/2012</span>
				</div>
				<hr></hr>
				<div class="userText">Proprio un bel film</div>
			</div>
			</br>
		 
COMMENTS
	  }
}

























sub countRegisteredUsers{
    my $nodelist = function->findUser();
    return $nodelist->size();
    
}


# funzione che ritorna il massimo id
# riceve come parametro l'indicatore di dove devo cercare: "film", "serie", "user" o "comment"
sub getMaxId {

my $path = $_[1];
my $xp;

switch ($path) {
	case "film" { $xp = XML::XPath->new(filename => $filmsXml); last;}
	case "serie" { $xp = XML::XPath->new(filename => $seriesXml); last;}
	case "comment" { $xp = XML::XPath->new(filename => $commentsXml); last;}
	case "user" { $xp = XML::XPath->new(filename => $usersXml); last;}
}

my $query = "/collection/$path/\@id[not(. <=../preceding-sibling::$path/\@id) and not(. <=../following-sibling::$path/\@id)]";

my $maxId = $xp->findnodes( $query );

return $maxId;
}




1;
