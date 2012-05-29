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
		</head> 
	
HEADER

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
					<img src="../images/comment.png"/><a href="#">Commenti</a><hr>
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
					<img src="../images/comment.png"/><a href="#">Commenti</a><hr>
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
					<img src="../images/comment.png"/><a href="#">Commenti</a><hr>
					</br>
				</div>
		</div>	
MENU
	}
if($_[0] eq "commenti"){
print<<MENU
			<div id="navigation">Ti trovi in : Commenti</div>
			<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
					<img src="../images/comment.png"/><a href="#"><b>Commenti</b></a><hr>
					</br>
				</div>
		</div>	
MENU
	}
}

sub left {

	my $session = CGI::Session->load();
	my $user = $session->param('username');
  if($session->is_expired)
  {
	  print <<LEFT;
    <body>
	<div id="wrapper">
		<div id="header">
			<div id="login">
				<p>Your has session expired. Please login again.</p>
				<form method="post" action="login.cgi">
					<input type="text" name="username" value="User" size="12"/>
					<input type="password" name="password" value="Password" size="12"/>
					<button type="submit" id="sending">Login</button>
				</form>
			</div>
		</div>	
LEFT
  }
  elsif($session->is_empty)
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
  }
menu($_[1]);
}


sub right {

my @sortId = function->sortIdFilmByDate();



# year-from-dateTime(datetime)


print <<RIGHT;
			<div id="right_side">
			<div class="view">I pi&ugrave; visti</div>
				<div class="content_max_view">
					Primo</br>
					Secondo</br>
					Terzo</br>
					Quarto</br>
					Quinto</br> 
				</div>
			<div class="news">Novit&agrave;</div>
				<div class="content_max_view">
RIGHT

# creo dinamicamente i link ai 5 film più recenti 
my $i;
for($i = 0; $i < 5; $i++) {
	my $id = "$sortId[$i]";
	my $nodeset = function->findFilm("//collection/film[\@id=$id]/title/text()");
	print "<a href=\"film.cgi?id=$id\" >$nodeset</a></br>";

}

print <<RIGHT;
				</div>
			<div class="news">User Online</div>
			<div class="content_max_view">100 visitatori online </div>
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
			<a href="#">About Us </a>-
			<a href="#"> Contact Us</a>
		</div>
    </body>
</html>

FOOTER
	
}


# ritorna gli id di tutti i film, ordinati per data di uscita ( dal + recente al meno recente )
sub sortIdFilmByDate{

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
return @sortId;

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


# funzione di ricerca user: se non riceve parametri (!$_[1]) ricerca tutti gli user,
# altrimenti esegue la query ricevuta in $_[1] 
sub getUser {

# creo un oggetto XPath e gli associo il file xml dove cercare
my $xp = XML::XPath->new(filename => $usersXml);

####### okkk da ricordare !!!
#my $id = "user-1";
#my $query= "//collection/user[\@id=\"$id\"]"; ## attenzione sintassi!!
#my $io = $xp->findnodes( $query );
#print $io;
#################


my $query;
if( $_[1] ){ $query= $_[1]; }
else{ $query= "//collection/user"; }

return $xp->findnodes( $query );
}

sub redirectTo {
	print $_[1]->header(-location=>"$_[2]");
}

sub loadComments {
	my $session = CGI::Session->load();
	  if($session->is_expired || $session->is_empty){
			
		}
	  else{
		  print <<COMMENTS;
		  <h2>Commenti</h2>
		  <div id="commenti">
			<div class="commento">
				<div class="userComment">
						<img src="../images/avatars/1.jpg" class="grav"/> 
						<p><b>Lory</b></p>
				</div>
				<div class="userText">Proprio un bel film</div>
			</div>
			<hr/>
			<div class="commento">
				<div class="userComment">
						<img src="../images/avatars/1.jpg" class="grav"/> 
						<p><b>Lory</b></p>
				</div>
				<div class="userText">Proprio un bel film</div>
			</div></br>
		  </div>
		  
COMMENTS
	  }
}

1;
