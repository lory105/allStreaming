#!/usr/bin/perl

  use CGI;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session ( '-ip_match' );
  use CGI::Session;
  use function;
  use XML::XPath;
  use Digest::MD5 qw(md5 md5_hex md5_base64);

  $q = new CGI;
  $username = $q->param('username');
  $password = $q->param('password');

# cerca nel db la presenza dello username inserito, e ne restituisce la password criptata
my $cryptedPassword = function->getPassword($username);  

if( "$cryptedPassword" eq "$password" )
# da sostituire con:
#if( "$cryptedPassword" eq md5($password) )
  {
      $session = new CGI::Session();
      $session->param("username", $username);
      print $session->header(-location=>'index.cgi');
	  #function->redirectTo($session,"films.cgi");
  }
  else
  {
      print $q->header(-type=>"text/html",-location=>"index.cgi");
  }
  


