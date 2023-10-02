import re
from pyformlang.fst import FST
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State , NondeterministicFiniteAutomaton , EpsilonNFA

l=list()
for i in range(1,12):
   print(f"story{i}.add_transitions(transitions{i})")
   print(f"story{i}.add_start_state(\"q\")")
   print(f"story{i}.add_final_state(\"e\")")

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
    ("q","1","c1"),
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


story1.add_transitions(transitions1)
story1.add_start_state("q")
story1.add_final_state("e")
story2.add_transitions(transitions2)
story2.add_start_state("q")
story2.add_final_state("e")
story3.add_transitions(transitions3)
story3.add_start_state("q")
story3.add_final_state("e")
story4.add_transitions(transitions4)
story4.add_start_state("q")
story4.add_final_state("e")
story5.add_transitions(transitions5)
story5.add_start_state("q")
story5.add_final_state("e")
story6.add_transitions(transitions6)
story6.add_start_state("q")
story6.add_final_state("e")
story7.add_transitions(transitions7)
story7.add_start_state("q")
story7.add_final_state("e")
story8.add_transitions(transitions8)
story8.add_start_state("q")
story8.add_final_state("e")
story9.add_transitions(transitions9)
story9.add_start_state("q")
story9.add_final_state("e")
story10.add_transitions(transitions10)
story10.add_start_state("q")
story10.add_final_state("e")
story11.add_transitions(transitions11)
story11.add_start_state("q")
story11.add_final_state("e")

print(story11.accepts("0000"))

