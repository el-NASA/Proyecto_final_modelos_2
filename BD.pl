juego(galaga_palomas,accion, 'https://bit.ly/2UaX8no','../static/img/galaga-palomas.png','juego al estilo del clasico Galaga, en el cual nuestro personaje tiene que evitar ser cagado por palomas...').

juego(galaga_palomas,disparos, 'https://bit.ly/2UaX8no','../static/img/galaga-palomas.png','juego al estilo del clasico Galaga, en el cual nuestro personaje tiene que evitar ser cagado por palomas...').

juego(covid_runner, plataformas, 'https://bit.ly/2UcROzN','../static/img/covid-runner.png','Corre y salta para evitar un contagio del coronavirus...').

juego(saltarin, plataformas, 'https://bit.ly/2J5QNDo','../static/img/saltarin.png','juego al estilo de flappy-bird, en el cual nuestro personaje principal es mario \ny este tiene que evitar chocarse con los gigantes misiles!').

juego(saltarin, deporte, 'https://bit.ly/2J5QNDo','../static/img/saltarin.png','juego al estilo de flappy-bird, en el cual nuestro personaje principal es mario \ny este tiene que evitar chocarse con los gigantes misiles!').

juego(busca_flores,puzzle,'https://bit.ly/2WCChuJ','../static/img/busca-flores.png','juego inspirado en el conocido buscaminas, pero tenemos que evitar tocar las flores').

juego(caza_calaveras,accion,'https://bit.ly/2Ue2Zbu','../static/img/caza-calaveras.png','juego en el cual nuestro personaje principal tiene que perseguir y cazar todas las calaberas que pueda!').

juego(caza_calaveras,aventura,'https://bit.ly/2Ue2Zbu','../static/img/caza-calaveras.png','juego en el cual nuestro personaje principal tiene que perseguir y cazar todas las calaberas que pueda!').


usuario(jordy,jordy).
usuario(nasa,nasa).

juegoUsu(jordy,saltarin).
juegoUsu(jordy,galaga_palomas).
juegoUsu(jordy,covid_runner).
juegoUsu(jordy,saltarin).

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

