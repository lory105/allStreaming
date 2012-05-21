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
			<div class="menu">Main Menu</div>
				<div class="content">
					<img src="../images/home.png"/><a href="index.cgi">Home</a><hr>
					<img src="../images/series.png"/><a href="#"><b>Serie Tv</b></a><hr>
					<img src="../images/film.png"/><a href="films.cgi">Film</a><hr>
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
