juego(galaga_palomas,accion, 'galaga','../static/img/galaga-palomas.PNG','juego al estilo del clasico Galaga, en el cual nuestro personaje tiene que evitar ser cagado por palomas...').

juego(galaga_palomas,disparos, 'galaga','../static/img/galaga-palomas.PNG','juego al estilo del clasico Galaga, en el cual nuestro personaje tiene que evitar ser cagado por palomas...').

juego(covid_runner, plataformas, 'covid_runner','../static/img/covid-runner.PNG','Corre y salta para evitar un contagio del coronavirus...').

juego(saltarin, plataformas, 'saltarin','../static/img/saltarin.PNG','juego al estilo de flappy-bird, en el cual nuestro personaje principal es mario \ny este tiene que evitar chocarse con los gigantes misiles!').

juego(saltarin, deporte, 'saltarin','../static/img/saltarin.PNG','juego al estilo de flappy-bird, en el cual nuestro personaje principal es mario \ny este tiene que evitar chocarse con los gigantes misiles!').

juego(busca_flores,puzzle,'busca_flores','../static/img/busca-flores.PNG','juego inspirado en el conocido buscaminas, pero tenemos que evitar tocar las flores').

juego(caza_calaveras,accion,'caza','../static/img/caza-calaveras.PNG','juego en el cual nuestro personaje principal tiene que perseguir y cazar todas las calaberas que pueda!').

juego(caza_calaveras,aventura,'caza','../static/img/caza-calaveras.PNG','juego en el cual nuestro personaje principal tiene que perseguir y cazar todas las calaberas que pueda!').

juego(2048,puzzle,'j_2048','../static/img/2048.PNG','Juego que reta nuestra habilidad para mantener las casillas vacias sumando numeros iguales').


usuario(jordy,jordy).
usuario(nasa,nasa).


juegoUsu(jordy,galaga_palomas).
juegoUsu(jordy,covid_runner).


juegoUsu(nasa,saltarin).
juegoUsu(nasa,saltarin).
juegoUsu(nasa,galaga_palomas).
juegoUsu(nasa,saltarin).
juegoUsu(nasa,saltarin).
juegoUsu(nasa,covid_runner).


member(X,[X|_]).
member(X,[_|T]):- member(X,T).

set([],[]).
set([H|T],[H|Out]):- not(member(H,T)), set(T,Out).
set([H|T],Out):-member(H,T), set(T,Out).


veces(U,J,N):-findall(J,juegoUsu(U,J),F),length(F,N).

sug(U,F):-findall((J,N),(juego(J,_,_,_,_), veces(U,J,N)), L), set(L,F).
