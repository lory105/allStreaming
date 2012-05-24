#!/usr/bin/perl

  use CGI;
  use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
  use CGI::Session ( '-ip_match' );
  use CGI::Session;
  
  my $page=new CGI;
  $session = CGI::Session->load();
  $session->delete();
  print $page->redirect("index.cgi");
