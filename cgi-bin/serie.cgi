#!/usr/bin/perl
# script per la visalizzazione di una determinata serie TV

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


my $var=new CGI;
my $id = $var->param('id');
my $node=function->findSerie( "//collection/serie[\@id=\"$id\"]")->get_node(1);
my $title=$node->find('title')->string_value;

function->header($title);
function->left("Serie", $title );
function->right();


print<<SERIE;
	<div id=\"center_side\">
	<div id=\"random_film\">
	<h1>$title</h1>
SERIE

my $isAdmin = function::checkIsAdmin(); 
if( $isAdmin eq "true"){
    print<<SERIE
         <form method="post" action="removeItem.cgi">
             <input name="type" value="serie" type="hidden">
             <input name="id" value="$id" type="hidden">
             <input type="submit" value="Rimuovi Serie">
         </form>
         <form method="post" action="addSeason.cgi">
             <input name="id" value="$id" type="hidden">
             <input type="submit" value="Aggiungi stagione">
         </form>
              <br />
SERIE
}
	
my $img=$node->find('image')->string_value;
print "<img src=\"../$img\" class=\"preview\"/>";
my $description = $node->find('description')->string_value;
print "<p>$description</p></br>";
my $seasons=$node->find('season');
my @sortIdSeason;       # array contenente il numero delle stagioni
my %sortSeason;         # key = number season, value = node season

# memorizzo i numeri delle stagioni della serie per stamparle in ordine crescente
foreach my $node ($seasons->get_nodelist) {
	my $number=$node->getAttribute('number');
	
	$sortSeason{$number}= $node;
	push( @sortIdSeason, $number);
}

# ordino l'array con i numeri delle stagini in modo crescente
@sortIdSeason = sort { $a <=> $b } @sortIdSeason;
	
my $x;
for($x=0; $x < scalar @sortIdSeason; $x++){
    my $number = $sortIdSeason[$x];
    my $node = $sortSeason{ $number };
    
	if( $isAdmin eq "true"){
        print<<SERIE
		 <h3>Stagione $number -- <a href=\"addEpisode.cgi?id=$id&idSeason=$number\" >Aggiungi Episodio</a></h3>
SERIE
	}
    else{ print "<h3>Stagione $number</h3>"; }
	my $episodes=$node->find('episode');
	print "<div class=\"episodes\">";
	foreach my $episode ($episodes->get_nodelist) {
		my $title=$episode->find('title')->string_value;
		my $link=$episode->find('link')->string_value;
		print "<p><a href=\"$link\" target=\"_blank\">$title</a></p>";
	}
	print "</div><br />";
}

print "</div>";

if( function->isLogged() eq "true"){ 
    function::printCommentsVideo({ typeVideo=>"serie", idVideo=>$id  });
}

print "</div>";

function->footer();
