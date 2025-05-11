:- dynamic si/1, no/1.

inicio :-
    deshacer,
    escribir('Sistema experto de diagnóstico respiratorio.'), nl,
    escribir('Contesta las siguientes preguntas con "si." o "no."'), nl, nl,
    (   enfermedad(Enfermedad) ->
        escribir('Diagnóstico probable: '), escribir(Enfermedad), nl
    ;   escribir('No se pudo determinar la enfermedad.'), nl
    ),
    deshacer.

% Reglas para las enfermedades

enfermedad('Resfriado común') :-
    verificar('congestion_nasal'),
    verificar('estornudos'),
    verificar('dolor_de_garganta_leve'),
    verificar('tos'),
    verificar('fiebre_baja_o_ausente'),
    verificar('dolor_leve_de_cabeza'),
    verificar('ojos_llorosos').

enfermedad('Gripe (Influenza)') :-
    verificar('fiebre_alta'),
    verificar('dolor_muscular_intenso'),
    verificar('tos_seca'),
    verificar('dolor_de_cabeza'),
    verificar('fatiga_extrema'),
    verificar('escalofrios'),
    verificar('perdida_de_apetito').

enfermedad('Faringitis') :-
    verificar('dolor_de_garganta_intenso'),
    verificar('dificultad_para_tragar'),
    verificar('fiebre_alta'),
    verificar('enrojecimiento_de_faringe'),
    verificar('voz_ronca'),
    verificar('amigdalas_inflamadas').

enfermedad('Rinosinusitis (Sinusitis)') :-
    verificar('congestion_nasal'),
    verificar('dolor_o_presion_facial'),
    verificar('secrecion_nasal_espesa'),
    verificar('dolor_de_cabeza'),
    verificar('fiebre_alta'),
    verificar('tos'),
    verificar('perdida_de_olfato_o_gusto'),
    verificar('mal_aliento').

enfermedad('Bronquitis aguda') :-
    verificar('tos'),
    verificar('produccion_de_flema'),
    verificar('dolor_en_el_pecho_o_al_respirar'),
    verificar('fatiga_extrema'),
    verificar('sibilancias').

enfermedad('Asma') :-
    verificar('dificultad_para_respirar'),
    verificar('sibilancias'),
    verificar('tos'),
    verificar('sensacion_de_falta_de_aire').

enfermedad('COVID-19') :-
    verificar('fiebre_alta'),
    verificar('tos'),
    verificar('dificultad_para_respirar'),
    verificar('perdida_de_olfato_o_gusto'),
    verificar('fatiga_extrema'),
    verificar('dolor_de_garganta_intenso'),
    verificar('dolor_muscular_intenso').

enfermedad('Neumonía') :-
    verificar('fiebre_alta'),
    verificar('tos'),
    verificar('escalofrios'),
    verificar('dolor_en_el_pecho_o_al_respirar'),
    verificar('dificultad_para_respirar'),
    verificar('respiracion_rapida_o_superficial'),
    verificar('cansancio_extremo').

% Preguntas por cada sintoma

pregunta('congestion_nasal') :- escribir('¿Tiene congestión nasal?').
pregunta('estornudos') :- escribir('¿Tiene estornudos?').
pregunta('dolor_de_garganta_leve') :- escribir('¿Tiene dolor de garganta leve?').
pregunta('tos') :- escribir('¿Tiene tos?').
pregunta('fiebre_baja_o_ausente') :- escribir('¿Tiene fiebre baja o esta ausente?').
pregunta('dolor_leve_de_cabeza') :- escribir('¿Tiene dolor leve de cabeza?').
pregunta('ojos_llorosos') :- escribir('¿Tiene ojos llorosos?').
pregunta('fiebre_alta') :- escribir('¿Tiene fiebre alta (mayor a 38.5°C)?').
pregunta('dolor_muscular_intenso') :- escribir('¿Tiene dolor muscular intenso?').
pregunta('tos_seca') :- escribir('¿Tiene tos seca?').
pregunta('dolor_de_cabeza') :- escribir('¿Tiene dolor de cabeza?').
pregunta('fatiga_extrema') :- escribir('¿Tiene fatiga extrema?').
pregunta('escalofrios') :- escribir('¿Tiene escalofrios?').
pregunta('perdida_de_apetito') :- escribir('¿Ha perdido el apetito?').
pregunta('dolor_de_garganta_intenso') :- escribir('¿Tiene dolor de garganta intenso?').
pregunta('dificultad_para_tragar') :- escribir('¿Tiene dificultad para tragar?').
pregunta('enrojecimiento_de_faringe') :- escribir('¿Tiene enrojecimiento de la faringe?').
pregunta('voz_ronca') :- escribir('¿Tiene voz ronca?').
pregunta('amigdalas_inflamadas') :- escribir('¿Tiene las amigdalas inflamadas?').
pregunta('dolor_o_presion_facial') :- escribir('¿Tiene dolor o presión facial?').
pregunta('secrecion_nasal_espesa') :- escribir('¿Tiene secreción nasal espesa, amarilla o verde?').
pregunta('perdida_de_olfato_o_gusto') :- escribir('¿Ha perdido el olfato o el gusto?').
pregunta('mal_aliento') :- escribir('¿Tiene mal aliento?').
pregunta('produccion_de_flema') :- escribir('¿Produce flema?').
pregunta('dolor_en_el_pecho_o_al_respirar') :- escribir('¿Tiene dolor en el pecho o al respirar?').
pregunta('sibilancias') :- escribir('¿Tiene sibilancias?').
pregunta('sensacion_de_falta_de_aire') :- escribir('¿Tiene sensacion de falta de aire?').
pregunta('dificultad_para_respirar') :- escribir('¿Tiene dificultad para respirar?').
pregunta('respiracion_rapida_o_superficial') :- escribir('¿Tiene respiracion rápida?').
pregunta('cansancio_extremo') :- escribir('¿Tiene cansancio extremo?').

% Verificación

verificar(Sintoma) :-
    si(Sintoma), !.

verificar(Sintoma) :-
    no(Sintoma), !, fail.

verificar(Sintoma) :-
    pregunta(Sintoma),
    leer(Respuesta),
    (   Respuesta == si ->
        asserta(si(Sintoma))
    ;   asserta(no(Sintoma)), fail).

% Leer y escribir

leer(X) :- read(X).
escribir(X) :- write(X).

% Reset de datos

deshacer :- retract(si(_)), fail.
deshacer :- retract(no(_)), fail.
deshacer.
