#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;


function->header();


print<<BODY;    
    <body>
	<div id="wrapper">
		<div id="header">
			<div id="login">
				<form method="post" action="">
					<input type="text" name="user" value="User" size="12"/>
					<input type="text" name="psw" value="Password" size="12"/>
					<button type="submit" id="sending">Login</button>
				</form>
			</div>
		</div>	
		
		<div id="navigation">Ti trovi in : Home</div>
		
		<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
					<img src="../images/film.png"/><a href="#"><b>Film</b></a><hr>
					<img src="../images/comment.png"/><a href="#">Commenti</a><hr>
					</br>
				</div>
		</div>
		
		<div id="right_side">
			<div class="view">I pi&ugrave; visti</div>
				<div class="content_max_view">
					Primo</br>
					Secondo</br>
					Terzo</br>
					Quarto</br>
					Quinto</br>
				</div>
			<div class="news">Novit&agrave;</div>
				<div class="content_max_view">
					Primo</br>
					Secondo</br>
					Terzo</br>
					Quarto</br>
					Quinto</br> 
				</div>		
			<div class="news">User Online</div>
				<div class="content_max_view">100 visitatori online </div>
		</div>
		
		<div id="center_side">
			<div id="random_film">
				<h1>Transformers</h1>
				<img src="../images/transformers.jpg" class="preview"/>	
				<p>La lotta tra il bene (gli Autobots) e il male (i Decepticons), dal pianeta Cybertron si spostata sulla Terra dove milioni di anni fa caduto il Cubo di Energon, il potere supremo capace di infondere la vita ai Transformers. Sam Witwicky - nipote dell'esploratore che per primo, durante una missione nel Circolo Polare Artico sul finire del 1800, ebbe a che fare con Megatron, il capo dei Decepticons - l'unico che pu aiutare Optimus Prime e i suoi Autobots a ritrovare il cubo e distruggerlo prima che finisca nelle mani dei nemici.</p>
				</br>
				<b>Link:</b></br>
				<a href="#">NowVideo</a> <br>
		
			</div>
		</div>
BODY

function->footer();
