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
			<h1>Film disponibili</h1>
			<div id="year">
				<h2>Anno d'uscita</h2></br>
				<a href="film.cgi">2012</a></br>
				<a href="#">2011</a></br>
				<a href="#">2010</a></br>
				<a href="#">2009</a></br>
				<a href="#">2008</a></br>
				<a href="#">2007</a></br>
				<a href="#">2006</a></br>
				<a href="#">2005</a></br>
				<a href="#">2004</a></br>
				<a href="#">2003</a></br>
				<a href="#">2002</a></br>
				<a href="#">2001</a></br>
				<a href="#">2000</a></br>
				<a href="#">pre-2000</br>
			</div>
			<div id="genre">
				<h2>Genere</h2></br>
				<a href="film.cgi">Action</a><hr>
				<a href="#">Thriller</a><hr>
				<a href="#">Horror</a><hr>
				<a href="#">Comics</a><hr>
				<a href="#">Cartoon</a><hr>
				<a href="#">Altro</a><hr>
			</div>
		</div>

BODY

function->footer();
