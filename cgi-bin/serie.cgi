#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;


function->header();
function->left("serie");
function->right();
       
print<<BODY;
		<div id="center_side">
			<div id="random_film">
				<h1>The Mentalist</h1>
				<img src="../images/mentalist.jpg" class="preview"/>	
				<p>Patrick Jane "consulente" al California Bureau of Investigation, dove aiuta la squadra investigativa coordinata da Teresa Lisbon e formata da Kimball Cho, Wayne Rigsby e Grace Van Pelt usando il suo particolare talento di Mentalist. La sua dote gli permette di notare ogni piccolo dettaglio, ogni sfuggevole particolare all?apparenza inutile, che per Patrick diventa un prezioso tassello del puzzle che lo porter a risolvere caso dopo caso...</p>
				</br>
				<b>Prima serie:</b></br>
				<a href="#">Prima puntata</a> <br>
				<a href="#">Seconda puntata</a> <br>
				<a href="#">Terza puntata</a> <br>
				<a href="#">Quarta puntata</a> <br>
				<a href="#">Quinta puntata</a> <br>
				<a href="#">Sesta puntata</a> <br>
				<a href="#">Settima puntata</a> <br>
				<a href="#">Ottava puntata</a> <br>
				<a href="#">Nona puntata</a> <br>
				<a href="#">Decima puntata</a> <br>
			</div>
		</div>
BODY

function->footer();
