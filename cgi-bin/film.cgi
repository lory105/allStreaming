#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );

function->header();
function->left("film");
function->right();


print<<BODY;    
		<div id="center_side">
			<div id="random_film">
				<h1>Transformers</h1>
				<img src="../images/transformers.jpg" class="preview"/>	
				<p>La lotta tra il bene (gli Autobots) e il male (i Decepticons), dal pianeta Cybertron si spostata sulla Terra dove milioni di anni fa caduto il Cubo di Energon, il potere supremo capace di infondere la vita ai Transformers. Sam Witwicky - nipote dell'esploratore che per primo, durante una missione nel Circolo Polare Artico sul finire del 1800, ebbe a che fare con Megatron, il capo dei Decepticons - l'unico che pu aiutare Optimus Prime e i suoi Autobots a ritrovare il cubo e distruggerlo prima che finisca nelle mani dei nemici.</p>
				</br>
				<b>Link:</b></br>
				<a href="#">NowVideo</a> <br>
		
			</div>
BODY
function->loadComments();
print <<BODY;
		</div>
BODY

function->footer();
