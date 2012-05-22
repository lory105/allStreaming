#!/usr/bin/perl

package function;

use CGI;
use strict;
use warnings;
use Digest::MD5 qw(md5 md5_hex md5_base64);



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
print <<LEFT;
    <body>
	<div id="wrapper">
		<div id="header">
			<div id="login">
				<form method="post" action="check_login.cgi">
					<input type="text" name="username" value="username" size="12"/>
					<input type="password" name="password" value="password" size="12"/>
					<button type="submit" id="sending">Login</button>
				</form>
			</div>
		</div>	
		
		<div id="navigation">Ti trovi in : Home</div>
LEFT
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











# legge i valori di una qualsiasi form e li salva nella hash %input che ritorna
sub take_form_values {
my %input; my $buffer; my @pairs; my $pair; my $name; my $value;

read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);					# divido ogni coppia di valore (key=value) ricevuta dalla form
foreach $pair (@pairs) {
( $name, $value) = split(/=/, $pair);
#$value =~ tr/+/ /;
#$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/g;
#$name =~ tr/+/ /;
#$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C",hex($1))/g;

$input{$name} = $value;

}

return %input;
}


# riceve in input lo username dell'utente che sta facendo il login, controlla nel db la presenza di tale username
# restituendone la password corrispondente che è criptata
sub get_password() {

# $_[0] contiene lo username

my $crypted_password;

return $crypted_password;

}


# fa la redirect in un'altra URL passata come parametro
sub redirect_to {

my $query=new CGI;
print $query->redirect( "index.cgi" );    # da sostituire con la riga sotto k xo non va!!!!!!

# print $query->redirect( "$_[0]" );  # questa non va, non capisco xk!!!!!!!!!!!!!!!!!!!!
}



1;
