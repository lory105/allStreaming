#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;


function->header();
       
print <<BODY;
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
			<h1>Serie Tv disponibili</h1>
				<a href="serie.cgi">Prima serie</a> <hr>
				<a href="serie.cgi">Seconda serie</a> <hr>
				<a href="serie.cgi">Terza serie</a> <hr>
				<a href="serie.cgi">Quarta serie</a> <hr>
				<a href="serie.cgi">Quinta serie</a> <hr>
				<a href="serie.cgi">Sesta serie</a> <hr>
				<a href="serie.cgi">Settima serie</a> <hr>
				<a href="serie.cgi">Ottava serie</a> <hr>
				<a href="serie.cgi">Nona serie</a> <hr>
				<a href="serie.cgi">Decima serie</a> <hr>
		</div>

BODY

function->footer();
