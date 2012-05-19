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
					<input type="password" name="psw" value="Password" size="12"/>
					<button type="submit" id="sending">Login</button>
				</form>
			</div>
		</div>	
		
		<div id="navigation">Ti trovi in : Home</div>
		
		<div id="left_side">
			<div class="menu">Menu Principale</div>
				<div class="content">
					<img src="../images/home.png"/><a href="#"><b>Home</b></a><hr>
					<img src="../images/series.png"/><a href="series.cgi">Serie Tv</a><hr>
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
			<h1>Film Consigliati</h1>
				<div id="random_film">
						<div class="film">
							<img src="../images/sin-city.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Sin City</a>
						</div>
						<div class="film">
							<img src="../images/shining.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Shining</a>
						</div>

						<div class="film">
							<img src="../images/harry.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Harry Potter</a>
						</div>
						<div class="film">
							<img src="../images/want.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:I want you</a>
						</div>
				</div>
		</div>

BODY

function->footer();
