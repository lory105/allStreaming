#!/usr/bin/perl

  use CGI;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session ( '-ip_match' );
  use CGI::Session;
  use function;

  $q = new CGI;
  $user = $q->param('username');
  $psw = $q->param('password');
  

  # process the form
  if($user eq "d" and $psw eq "d")
  {
      $session = new CGI::Session();
      $session->param("username", $user);
      print $session->header(-location=>'index.cgi');
	  #function->redirectTo($session,"films.cgi");
  }
  else
  {
      print $q->header(-type=>"text/html",-location=>"index.cgi");
  }
  


