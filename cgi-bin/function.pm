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
	my $user = $session->param('user');
  if($session->is_expired)
  {
	  print <<LEFT;
    <body>
	<div id="wrapper">
		<div id="header">
			<div id="login">
				<p>Your has session expired. Please login again.</p>
				<form method="post" action="login.cgi">
					<input type="text" name="user" value="User" size="12"/>
					<input type="password" name="psw" value="Password" size="12"/>
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
					<input type="text" name="user" value="User" size="12"/>
					<input type="password" name="psw" value="Password" size="12"/>
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
LEFT
				
				print "Benvenuto $user!";
		print <<LEFT;			
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

sub checkSession {
	
  my $session = CGI::Session->load();

  if($session->is_expired)
  {
      print "Your has session expired. Please login again.";
	  print "<br/><a href='login.pl>Login</a>";
  }
  elsif($session->is_empty)
  {
      print "You have not logged in";
  }
  else
  {
      print "<h2>Welcome</h2>";
  }
	
}



1;
