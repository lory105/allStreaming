#!/usr/bin/perl 

use strict;
use warnings;
use CGI;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
use XML::XPath;
use XML::XPath::XMLParser;
use XML::LibXML;

	my $usersXml = "../xml/users.xml";
	my $form = new CGI;
	my $comment = $form->param('userComment');
	my $id = $form->param('id');
	my $type = $form->param('type');
	my $dateComment   = DateTime->now;
	
	my $session = CGI::Session->load();
	my $username = $session->param('username');
	
	my $xp = XML::XPath->new(filename => $usersXml);
	my $query= "//collection/user[username/text()=\"$username\"]";
	my $user = $xp->find( $query );
	my $userId;
	
	foreach my $node ($user->get_nodelist) {
		$userId = $node->findvalue('@id')->string_value;
    }

	function::addComment({ id=>"$id", type=>"$type", idUser=>"$userId", comment=>"$comment", dateComment=>"$dateComment" });
	print $form->redirect($type.'.cgi?id='.$id);
