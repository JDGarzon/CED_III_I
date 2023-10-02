import re
from pyformlang.fst import FST
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State , NondeterministicFiniteAutomaton , EpsilonNFA

l=list()

estado0="Estado 0"
estado1="Estado 1"
estado2="Estado 2"
estado3="Estado 3"
estado4="Estado 4"
estado5="Estado 5"
estado6="Estado 6"
estado7="Estado 7"
estado8="Estado 8"
estado9="Estado 9"
estado10="Estado 10"
estado11="Estado 11"
estado12="Estado 12"
estado13="Estado 13"
estado14="Estado 14"
estado15="Estado 15"
estado16="Estado 16"
estado17="Estado 17"
estado18="Estado 18"
estado19="Estado 19"
estado20="Estado 20"
estado21="Estado 21"
estado22="Estado 22"
estado23="Estado 23"
estado24="Estado 24"
estado25="Estado 25"
estado26="Estado 26"
estado27="Estado 27"
estado28="Estado 28"
estado29="Estado 29"
estado30="Estado 30"
estado31="Estado 31"
estado32="Estado 32"
estado33="Estado 33"
estado34="Estado 34"
estado35="Estado 35"
estado36="Estado 36"
estado37="Estado 37"
estado38="Estado 38"
estado39="Estado 39"
estado40="Estado 40"
estado41="Estado 41"
estado42="Estado 42"
estado43="Estado 43"
estado44="Estado 44"
estado45="Estado 45"
estado46="Estado 46"
estado47="Estado 47"
estado48="Estado 48"
estado49="Estado 49"
estado50="Estado 50"
estado51="Estado 51"
estado52="Estado 52"
estado53="Estado 53"
estado54="Estado 54"
estado55="Estado 55"
estado56="Estado 56"
estado57="Estado 57"
estado58="Estado 58"
estado59="Estado 59"
estado60="Estado 60"
estado61="Estado 61"
estado62="Estado 62"
estado63="Estado 63"
estado64="Estado 64"
estado65="Estado 65"
estado66="Estado 66"
estado67="Estado 67"
estado68="Estado 68"
estado69="Estado 69"
estado70="Estado 70"
estado71="Estado 71"
estado72="Estado 72"
estado73="Estado 73"
estado74="Estado 74"
estado75="Estado 75"
estado76="Estado 76"
estado77="Estado 77"
estado78="Estado 78"
estado79="Estado 79"
estado80="Estado 80"
estado81="Estado 81"
estado82="Estado 82"
estado83="Estado 83"
estado84="Estado 84"
estado85="Estado 85"
estado86="Estado 86"
estado87="Estado 87"
estado88="Estado 88"
estado89="Estado 89"
estado90="Estado 90"
estado91="Estado 91"
estado92="Estado 92"
estado93="Estado 93"
estado94="Estado 94"
estado95="Estado 95"

story1=DeterministicFiniteAutomaton()
story2=DeterministicFiniteAutomaton()
story3=DeterministicFiniteAutomaton()
story4=DeterministicFiniteAutomaton()
story5=DeterministicFiniteAutomaton()
story6=DeterministicFiniteAutomaton()
story7=DeterministicFiniteAutomaton()
story8=DeterministicFiniteAutomaton()
story9=DeterministicFiniteAutomaton()
story10=DeterministicFiniteAutomaton()
story11=DeterministicFiniteAutomaton()

l=[]
transitions1=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c0"),
    
]

transitions2=[
     #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),
]
p=[

("q","0","q"),
("q","1","q"),

]
transitions3=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),
]
transitions4=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),
]
transitions5=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

]
transitions6=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

]
transitions7=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

]
transitions8=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","0","e"),
    ("q26","1","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","0","e"),
    ("q30","1","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","0","e"),
    ("q32","1","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","0","e"),
    ("q34","1","e"),

    ("q35","0","e"),
    ("q35","1","e"),

    ("q36","0","e"),
    ("q36","1","e"),
]
transitions9=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","0","e"),
    ("q26","1","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","0","e"),
    ("q30","1","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","0","e"),
    ("q32","1","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","0","e"),
    ("q34","1","e"),

    ("q35","0","e"),
    ("q35","1","e"),

    ("q36","0","e"),
    ("q36","1","e"),

    ("q37","0","e"),
    ("q37","1","e"),

    ("q38","0","e"),
    ("q38","1","e"),

    ("q39","0","e"),
    ("q39","1","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","0","e"),
    ("q41","1","e"),
    
    ("q42","0","e"),
    ("q42","1","e"),

    ("q43","0","e"),
    ("q43","1","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","0","e"),
    ("q45","1","e"),

    ("q46","0","e"),
    ("q46","1","e"),

    ("q47","0","e"),
    ("q47","1","e"),
    
    ("q48","0","e"),
    ("q48","1","e"),
]
transitions10=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","0","e"),
    ("q26","1","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","0","e"),
    ("q30","1","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","0","e"),
    ("q32","1","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","0","e"),
    ("q34","1","e"),

    ("q35","0","e"),
    ("q35","1","e"),

    ("q36","0","e"),
    ("q36","1","e"),

    ("q37","0","e"),
    ("q37","1","e"),

    ("q38","0","e"),
    ("q38","1","e"),

    ("q39","0","e"),
    ("q39","1","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","0","e"),
    ("q41","1","e"),
    
    ("q42","0","e"),
    ("q42","1","e"),

    ("q43","0","e"),
    ("q43","1","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","0","e"),
    ("q45","1","e"),

    ("q46","0","e"),
    ("q46","1","e"),

    ("q47","0","e"),
    ("q47","1","e"),
    
    ("q48","0","e"),
    ("q48","1","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q44","0","q51"),
    ("q44","1","q52"),

    ("q49","0","e"),
    ("q49","1","e"),

    ("q50","0","e"),
    ("q50","1","e"),

    ("q51","0","e"),
    ("q51","1","e"),

    ("q52","0","e"),
    ("q52","1","e"),
]
transitions11=[
    #Inicio
    ("q","0","q0"),
    ("q","1","c1"),
    #Ruta casa
    ("q0","0","q1"),
    ("q0","1","q2"),

    ("q1","0","q3"),
    ("q1","1","q4"),

    ("q2","2","q5"),
    ("q2","3","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","2","q27"),
    ("q19","3","q28"),

    ("q20","4","q29"),
    ("q20","5","q30"),

    ("q21","6","q31"),
    ("q21","7","q32"),

    ("q22","8","q33"),
    ("q22","9","q34"),

    ("q23","a","q35"),
    ("q23","b","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","0","e"),
    ("q26","1","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","0","e"),
    ("q30","1","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","0","e"),
    ("q32","1","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","0","e"),
    ("q34","1","e"),

    ("q35","0","e"),
    ("q35","1","e"),

    ("q36","0","e"),
    ("q36","1","e"),

    ("q37","0","e"),
    ("q37","1","e"),

    ("q38","0","e"),
    ("q38","1","e"),

    ("q39","0","e"),
    ("q39","1","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","0","e"),
    ("q41","1","e"),
    
    ("q42","0","e"),
    ("q42","1","e"),

    ("q43","0","e"),
    ("q43","1","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","0","e"),
    ("q45","1","e"),

    ("q46","0","e"),
    ("q46","1","e"),

    ("q47","0","e"),
    ("q47","1","e"),
    
    ("q48","0","e"),
    ("q48","1","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q44","0","q51"),
    ("q44","1","q52"),

    ("q49","0","e"),
    ("q49","1","e"),

    ("q50","0","e"),
    ("q50","1","e"),

    ("q51","0","e"),
    ("q51","1","e"),

    ("q52","0","e"),
    ("q52","1","e"),
]

transitionsc2=[
    #Ruta colegio
    ("c0","c","c1"),
    ("c0","d","c2"),
]

transitionsc3=[
    #Ruta Profesor-final
    ("c1","0","e"),
    #Ruta amiga
    ("c2","c","c3"),
    ("c2","d","c4"),
]
transitionsc4=[
    #Ruta presionar
    ("c3","c","c5"),
    ("c3","d","c6"),
    #Ruta Buscar Gabriel
    ("c4","e","c7"),
    ("c4","f","c8"),
]
transitionsc5=[
    #Ruta Amenazar Silencio
    ("c5","c","c9"),
    ("c5","d","c10"),
    #Ruta Cazar Gabriel
    ("c6","e","c11"),
    ("c6","f","c12"),
    #Ruta Perseguir
    ("c7","g","c13"),
    ("c7","h","c14"),
    #Ruta Policía-final
    ("c8","0","e"),
]
transitionsc6=[
    #Ruta Plan en la noche
    ("c9","c","c15"),
    ("c9","d","c16"),
    #Ruta Plan en el día-final
    ("c10","0","e"),
    #Ruta Pasar derecho
    ("c11","e","c17"),
    ("c11","f","c18"),
    #Ruta Ir callejon-final
    ("c12","0","e"),
    #Ruta Busca afuera
    ("c13","g","c19"),
    ("c13","h","c20"),
    #Ruta Buscar piso 2°
    ("c14","i","c21"),
    ("c14","j","c22"),
]
transitionsc7=[
    #Ruta Escucharle
    ("c15","c","c23"),
    ("c15","d","c24"),
    ("c15","e","c25"),
    #Ruta Acabar con él-final
    ("c16","0","e"),
    #Ruta Saltar Obstáculo-final
    ("c17","0","e"),
    #Ruta Rodear Obstáculo
    ("c18","f","c26"),
    ("c18","g","c27"),
    #Ruta Ir contra profesor 
    ("c19","h","c28"),
    ("c19","i","c29"),
    #Ruta Aceptar reunión
    ("c20","j","c30"),
    ("c20","k","c31"),
    #Ruta Acercarse-final
    ("c21","0","e"),
    #Ruta Hablarle-final
    ("c22","0","e"),
]
transitionsc8=[
    #Ruta Perdonar-final
    ("c23","0","e"),
    #Ruta Huir-final
    ("c24","0","e"),
    #Ruta Acabarle-final
    ("c25","0","e"),
    #Ruta Forcejear-final
    ("c26","0","e"),
    #Ruta Redimir-final
    ("c27","0","e"),
    #Ruta Acabar con Gabriel-final
    ("c28","0","e"),
    #Ruta Rendirse-final
    ("c29","0","e"),
    #Ruta Sobornado-final
    ("c30","0","e"),
    #Ruta No aceptar
    ("c31","c","c32"),
    ("c31","d","c33"),
]
transitionsc9=[
    #Ruta Confrontar
    ("c32","c","34"),
    ("c32","d","35"),
    #Ruta Disimular
    ("c33","e","36"),
    ("c33","f","37"),
]
transitionsc10=[
    #Ruta Directamente-final
    ("c34","0","e"),
    #Ruta Sorpresa
    ("c35","c","c38"),
    ("c35","d","c39"),
    #Ruta Incendio-final
    ("c36","0","e"),
    #Ruta Policía-final
    ("c37","0","e"),
]
transitionsc11=[
    #Ruta Venganza-final
    ("c38","0","e"),
    #Ruta Policía-final
    ("c39","0","e"),
]


story1.add_transitions(transitions1)
story1.add_start_state("q")
story1.add_final_state("e")
story2.add_transitions(transitions2)
story2.add_transitions(transitionsc2)
story2.add_start_state("q")
story2.add_final_state("e")
story3.add_transitions(transitions3)
story3.add_transitions(transitionsc2)
story3.add_transitions(transitionsc3)
story3.add_start_state("q")
story3.add_final_state("e")
story4.add_transitions(transitions4)
story4.add_transitions(transitionsc2)
story4.add_transitions(transitionsc3)
story4.add_transitions(transitionsc4)
story4.add_start_state("q")
story4.add_final_state("e")
story5.add_transitions(transitions5)
story5.add_transitions(transitionsc2)
story5.add_transitions(transitionsc3)
story5.add_transitions(transitionsc4)
story5.add_transitions(transitionsc5)
story5.add_start_state("q")
story5.add_final_state("e")
story6.add_transitions(transitions6)
story6.add_transitions(transitionsc2)
story6.add_transitions(transitionsc3)
story6.add_transitions(transitionsc4)
story6.add_transitions(transitionsc5)
story6.add_transitions(transitionsc6)
story6.add_start_state("q")
story6.add_final_state("e")
story7.add_transitions(transitions7)
story7.add_transitions(transitionsc2)
story7.add_transitions(transitionsc3)
story7.add_transitions(transitionsc4)
story7.add_transitions(transitionsc5)
story7.add_transitions(transitionsc6)
story7.add_transitions(transitionsc7)
story7.add_start_state("q")
story7.add_final_state("e")
story8.add_transitions(transitions8)
story8.add_transitions(transitionsc2)
story8.add_transitions(transitionsc3)
story8.add_transitions(transitionsc4)
story8.add_transitions(transitionsc5)
story8.add_transitions(transitionsc6)
story8.add_transitions(transitionsc7)
story8.add_transitions(transitionsc8)
story8.add_start_state("q")
story8.add_final_state("e")
story9.add_transitions(transitions9)
story9.add_transitions(transitionsc2)
story9.add_transitions(transitionsc3)
story9.add_transitions(transitionsc4)
story9.add_transitions(transitionsc5)
story9.add_transitions(transitionsc6)
story9.add_transitions(transitionsc7)
story9.add_transitions(transitionsc8)
story9.add_transitions(transitionsc9)
story9.add_start_state("q")
story9.add_final_state("e")
story10.add_transitions(transitions10)
story10.add_transitions(transitionsc2)
story10.add_transitions(transitionsc3)
story10.add_transitions(transitionsc4)
story10.add_transitions(transitionsc5)
story10.add_transitions(transitionsc6)
story10.add_transitions(transitionsc7)
story10.add_transitions(transitionsc8)
story10.add_transitions(transitionsc9)
story10.add_transitions(transitionsc10)
story10.add_start_state("q")
story10.add_final_state("e")
story11.add_transitions(transitions11)
story11.add_transitions(transitionsc2)
story11.add_transitions(transitionsc3)
story11.add_transitions(transitionsc4)
story11.add_transitions(transitionsc5)
story11.add_transitions(transitionsc6)
story11.add_transitions(transitionsc7)
story11.add_transitions(transitionsc8)
story11.add_transitions(transitionsc9)
story11.add_transitions(transitionsc10)
story11.add_transitions(transitionsc11)
story11.add_start_state("q")
story11.add_final_state("e")

story1.add_final_state("q0")
story1.add_final_state("c0")
story2.add_final_state("q1")
story2.add_final_state("q2")
story2.add_final_state("c1")
story2.add_final_state("c2")
story3.add_final_state("q3")
story3.add_final_state("q4")
story3.add_final_state("q5")
story3.add_final_state("q6")
story3.add_final_state("c3")
story3.add_final_state("c4")
story4.add_final_state("q7")
story4.add_final_state("q8")
story4.add_final_state("q9")
story4.add_final_state("q10")
story4.add_final_state("c5")
story4.add_final_state("c6")
story4.add_final_state("c7")
story4.add_final_state("c8")
story5.add_final_state("q11")
story5.add_final_state("q12")
story5.add_final_state("q13")
story5.add_final_state("q14")
story5.add_final_state("q15")
story5.add_final_state("q16")
story5.add_final_state("c9")
story5.add_final_state("c10")
story5.add_final_state("c11")
story5.add_final_state("c12")
story5.add_final_state("c13")
story5.add_final_state("c14")
story6.add_final_state("q17")
story6.add_final_state("q18")
story6.add_final_state("q19")
story6.add_final_state("q20")
story6.add_final_state("q21")
story6.add_final_state("q22")
story6.add_final_state("q23")
story6.add_final_state("q24")
story6.add_final_state("c15")
story6.add_final_state("c16")
story6.add_final_state("c17")
story6.add_final_state("c18")
story6.add_final_state("c19")
story6.add_final_state("c20")
story6.add_final_state("c21")
story6.add_final_state("c22")
story7.add_final_state("q25")
story7.add_final_state("q26")
story7.add_final_state("q27")
story7.add_final_state("q28")
story7.add_final_state("q29")
story7.add_final_state("q30")
story7.add_final_state("q31")
story7.add_final_state("q32")
story7.add_final_state("q33")
story7.add_final_state("q34")
story7.add_final_state("q35")
story7.add_final_state("q36")
story7.add_final_state("c23")
story7.add_final_state("c24")
story7.add_final_state("c25")
story7.add_final_state("c26")
story7.add_final_state("c27")
story7.add_final_state("c28")
story7.add_final_state("c29")
story7.add_final_state("c30")
story7.add_final_state("c31")
story8.add_final_state("q37")
story8.add_final_state("q38")
story8.add_final_state("q39")
story8.add_final_state("q40")
story8.add_final_state("q41")
story8.add_final_state("q42")
story8.add_final_state("q43")
story8.add_final_state("q44")
story8.add_final_state("q45")
story8.add_final_state("q46")
story8.add_final_state("q47")
story8.add_final_state("q48")
story8.add_final_state("c32")
story8.add_final_state("c33")
story9.add_final_state("q49")
story9.add_final_state("q50")
story9.add_final_state("q51")
story9.add_final_state("q52")
story9.add_final_state("c34")
story9.add_final_state("c35")
story9.add_final_state("c36")
story9.add_final_state("c37")
story10.add_final_state("c38")
story10.add_final_state("c39")


print(story11.accepts("0000"))
   
def dialogos(transitionLevel, string):
    value = string[-1]
    response = ""
    match transitionLevel:
        case 1:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
        case 2:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
        case 3:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
        case 4:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
        case 5:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case '4':
                    response = ""
                case '5':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
                case 'g':
                    response = ""
                case 'h':
                    response = ""
        case 6:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case '4':
                    response = ""
                case '5':
                    response = ""
                case '6':
                    response = ""
                case '7':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
                case 'g':
                    response = ""
                case 'h':
                    response = ""
                case 'i':
                    response = ""
                case 'j':
                    response = ""
        case 7:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case '4':
                    response = ""
                case '5':
                    response = ""
                case '6':
                    response = ""
                case '7':
                    response = ""
                case '8':
                    response = ""
                case '9':
                    response = ""
                case 'a':
                    response = ""
                case 'b':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
                case 'g':
                    response = ""
                case 'h':
                    response = ""
                case 'i':
                    response = ""
                case 'j':
                    response = ""
                case 'k':
                    response = ""
        case 8:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case '4':
                    response = ""
                case '5':
                    response = ""
                case '6':
                    response = ""
                case '7':
                    response = ""
                case '8':
                    response = ""
                case '9':
                    response = ""
                case 'a':
                    response = ""
                case 'b':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
        case 9:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case '2':
                    response = ""
                case '3':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
                case 'e':
                    response = ""
                case 'f':
                    response = ""
        case 10:
            match value:
                case '0':
                    response = ""
                case '1':
                    response = ""
                case 'c':
                    response = ""
                case 'd':
                    response = ""
        case 11:
            match value:
                case '0':
                    response = "Texto de ejemplo - Vuelve a jugar"
                case '1':
                    response = "Texto de ejemplo - Dejar de jugar"
    return response


