#!/usr/bin/perl
# script per la visualizzazione di un determinato film

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


# LUCA !!!!!!!!!!!!!!!!!!!!!!!! #################################
binmode(STDOUT, ":iso-8859-1");


my $var=new CGI;
my $id = $var->param('id');
my $node=function->findFilm( "//collection/film[\@id=\"$id\"]")->get_node(1);
my $t=$node->find('title')->string_value;

# prove per vedere risultati ####################################
my $title=function->convert($t);



function->header($title);
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
         <fieldset style="border:0em;">
             <input name="type" value="film" type="hidden" />
             <input name="id" value="$id" type="hidden" />
             <input type="submit" value="Rimuovi Film" />
         </fieldset>
         </form>
         <form method="post" action="addLink.cgi">
         <fieldset style="border:0em;">
             <input name="type" value="film" type="hidden" />
             <input name="id" value="$id" type="hidden" />
             <input type="submit" value="Aggiungi Link" />
         </fieldset>
         </form>
           <br />
FILM
}

my $img=$node->find('image')->string_value;
print "<img src=\"../$img\" class=\"preview\" alt=\"Locandina film\"/>";
my $description = $node->find('description')->string_value;
$description=function->convert($description);
print "<p>$description</p><br />";
my $address=$node->find('address');
foreach my $try ($address->get_nodelist) {
    my $idLink=$try->findvalue('@idLink')->string_value;
    my $linkname=$try->find('linkName')->string_value;
    $linkname=function->convert($linkname);
    my $link=$try->find('link')->string_value;
    print "<p><b>Link:</b> <a href=\"$link\" target=\"_blank\">$linkname</a></p>";
    if( $isAdmin eq "true"){
        print<<FILM
               <form method="post" action="removeItem.cgi">
				<fieldset style="border:0">
                   <input name="type" value="link" type="hidden" />
                   <input name="idFilm" value="$id" type="hidden" />
                   <input name="idLink" value="$idLink" type="hidden" />
                   <input type="submit" value="Rimuovi Link" />
                 </fieldset>
               </form>
FILM
    }
}

print "<br /></div>";

my $session = CGI::Session->load();

# se l'utente è loggato stampo i commenti al film
if( function->isLogged() eq "true"){
	function::printCommentsVideo({ typeVideo=>"film", idVideo=>$id  }); 	
}

print "</div>";

function->footer();
