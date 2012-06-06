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

$session = new CGI::Session();

if( "$cryptedPassword" eq "$password" ){
# da sostituire con:
#if( "$cryptedPassword" eq md5($password) ){

    my $user = function::findItem({type=>"user", query=>"//collection/user[username/text()=\"$username\"]"})->get_node(1);
    
    my $id = $user->findvalue('@id')->string_value;
    my $admin = $user->find("admin")->string_value;
    
    $session->param("username", $username);
    $session->param("id", $id);
    $session->param("admin", $admin);
    
    print $session->header(-location=>'index.cgi');
	#function->redirectTo($session,"films.cgi");
  }
  else{

      #print $session->header(-location=>'index.cgi');
      print $q->header(-type=>"text/html",-location=>"index.cgi?error_login=true");
  }
  


