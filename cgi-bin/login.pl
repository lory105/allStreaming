#!/usr/bin/perl

  use CGI;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session ( '-ip_match' );
  
  $q = new CGI;
  $user = $q->param('user');
  $psw = $q->param('psw');
  

  # process the form
  if($user eq "demo" and $psw eq "demo")
  {
      $session = new CGI::Session();
      print $session->header(-location=>'index.cgi');
  }
  else
  {
      print $q->header(-type=>"text/html",-location=>"index.cgi");
  }
  
1;

