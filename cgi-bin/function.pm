#!/usr/bin/perl

package function;

use CGI;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
#use CGI qw(:standard);
use strict;
use warnings;
use XML::XPath;
#use XML::XPath::XMLParser;
use XML::LibXML;
#use XML::LibXML::Node;

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
my $nav = $_[0];
    
print<<MENU;
                    <div id="navigation">Ti trovi in : $nav</div>
			            <div id="left_side">
			               <div class="menu">Menu Principale</div>
				               <div class="content">
				                   <ul>
MENU
    
    switch ($nav) {
	   case "Home"  { 
	       print<<MENU;
	           <li><img src="../images/home.png"/><a href="#"><b>Home</b></a><hr></li>
	           <li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
			   <li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
			   <li><img src="../images/signin.png"/><a href="registration.cgi">Registrazione</a><hr></li>
MENU
	       last;
	   }
	   case "Serie" {
	       print<<MENU;
	              <li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
MENU

           my $title = $_[1];
           if( $title eq "" ){
			      print "<li><img src=\"../images/series.png\"/><b>Serie</b><hr></li>";
           }
           else{ 
               print<<MENU;
               <li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a>
                   <ul><li> &nbsp;&nbsp;&nbsp;&nbsp; >  $title </li> </ul>
                   <hr />
               </li>
MENU
           }

           print<<MENU;
			      <li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
			      <li><img src="../images/signin.png"/><a href="registration.cgi">Registrazione</a><hr></li>
MENU
	       last;	       
	   }
	   case "Film" {
	       print<<MENU;
	              <li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
	              <li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
MENU
           my $title = $_[1];
           if( $title eq "" ){
			      print "<li><img src=\"../images/film.png\"/><b>Film</b><hr></li>";
           }
           else{ 
               print<<MENU;
               <li><img src="../images/film.png"/><a href="films.cgi">Film</a>
                   <ul><li> &nbsp;&nbsp;&nbsp;&nbsp; >  $title </li> </ul>
                   <hr />
               </li>
MENU
           }
           print<<MENU;           
			      <li><img src="../images/signin.png"/><a href="registration.cgi">Registrazione</a><hr></li>
MENU
	       last;	       
	   }
	   case "Registrazione" {
	       print<<MENU;
				<li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
				<li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
				<li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
				<li><img src="../images/signin.png"/><b>Registrazione</b><hr></li>
MENU
	       last;	       
	   }
	   
	   case "" {
	       print<<MENU;
				<li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
				<li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
				<li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
				<li><img src="../images/signin.png"/><a href="registration.cgi">Registrazione</a><hr></li>
MENU
	       last;	       
	   }
    }

print<<MENU;
                    </ul>
					</br>
				</div>
		</div>	
MENU

}

sub menu {
    my $nav = $_[0];
    
    my $session = CGI::Session->load();
    my $id = $session->param('id');
    my $self = $session->param('username');
    
    
    print<<MENU;
                    <div id="navigation">Ti trovi in : $nav</div>
			            <div id="left_side">
			               <div class="menu">Menu Principale</div>
				               <div class="content">
		      <ul>
MENU

    switch ($nav) {
	   case "Home"  { 
	       print<<MENU;
	              <li><img src="../images/home.png"/><b>Home</b><hr></li>
	              <li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
			      <li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
			      <li><img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr></li>
			      <li><img src="../images/profile.png"/><a href="profile.cgi?id=$id">Profilo</a><hr></li>
MENU
	       last;
	   }
	   
	   	   case "Serie"  { 
	       print<<MENU;
	              <li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
MENU

           my $title = $_[1];
           if( $title eq "" ){
			      print "<li><img src=\"../images/series.png\"/><b>Serie</b><hr></li>";
           }
           else{ 
               print<<MENU;
               <li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a>
                   <ul><li> &nbsp;&nbsp;&nbsp;&nbsp; >  <b>$title</b> </li> </ul>
                   <hr />
               </li>
MENU
           }

           print<<MENU;
			      <li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
			      <li><img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr></li>
			      <li><img src="../images/profile.png"/><a href="profile.cgi?id=$id">Profilo</a><hr></li>
MENU
	       last;
	   }
	   
	   case "Film"  { 
	       print<<MENU;
	              <li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
	              <li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
MENU
           my $title = $_[1];
           if( $title eq "" ){
			      print "<li><img src=\"../images/film.png\"/><b>Film</b><hr></li>";
           }
           else{ 
               print<<MENU;
               <li><img src="../images/film.png"/><a href="films.cgi">Film</a>
                   <ul><li> &nbsp;&nbsp;&nbsp;&nbsp; >  <b>$title</b> </li> </ul>
                   <hr />
               </li>
MENU
           }
           print<<MENU;           
			      <li><img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr></li>
			      <li><img src="../images/profile.png"/><a href="profile.cgi?id=$id">Profilo</a><hr></li>
MENU
	       last;
	   }

	   case "Commenti"  { 
	       print<<MENU;
	       	      <li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
	              <li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
			      <li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
			      <li><img src="../images/comment.png"/><b>Commenti</b><hr></li>
			      <li><img src="../images/profile.png"/><a href="profile.cgi?id=$id">Profilo</a><hr></li>
MENU
	       last;
	   }

        case "Profilo" {
        print<<MENU;
	       	      <li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
	              <li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
			      <li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
			      <li><img src="../images/comment.png"/><a href="comments.cgi">Commenti</a><hr></li>
MENU
           my $username = $_[1];
           if( $username eq "" || $username eq $self){
			      print "<li><img src=\"../images/profile.png\"/><b>Profilo</b><hr></li>";
           }
           else{
               print<<MENU;
               <li><img src="../images/profile.png"/><a href="profile.cgi?id=$id">Profile</a>
                   <ul><li> &nbsp;&nbsp;&nbsp;&nbsp; >  <b>$username</b> </li> </ul>
                   <hr />
               </li>
MENU
           }
			      
        }
        case "" {
	       print<<MENU;
				<li><img src="../images/home.png"/><a href="index.cgi">Home</a><hr></li>
				<li><img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr></li>
				<li><img src="../images/film.png"/><a href="films.cgi">Film</a><hr></li>
				<li><img src="../images/signin.png"/><a href="registration.cgi">Registrazione</a><hr></li>
MENU
	       last;	       
	   }
    }



	 print<<MENU
	 		      </ul>
					</br>
				</div>
		</div>	
MENU
}


sub left {

    my $session = CGI::Session->load();
    #my $cgi = new CGI;
    #my $session  = new CGI::Session(undef, $cgi, undef );
    if($session->is_expired || $session->is_empty){
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
LEFT

        my $q = new CGI;
        my $error_login = $q->param('error_login');
        if( $error_login eq "true" ){ 
            print "<p>Errore nel login</p>";     #!! X LUCA: applica il css ( è il mess di errore k compare se il login fallisce)
        }

        print <<LEFT;
	  			</div>
			</div>	
LEFT


        menuNotLogged($_[1], $_[2]);
    }
  
    else{
        my $username = $session->param('username');
        print <<LEFT;
		<body>
			<div id="wrapper">
				<div id="header">
					<div id="login">
						<div class="userLogged">
LEFT

		my $user = function::findItem({ type=>"user", query=>"//collection/user[username=\"$username\"]" });
		my $id;
		foreach my $node ($user->get_nodelist) {
			$id = $node->find('@id')->string_value;
		}
		print <<LEFT;
                            <div class=\"avatar\"> <img src=\"../images/avatars/$username.jpg\" class=\"grav\"/> </div>
		                    <div class=\"name\">Benvenuto, <B><a href=\"profile.cgi?id=$id\">$username</a></B> <br><a href=\"logout.cgi\">Logout</a></div>
					    </div>
				    </div>
			    </div>
LEFT
        menu($_[1], $_[2]);
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

FOO: {
    # se non ci sono commenti nel DB
    my $arraySize = @sortIdComment;
    my @idFilmSelected;
    my @idSerieSelected;
    if( $arraySize==0 ){ print "Non ci sono commenti"; last FOO;}
    
    my $video; my $x; my $y=1;
    
    for($x = 0; scalar @sortIdComment >$y && $x < 5; $x++) {
            
	    my $idComment = "$sortIdComment[$y]";
	    my $node = function::findItem({ type=>"comment", query=>"//collection/comment[\@id=$idComment]" })->get_node(1);
    
	    my $typeVideo; my $idVideo;
	
        # dal singolo commento cerco a quale video si riferisce
    	$typeVideo = $node->find('typeVideo')->string_value;
	    $idVideo= $node->find('idVideo')->string_value;
    
        # cerco il video con l'id corrispondente 
        if( $typeVideo eq "film"){
            # controllo di non aver già inserito il film con id = $idVideo            
            my %params = map { $_ => 1 } @idFilmSelected;
            if(exists($params{$idVideo})) { $x = $x - 1; }
            else{
                push( @idFilmSelected, $idVideo);
                $video = function::findItem({ type=>$typeVideo, query=>"//collection/film[\@id=$idVideo]" })->get_node(1);
                my $title = $video->find('title')->string_value;
	            print "<a href=\"$typeVideo.cgi?id=$idVideo\" >$title</a></br>";
            }
        }
        #if( $typeVideo eq "serie"){
         else{
            # controllo di non aver già inserito la serire con id = $idVideo
            my %params = map { $_ => 1 } @idSerieSelected;
            if(exists($params{$idVideo})) { $x = $x - 1; }
            else{        
                push( @idSerieSelected, $idVideo);
                $video = function::findItem({ type=>$typeVideo, query=>"//collection/serie[\@id=$idVideo]" })->get_node(1);
                my $title = $video->find('title')->string_value;
        	    print "<a href=\"$typeVideo.cgi?id=$idVideo\" >$title</a></br>";
            }
        }
    
	    $y = $y+1;
    }
}

print <<RIGHT;
				</div>
			<div class="news">Novit&agrave;</div>
				<div class="content_max_view">
RIGHT

my @sortIdFilm = function::sortIdItemByDate({ type=>"film" });

FOO: {
    # se non ci sono commenti nel DB
    my $arraySize = @sortIdFilm;
    if( $arraySize==0 ){ print "Non ci sono film"; last FOO;}
    

    # creo dinamicamente i link ai 5 film più recenti 
    my $i;
    for($i = 0; scalar @sortIdFilm >$i && $i < 5; $i++) {
	   my $id = "$sortIdFilm[$i]";
	   my $nodeset = function::findItem({ type=>"film", query=>"//collection/film[\@id=$id]/title/text()" });
	   print "<a href=\"film.cgi?id=$id\" >$nodeset</a></br>";
    }
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
    #print $root->toString();
    
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
    my $max = function->getMaxId("serie");
    $max = "$max" + 1;
   
    my $title = $parameters->{title};
    my $image = $parameters->{image};
    my $description = $parameters->{description};
    
    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $seriesXml );
    # extract the root element
    my $root = $doc->getDocumentElement();

    # string with the new element
    my $newNode = "\t<serie id=\"$max\">\n\t\t<title>$title</title>\n\t\t<image>$image</image>\n\t\t<description>$description</description>\n\t</serie>\n";
    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newNode); 
    # insert the new child
    $root->appendChild($fragment);
    
    	
    
    # write to file
    open(OUT,'>:utf8',$seriesXml ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}


# aggiunge un episodio ad una stagione di una serie
sub addEpisode{
    my $parameters = shift;
    my $idSerie = $parameters->{idSerie};
    my $idSeason = $parameters->{idSeason};
    my $title = $parameters->{title};
    my $link = $parameters->{link};


    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $seriesXml );
    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");
    # recupero il nodo del film da modificare
    my $newNode = $xpc->findnodes("//collection:serie[\@id=\"$idSerie\"]", $doc )->get_node(1);
    my $oldNode = $newNode;

    # extract the root element
    my $root = $doc->getDocumentElement();

    my $maxId = function->getMaxId("link", $idSerie);
    $maxId = "$maxId" + 1;

    # string with the new element
    my $newAddressNode = "\t\t\t\t<episode idEpisode=\"$maxId\">\n\t\t\t\t\t<title>$title</title>\n\t\t\t\t\t<link>$link</link>\n\t\t\t\t</episode>\n";

    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newAddressNode);
    # insert the new child
    $newNode->appendChild($fragment);
    
    $root->removeChild( $oldNode );
    $root->appendChild($newNode);
    # debug da togliere!!!
    
    # write to file
    open(OUT,'>:utf8',$seriesXml ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}

# aggiunge in modo incrementale una stagione ad una serie
# function::addSeason({ idSerie=>$id });
sub addSeason{
    my $parameters = shift;
    my $idSerie = $parameters->{idSerie};
    
    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $seriesXml );
    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");
    # recupero il nodo della serie da modificare
    my $newNode = $xpc->findnodes("//collection:serie[\@id=\"$idSerie\"]", $doc )->get_node(1);
    my $oldNode = $newNode;

    # extract the root element
    my $root = $doc->getDocumentElement();

    my $maxId = function->getMaxId( "season", $idSerie );
    $maxId = "$maxId" +1;

    # string with the new element
    my $newAddressNode = "\t\t<season number=\"$maxId\">\n\t\t</season>\n";

    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newAddressNode);
    # insert the new child
    $newNode->appendChild($fragment);
    
    $root->removeChild( $oldNode );
    $root->appendChild($newNode);
    
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

    my $maxId = function->getMaxId("link", $idFilm);
    $maxId = "$maxId" + 1;

    # string with the new element
    my $newAddressNode = "\t\t<address idLink=\"$maxId\">\n\t\t\t<linkName>$linkName</linkName>\n\t\t\t<link>$link</link>\n\t\t</address>\n";

    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newAddressNode);
    # insert the new child
    $newNode->appendChild($fragment);
    
    $root->removeChild( $oldNode );
    $root->appendChild($newNode);
    # debug da togliere!!!
    
    # write to file
    open(OUT,'>:utf8',$filmsXml ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
    
}

# rimuove un film, una serie ..
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
	   case "comment" { $file = $commentsXml;
	                    $query = "//collection:comment[\@id=\"$id\"]"; last;
	   }
    }
    
    $doc = $parser->parse_file( $file );

    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");

    my $node = $xpc->findnodes( $query, $doc )->get_node(1);
  
    # extract the root element
    my $root = $doc->getDocumentElement();
 
    $root->removeChild( $node );
    # debug da togliere!!!

    
    # write to file
    open(OUT,'>:utf8',$file ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);

}


# rimuove un link di un film
# es: function:removeLink({ idFilm=>$idFilm, idLink=>$idLink });
sub removeLink{
    my $parameters = shift;
    my $idFilm = $parameters->{idFilm};
    my $idLink = $parameters->{idLink};

    my $parser = XML::LibXML->new;
    my $doc; my $file;

    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");
    
	$file = $filmsXml;  
	my $query1 = "//collection:film[\@id=\"$idFilm\"]";
	my $query2 = "//collection:film[\@id=\"$idFilm\"]/collection:address[\@idLink=\"$idLink\"]";
    
    $doc = $parser->parse_file( $file );

    my $oldFilm = $xpc->findnodes( $query1, $doc )->get_node(1);
    my $newFilm = $oldFilm;

    my $link = $xpc->findnodes( $query2, $doc )->get_node(1);
    
    $newFilm->removeChild( $link );
    
    # extract the root element
    my $root = $doc->getDocumentElement();
    $root->removeChild( $oldFilm);
    $root->appendChild( $newFilm);

    # write to file
    open(OUT,'>:utf8',$file ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}

=o
# rimuove un episodio di una stagione di una serie
# es: function:remove ({ idFilm=>$idFilm, idLink=>$idLink });
sub removeEpisode{
    my $parameters = shift;
    my $idSerie =  $parameters->{idSerie};
    my $idEpisode =  $parameters->{id};

    my $parser = XML::LibXML->new;
    my $doc; my $file;

    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");
    
	$file = $filmsXml;  
	my $query1 = "//collection:film[\@id=\"$idSerie\"]";
	my $query2 = "//collection:film[\@id=\"$idEpisode\"]/collection:address[\@idLink=\"$idLink\"]";
    
    $doc = $parser->parse_file( $file );

    my $oldFilm = $xpc->findnodes( $query1, $doc )->get_node(1);
    my $newFilm = $oldFilm;

    my $link = $xpc->findnodes( $query2, $doc )->get_node(1);
    
    $newFilm->removeChild( $link );
    
    # extract the root element
    my $root = $doc->getDocumentElement();
    $root->removeChild( $oldFilm);
    $root->appendChild( $newFilm);

    # write to file
    open(OUT,'>:utf8',$file ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}

=cut


# rimuove uno user
# function::removeUser({ id=>"3"});
sub removeUser {
    my $parameters = shift;
    my $id = $parameters->{id};


    # prima rimuovo tutti i commenti dell'utente  !!


    ######
    
    
    my $parser = XML::LibXML->new;
    my $query = "//collection:user[\@id=\"$id\"]";
    my $doc = $parser->parse_file( $usersXml );

    my $xpc = XML::LibXML::XPathContext->new;
    $xpc->registerNs("collection", "http://allStreaming.altervista.org");

    my $node = $xpc->findnodes( $query, $doc )->get_node(1);
  
    # extract the root element
    my $root = $doc->getDocumentElement();
 
    $root->removeChild( $node );
    
    # write to file
    open(OUT,'>:utf8',$usersXml ) || die("Cannot open file");
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

#in $[1] passo lo username, in $[2] l'email
sub checkUserRegistration{
	my $username = $_[1];
	my $email = $_[2];
	my $xp = XML::XPath->new(filename => $usersXml);
	my $query="//collection/user[username/text()=\"$username\"]";
	my $result=$xp->findnodes( $query );
	if($result->size() == 0){
		$query="//collection/user[email/text()=\"$email\"]";
		$result=$xp->findnodes( $query );
	}
	return $result;
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


# controlla se l'utente è loggato (cioè se ha la sua sessione)
sub isLogged{
    my $session = CGI::Session->load();

    if($session->is_expired || $session->is_empty){ return "false";}
    return "true";
}


# controlla se l'utente è l'admin: ritorna true o false
# es: if( function->checkIsAdmin() eq "false" ){ ... } 
sub checkIsAdmin{
    my $session = CGI::Session->load();
    my $admin = $session->param('admin');

    # se l'utente non è loggato o non è l'amministratore
    if($session->is_expired || $session->is_empty || $admin eq "false" ){ return "false"; }
    else{ return "true"; }
}


sub redirectTo {
	print $_[1]->header(-location=>"$_[2]");
}



# stampa gli ultimi X commenti inseriti
sub printAllComments{

     print <<COMMENTS;
			<div id="center_side">
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
        
                print <<COMMENT;
                <div class="commento">
				    <div class="userComment">
						  <img src="../images/avatars/$username.jpg" class="grav"/> 
						  <b><a href="profile.cgi?id=$idUser">$username</a></b>
						  <span class="data">$date</span>
				    </div>
				    <b><a href="$typeVideo.cgi?id=$idVideo">$titleVideo</a></b>
				    <hr></hr>
				    <div class="userText">$content</div>
			    </div>
			    </br>
COMMENT
            }
            if( $x < 20 ){ print "Non ci sono altri commenti";}
        }
    }
	print <<COMMENT;
	</div>
COMMENT
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
    
    if( function->checkIsAdmin() eq "false" ){    
        print <<COMMENTS;
			<div class="commento">
		  		<form name="comment" method="post" action="checkComment.cgi" >
					<fieldset>
						<span class="sx"><textarea rows="4" cols="10" style="width:100%;" id="userComment" name="userComment" value="Inserisci il tuo commento" >commento</textarea></span>
						<span class="dx"><button type="submit" id="send" >Invia</button></span>
						<input type="hidden" name="id" value="$idVideo" /> 
						<input type="hidden" name="type" value="$typeVideo" /> 
					</fieldset>
				</form>
			</div>
		 </br>
COMMENTS
    }


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
        
            print <<COMMENT;
            
            <div class="commento">
				<div class="userComment">
						<img src="../images/avatars/$username.jpg" class="grav"/> 
						<b><a href="profile.cgi?id=$idUser">$username</a></b>
						<span class="data">$date</span>
COMMENT
            
            
            if( function->checkIsAdmin() eq "true" ){
                my $id = $node->findvalue('@id')->string_value;
                print<<COMMENT;
               <form method="post" action="removeItem.cgi">
                   <input name="type" value="comment" type="hidden">
                   <input name="id" value="$id" type="hidden">
                   <input type="submit" value="Rimuovi Commento">
               </form>
COMMENT
            }
            print<<COMMENT;
				</div>
				<hr></hr>
				<div class="userText">$content</div>
			</div>
			</br>
		
COMMENT
        }
      print <<CLOSE;
     </div>
CLOSE
    }
}

sub countRegisteredUsers{
    my $nodelist = function->findUser();
    return $nodelist->size();
    
}


# funzione che ritorna il massimo id
# riceve come parametro l'indicatore di dove devo cercare: "film", "serie", "user" o "comment"
# es function->getMaxId("film", $idFilm );
sub getMaxId {

my $type = $_[1];
my $xp; my $query;

switch ($type) {
	case "film" { $xp = XML::XPath->new(filename => $filmsXml); 
	              $query = "/collection/$type/\@id[not(. <=../preceding-sibling::$type/\@id) and not(. <=../following-sibling::$type/\@id)]";
	              last;
	}
	case "serie" { $xp = XML::XPath->new(filename => $seriesXml);
	               $query = "/collection/$type/\@id[not(. <=../preceding-sibling::$type/\@id) and not(. <=../following-sibling::$type/\@id)]";
	               last;
	}
	case "comment" { $xp = XML::XPath->new(filename => $commentsXml);
                     $query = "/collection/$type/\@id[not(. <=../preceding-sibling::$type/\@id) and not(. <=../following-sibling::$type/\@id)]";
	                 last;
	}
	case "user" { $xp = XML::XPath->new(filename => $usersXml);
                  $query = "/collection/$type/\@id[not(. <=../preceding-sibling::$type/\@id) and not(. <=../following-sibling::$type/\@id)]";
	              last;
	}
	case "link" {$xp = XML::XPath->new(filename => $filmsXml);
	             my $idFilm= $_[2];
	             $query = "/collection/film[\@id=\"$idFilm\"]/address/\@idLink[not(. <=../preceding-sibling::address/\@idLink) and not(. <=../following-sibling::address/\@idLink)]";
	             last;
	}
	case "season" {$xp = XML::XPath->new(filename => $seriesXml);
	             my $idSerie= $_[2];
	             $query = "/collection/serie[\@id=\"$idSerie\"]/season/\@number[not(. <=../preceding-sibling::season/\@number) and not(. <=../following-sibling::season/\@number)]";
	             last;
	}	
	
}

my $maxId = $xp->findnodes( $query );

if( ! $maxId ){ return 0;}
return $maxId;
}

# ritorna un numero "number" di video (film e serie ) scelte a random
sub randomVideo{
    my $parameters = shift;
    my $number = $parameters->{number};
    
    print <<CENTER;
		<div id="center_side">
				<h1>Alcuni Film</h1>
				<div id="random_film">
				<br />
CENTER
    
    my @sortIdFilm = function::sortIdItemByDate({ type=>"film"});

    FOO: {
        # se non ci sono film nel DB
        my $arraySize = @sortIdFilm;
        if( $arraySize==0 ){ print "Non ci sono film"; last FOO;}
        else{
            my @idFilmSelected; my $x;
            
            for($x = 0; scalar @sortIdFilm >$x && $x < $number ; $x++) {
                FOO: {    
                
                my $random_number = int(rand( $arraySize ));
                my $idFilm = $sortIdFilm[ $random_number ];
                
                my %params = map { $_ => 1 } @idFilmSelected;

                if(exists($params{$idFilm})) { $x = $x - 1; last FOO; }
                $idFilmSelected[$x]= $idFilm;
                                    
	            my $node = function::findItem({ type=>"film", query=>"//collection/film[\@id=$idFilm]" })->get_node(1);
	           
	            my $title = $node->find('title')->string_value;
	            my $image = $node->find('image')->string_value;
	            
	            print<<CENTER
   						<div class="film">
   						
							<img for="link" src=\"../$image\" class="locandina" />
							</br>
							<a id="link" href="film.cgi?id=$idFilm">Film: $title</a>
							<br /><br />
						</div>
CENTER
                }
            }
            
            print<<CENTER
                    </div>
		      </div>
CENTER
        }         
    }
}

sub addComment{
    my $parameters = shift;
    my $maxId = function->getMaxId("comment");
    $maxId = "$maxId" + 1;
    
    my $idReference = $parameters->{id};
    my $type = $parameters->{type};
    my $comment = $parameters->{comment};
    my $idUser = $parameters->{idUser};
    my $date = $parameters->{dateComment};
    
    my $parser = XML::LibXML->new;
    my $doc = $parser->parse_file( $commentsXml );
    # extract the root element
    my $root = $doc->getDocumentElement();

    # string with the new element
    my $newNode = "\t<comment id=\"$maxId\">\n\t\t<idUser>$idUser</idUser>\n\t\t<typeVideo>$type</typeVideo>\n\t\t<idVideo>$idReference</idVideo>\n\t\t<date>$date</date>\n\t\t<content>$comment</content>\n\t</comment>\n";

    # check if it's well formed and create the node
    my $fragment = $parser->parse_balanced_chunk($newNode);
    # insert the new child
    $root->appendChild($fragment);
    
    # write to file
    open(OUT,'>:utf8',$commentsXml ) || die("Cannot open file");
    print OUT $root->toString();
    close(OUT);
}


1;
