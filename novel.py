import re
from pyformlang.fst import FST
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State , NondeterministicFiniteAutomaton , EpsilonNFA

l=list()
print(f"story1.add_final_state(q0)")
print(f"story1.add_final_state(c0)")
x =2
for i in range(1,3):
   print(f"story{x}.add_final_state(q{i})")
for i in range(1,3):
   print(f"story{x}.add_final_state(c{i})")

x =3
for i in range(3,7):
   print(f"story{x}.add_final_state(q{i})")
for i in range(3,5):
   print(f"story{x}.add_final_state(c{i})")

x =4
for i in range(7,11):
   print(f"story{x}.add_final_state(q{i})")
for i in range(5,9):
   print(f"story{x}.add_final_state(c{i})")

x =5
for i in range(11,17):
   print(f"story{x}.add_final_state(q{i})")
for i in range(9,15):
   print(f"story{x}.add_final_state(c{i})")

x =6
for i in range(17,25):
   print(f"story{x}.add_final_state(q{i})")
for i in range(15,23):
   print(f"story{x}.add_final_state(c{i})")

x =7
for i in range(25,37):
   print(f"story{x}.add_final_state(q{i})")
for i in range(23,32):
   print(f"story{x}.add_final_state(c{i})")

x =8
for i in range(37,49):
   print(f"story{x}.add_final_state(q{i})")
for i in range(32,34):
   print(f"story{x}.add_final_state(c{i})")

x =9
for i in range(49,53):
   print(f"story{x}.add_final_state(q{i})")
for i in range(34,38):
   print(f"story{x}.add_final_state(c{i})")

x =10
for i in range(38,40):
   print(f"story{x}.add_final_state(c{i})")

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

    ("q2","0","q5"),
    ("q2","1","q6"),
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

    ("q2","0","q5"),
    ("q2","1","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","0","q9"),
    ("q6","1","q10"),
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

    ("q2","0","q5"),
    ("q2","1","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","0","q9"),
    ("q6","1","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","0","q13"),
    ("q8","1","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","0","q15"),
    ("q10","1","q16"),

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

    ("q2","0","q5"),
    ("q2","1","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","0","q9"),
    ("q6","1","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","0","q13"),
    ("q8","1","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","0","q15"),
    ("q10","1","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","0","q19"),
    ("q14","1","q20"),

    ("q15","0","q21"),
    ("q15","1","q21"),

    ("q16","0","q23"),
    ("q16","1","q24"),

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

    ("q2","0","q5"),
    ("q2","1","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","0","q9"),
    ("q6","1","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","0","q13"),
    ("q8","1","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","0","q15"),
    ("q10","1","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","0","q19"),
    ("q14","1","q20"),

    ("q15","0","q21"),
    ("q15","1","q21"),

    ("q16","0","q23"),
    ("q16","1","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","0","q27"),
    ("q19","1","q28"),

    ("q20","0","q29"),
    ("q20","1","q30"),

    ("q21","0","q31"),
    ("q21","1","q32"),

    ("q22","0","q33"),
    ("q22","1","q34"),

    ("q23","0","q35"),
    ("q23","1","q36"),

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

    ("q2","0","q5"),
    ("q2","1","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","0","q9"),
    ("q6","1","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","0","q13"),
    ("q8","1","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","0","q15"),
    ("q10","1","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","0","q19"),
    ("q14","1","q20"),

    ("q15","0","q21"),
    ("q15","1","q21"),

    ("q16","0","q23"),
    ("q16","1","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","0","q27"),
    ("q19","1","q28"),

    ("q20","0","q29"),
    ("q20","1","q30"),

    ("q21","0","q31"),
    ("q21","1","q32"),

    ("q22","0","q33"),
    ("q22","1","q34"),

    ("q23","0","q35"),
    ("q23","1","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","0","e"),
    ("q26","1","e"),

    ("q27","0","q39"),
    ("q27","1","40"),

    ("q28","0","q41"),
    ("q28","1","q42"),

    ("q29","0","q43"),
    ("q29","1","q44"),

    ("q30","0","e"),
    ("q30","1","e"),

    ("q31","0","q45"),
    ("q31","1","q46"),

    ("q32","0","e"),
    ("q32","1","e"),

    ("q33","0","q47"),
    ("q33","1","q48"),

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

    ("q2","0","q5"),
    ("q2","1","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","0","q9"),
    ("q6","1","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","0","q13"),
    ("q8","1","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","0","q15"),
    ("q10","1","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","0","q19"),
    ("q14","1","q20"),

    ("q15","0","q21"),
    ("q15","1","q21"),

    ("q16","0","q23"),
    ("q16","1","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","0","q27"),
    ("q19","1","q28"),

    ("q20","0","q29"),
    ("q20","1","q30"),

    ("q21","0","q31"),
    ("q21","1","q32"),

    ("q22","0","q33"),
    ("q22","1","q34"),

    ("q23","0","q35"),
    ("q23","1","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","0","e"),
    ("q26","1","e"),

    ("q27","0","q39"),
    ("q27","1","40"),

    ("q28","0","q41"),
    ("q28","1","q42"),

    ("q29","0","q43"),
    ("q29","1","q44"),

    ("q30","0","e"),
    ("q30","1","e"),

    ("q31","0","q45"),
    ("q31","1","q46"),

    ("q32","0","e"),
    ("q32","1","e"),

    ("q33","0","q47"),
    ("q33","1","q48"),

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

    ("q44","0","q51"),
    ("q44","1","q52"),

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

    ("q2","0","q5"),
    ("q2","1","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","0","q9"),
    ("q6","1","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","0","q13"),
    ("q8","1","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","0","q15"),
    ("q10","1","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","0","q19"),
    ("q14","1","q20"),

    ("q15","0","q21"),
    ("q15","1","q21"),

    ("q16","0","q23"),
    ("q16","1","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","0","q27"),
    ("q19","1","q28"),

    ("q20","0","q29"),
    ("q20","1","q30"),

    ("q21","0","q31"),
    ("q21","1","q32"),

    ("q22","0","q33"),
    ("q22","1","q34"),

    ("q23","0","q35"),
    ("q23","1","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","0","e"),
    ("q26","1","e"),

    ("q27","0","q39"),
    ("q27","1","40"),

    ("q28","0","q41"),
    ("q28","1","q42"),

    ("q29","0","q43"),
    ("q29","1","q44"),

    ("q30","0","e"),
    ("q30","1","e"),

    ("q31","0","q45"),
    ("q31","1","q46"),

    ("q32","0","e"),
    ("q32","1","e"),

    ("q33","0","q47"),
    ("q33","1","q48"),

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

    ("q44","0","q51"),
    ("q44","1","q52"),

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

    ("q2","0","q5"),
    ("q2","1","q6"),

    ("q3","0","e"),
    ("q3","1","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","0","e"),
    ("q5","1","e"),

    ("q6","0","q9"),
    ("q6","1","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","0","q13"),
    ("q8","1","q14"),

    ("q9","0","e"),
    ("q9","1","e"),

    ("q10","0","q15"),
    ("q10","1","q16"),

    ("q11","0","e"),
    ("q11","1","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","0","e"),
    ("q13","1","e"),

    ("q14","0","q19"),
    ("q14","1","q20"),

    ("q15","0","q21"),
    ("q15","1","q21"),

    ("q16","0","q23"),
    ("q16","1","q24"),

    ("q17","0","e"),
    ("q17","1","e"),

    ("q18","0","q25"),
    ("q18","1","q26"),

    ("q19","0","q27"),
    ("q19","1","q28"),

    ("q20","0","q29"),
    ("q20","1","q30"),

    ("q21","0","q31"),
    ("q21","1","q32"),

    ("q22","0","q33"),
    ("q22","1","q34"),

    ("q23","0","q35"),
    ("q23","1","q36"),

    ("q24","0","e"),
    ("q24","1","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","0","e"),
    ("q26","1","e"),

    ("q27","0","q39"),
    ("q27","1","40"),

    ("q28","0","q41"),
    ("q28","1","q42"),

    ("q29","0","q43"),
    ("q29","1","q44"),

    ("q30","0","e"),
    ("q30","1","e"),

    ("q31","0","q45"),
    ("q31","1","q46"),

    ("q32","0","e"),
    ("q32","1","e"),

    ("q33","0","q47"),
    ("q33","1","q48"),

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

    ("q44","0","q51"),
    ("q44","1","q52"),

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
    ("c0","0","c1"),
    ("c0","1","c2"),
]

transitionsc3=[
    #Ruta Profesor-final
    ("c1","0","e"),
    #Ruta amiga
    ("c2","0","c3"),
    ("c2","1","c4"),
]
transitionsc4=[
    #Ruta presionar
    ("c3","0","c5"),
    ("c3","1","c6"),
    #Ruta Buscar Gabriel
    ("c4","0","c7"),
    ("c4","1","c8"),
]
transitionsc5=[
    #Ruta Amenazar Silencio
    ("c5","0","c9"),
    ("c5","1","c10"),
    #Ruta Cazar Gabriel
    ("c6","0","c11"),
    ("c6","1","c12"),
    #Ruta Perseguir
    ("c7","0","c13"),
    ("c7","1","c14"),
    #Ruta Policía-final
    ("c8","0","e"),
]
transitionsc6=[
    #Ruta Plan en la noche
    ("c9","0","c15"),
    ("c9","1","c16"),
    #Ruta Plan en el día-final
    ("c10","0","e"),
    #Ruta Pasar derecho
    ("c11","0","c17"),
    ("c11","1","c18"),
    #Ruta Ir callejon-final
    ("c12","0","e"),
    #Ruta Busca afuera
    ("c13","0","c19"),
    ("c13","1","c20"),
    #Ruta Buscar piso 2°
    ("c14","0","c21"),
    ("c14","1","c22"),
]
transitionsc7=[
    #Ruta Escucharle
    ("c15","0","c23"),
    ("c15","1","c24"),
    ("c15","2","c25"),
    #Ruta Acabar con él-final
    ("c16","0","e"),
    #Ruta Saltar Obstáculo-final
    ("c17","0","e"),
    #Ruta Rodear Obstáculo
    ("c18","0","c26"),
    ("c18","1","c27"),
    #Ruta Ir contra profesor 
    ("c19","0","c28"),
    ("c19","1","c29"),
    #Ruta Aceptar reunión
    ("c20","0","c30"),
    ("c20","1","c31"),
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
    ("c31","0","c32"),
    ("c31","1","c33"),
]
transitionsc9=[
    #Ruta Confrontar
    ("c32","0","34"),
    ("c32","1","35"),
    #Ruta Disimular
    ("c33","0","36"),
    ("c33","1","37"),
]
transitionsc10=[
    #Ruta Directamente-final
    ("c34","0","e"),
    #Ruta Sorpresa
    ("c35","0","c38"),
    ("c35","1","c39"),
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

story1.add_final_state(q0)
story1.add_final_state(c0)
story2.add_final_state(q1)
story2.add_final_state(q2)
story2.add_final_state(c1)
story2.add_final_state(c2)
story3.add_final_state(q3)
story3.add_final_state(q4)
story3.add_final_state(q5)
story3.add_final_state(q6)
story3.add_final_state(c3)
story3.add_final_state(c4)
story4.add_final_state(q7)
story4.add_final_state(q8)
story4.add_final_state(q9)
story4.add_final_state(q10)
story4.add_final_state(c5)
story4.add_final_state(c6)
story4.add_final_state(c7)
story4.add_final_state(c8)
story5.add_final_state(q11)
story5.add_final_state(q12)
story5.add_final_state(q13)
story5.add_final_state(q14)
story5.add_final_state(q15)
story5.add_final_state(q16)
story5.add_final_state(c9)
story5.add_final_state(c10)
story5.add_final_state(c11)
story5.add_final_state(c12)
story5.add_final_state(c13)
story5.add_final_state(c14)
story6.add_final_state(q17)
story6.add_final_state(q18)
story6.add_final_state(q19)
story6.add_final_state(q20)
story6.add_final_state(q21)
story6.add_final_state(q22)
story6.add_final_state(q23)
story6.add_final_state(q24)
story6.add_final_state(c15)
story6.add_final_state(c16)
story6.add_final_state(c17)
story6.add_final_state(c18)
story6.add_final_state(c19)
story6.add_final_state(c20)
story6.add_final_state(c21)
story6.add_final_state(c22)
story7.add_final_state(q25)
story7.add_final_state(q26)
story7.add_final_state(q27)
story7.add_final_state(q28)
story7.add_final_state(q29)
story7.add_final_state(q30)
story7.add_final_state(q31)
story7.add_final_state(q32)
story7.add_final_state(q33)
story7.add_final_state(q34)
story7.add_final_state(q35)
story7.add_final_state(q36)
story7.add_final_state(c23)
story7.add_final_state(c24)
story7.add_final_state(c25)
story7.add_final_state(c26)
story7.add_final_state(c27)
story7.add_final_state(c28)
story7.add_final_state(c29)
story7.add_final_state(c30)
story7.add_final_state(c31)
story8.add_final_state(q37)
story8.add_final_state(q38)
story8.add_final_state(q39)
story8.add_final_state(q40)
story8.add_final_state(q41)
story8.add_final_state(q42)
story8.add_final_state(q43)
story8.add_final_state(q44)
story8.add_final_state(q45)
story8.add_final_state(q46)
story8.add_final_state(q47)
story8.add_final_state(q48)
story8.add_final_state(c32)
story8.add_final_state(c33)
story9.add_final_state(q49)
story9.add_final_state(q50)
story9.add_final_state(q51)
story9.add_final_state(q52)
story9.add_final_state(c34)
story9.add_final_state(c35)
story9.add_final_state(c36)
story9.add_final_state(c37)
story10.add_final_state(c38)
story10.add_final_state(c39)

print(story11.accepts("0000"))

