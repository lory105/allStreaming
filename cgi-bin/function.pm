#!/usr/bin/perl

package function;

use CGI;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
#use CGI qw(:standard);
use strict;
use warnings;
#use XML::XPath;
#use XML::XPath::XMLParser;
#use XML::LibXML;
use Digest::MD5 qw(md5 md5_hex md5_base64);


# path db films
my $filmsXml = "../xml/films.xml";






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
				print "<div class=\"name\"> $user <br><a href=\"logout.cgi\">Logout</a></div>";
		print <<LEFT;			
				</div>
			</div>
		</div>	
LEFT
  }
menu($_[1]);
}

sub right {
	
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
					Primo</br>
					Secondo</br>
					Terzo</br>
					Quarto</br>
					Quinto</br> 
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


# funzione di ricerca film: se non riceve parametri (!$_[1]) ricerca tutti i film,
# altrimenti esegue la query ricevuta in $_[1]  
sub findFilm {

# creo un oggetto XPath e gli associo il file xml dove cercare
my $xp = XML::XPath->new(filename => $filmsXml);

my $query;

# se ricevo la query
if( $_[1]){
$query = $_[1];
}
# altrimenti cerco tutti i fiml
else{
$query = "//collection/film";
}

print "$query" . "\n";

#$xp->find()->get_nodelist;
#return $xp->find( $query )->get_nodelist;
return $xp->findnodes( $query );

}


# riceve in input lo username dell'utente che sta facendo il login, controlla nel db la presenza di tale username
# restituendone la password corrispondente che è criptata
sub get_password() {

# $_[0] contiene lo username

my $crypted_password;

return $crypted_password;

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
					<div class="pict"> 
						<img src="../images/avatars/1.jpg" class="grav"/> 
						<p>Lory</p>
					</div>
				</div>
				<div class="userText">Proprio un bel film</div>
			</div>
		  </div>
			
	
COMMENTS
	  }
}

1;
