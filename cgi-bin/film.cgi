#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );

function->header();


my $var=new CGI;
my $id = $var->param('id');
my $node=function->findFilm( "//collection/film[\@id=\"$id\"]")->get_node(1);
my $title=$node->find('title')->string_value;

function->left("Film", $title );
function->right();

print<<FILM;
	<div id=\"center_side\">\n
	   <div id=\"random_film\">\n
	       <h1>$title</h1>
FILM


my $isAdmin = function::checkIsAdmin(); 
if( $isAdmin eq "true"){
    print<<FILM
         <form method="post" action="removeItem.cgi">
             <input name="type" value="film" type="hidden">
             <input name="id" value="$id" type="hidden">
             <input type="submit" value="Rimuovi Film">
         </form>
         <form method="post" action="addLink.cgi">
             <input name="type" value="film" type="hidden">
             <input name="id" value="$id" type="hidden">
             <input type="submit" value="Aggiungi Link">
         </form>
           <br></br>
FILM
}

my $img=$node->find('image')->string_value;
print "<img src=\"../$img\" class=\"preview\"/>";
my $description = $node->find('description')->string_value;
print "<p>$description</p></br>";
my $address=$node->find('address');
foreach my $try ($address->get_nodelist) {
    my $idLink=$try->findvalue('@idLink')->string_value;
    my $linkname=$try->find('linkName')->string_value;
    my $link=$try->find('link')->string_value;
    print "<p><b>Link:</b> <a href=\"http://$link\" target=\"_blank\">$linkname</a></p>";
    if( $isAdmin eq "true"){
        print<<FILM
               <form method="post" action="removeItem.cgi">
                   <input name="type" value="link" type="hidden">
                   <input name="idFilm" value="$id" type="hidden">
                   <input name="idLink" value="$idLink" type="hidden">
                   <input type="submit" value="Rimuovi Link">
               </form>
FILM
    }
}

print "<br /></div>";

my $session = CGI::Session->load();

if($session->is_expired || $session->is_empty){}
else{ 
	function::printCommentsVideo({ typeVideo=>"film", idVideo=>$id  }); 	
}

print "</div></div>";

function->footer();
