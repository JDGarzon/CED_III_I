import re
from pyformlang.fst import FST
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State , NondeterministicFiniteAutomaton , EpsilonNFA
from pyformlang.cfg import CFG

sequence = ""

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

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

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

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

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

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

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

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

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

    ("q24","z","e"),
    ("q24","z","e"),

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

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

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

    ("q24","z","e"),
    ("q24","z","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","z","e"),
    ("q26","z","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","z","e"),
    ("q30","z","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","z","e"),
    ("q32","z","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","z","e"),
    ("q34","z","e"),

    ("q35","z","e"),
    ("q35","z","e"),

    ("q36","z","e"),
    ("q36","z","e"),
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

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

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

    ("q24","z","e"),
    ("q24","z","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","z","e"),
    ("q26","z","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","z","e"),
    ("q30","z","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","z","e"),
    ("q32","z","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","z","e"),
    ("q34","z","e"),

    ("q35","z","e"),
    ("q35","z","e"),

    ("q36","z","e"),
    ("q36","z","e"),

    ("q37","z","e"),
    ("q37","z","e"),

    ("q38","z","e"),
    ("q38","z","e"),

    ("q39","z","e"),
    ("q39","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","z","e"),
    ("q41","z","e"),
    
    ("q42","z","e"),
    ("q42","z","e"),

    ("q43","z","e"),
    ("q43","z","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","z","e"),
    ("q45","z","e"),

    ("q46","z","e"),
    ("q46","z","e"),

    ("q47","z","e"),
    ("q47","z","e"),
    
    ("q48","z","e"),
    ("q48","z","e"),
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

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

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

    ("q24","z","e"),
    ("q24","z","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","z","e"),
    ("q26","z","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","z","e"),
    ("q30","z","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","z","e"),
    ("q32","z","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","z","e"),
    ("q34","z","e"),

    ("q35","z","e"),
    ("q35","z","e"),

    ("q36","z","e"),
    ("q36","z","e"),

    ("q37","z","e"),
    ("q37","z","e"),

    ("q38","z","e"),
    ("q38","z","e"),

    ("q39","z","e"),
    ("q39","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","z","e"),
    ("q41","z","e"),
    
    ("q42","z","e"),
    ("q42","z","e"),

    ("q43","z","e"),
    ("q43","z","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","z","e"),
    ("q45","z","e"),

    ("q46","z","e"),
    ("q46","z","e"),

    ("q47","z","e"),
    ("q47","z","e"),
    
    ("q48","z","e"),
    ("q48","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q44","0","q51"),
    ("q44","1","q52"),

    ("q49","z","e"),
    ("q49","z","e"),

    ("q50","z","e"),
    ("q50","z","e"),

    ("q51","z","e"),
    ("q51","z","e"),

    ("q52","z","e"),
    ("q52","z","e"),
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

    ("q3","z","e"),
    ("q3","z","e"),

    ("q4","0","q7"),
    ("q4","1","q8"),

    ("q5","z","e"),
    ("q5","z","e"),

    ("q6","2","q9"),
    ("q6","3","q10"),

    ("q7","0","q11"),
    ("q7","1","q12"),

    ("q8","2","q13"),
    ("q8","3","q14"),

    ("q9","z","e"),
    ("q9","z","e"),

    ("q10","4","q15"),
    ("q10","5","q16"),

    ("q11","z","e"),
    ("q11","z","e"),

    ("q12","0","17"),
    ("q12","1","q18"),

    ("q13","z","e"),
    ("q13","z","e"),

    ("q14","2","q19"),
    ("q14","3","q20"),

    ("q15","4","q21"),
    ("q15","5","q21"),

    ("q16","6","q23"),
    ("q16","7","q24"),

    ("q17","z","e"),
    ("q17","z","e"),

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

    ("q24","z","e"),
    ("q24","z","e"),

    ("q25","0","q37"),
    ("q25","1","q38"),

    ("q26","z","e"),
    ("q26","z","e"),

    ("q27","2","q39"),
    ("q27","3","40"),

    ("q28","4","q41"),
    ("q28","5","q42"),

    ("q29","6","q43"),
    ("q29","7","q44"),

    ("q30","z","e"),
    ("q30","z","e"),

    ("q31","8","q45"),
    ("q31","9","q46"),

    ("q32","z","e"),
    ("q32","z","e"),

    ("q33","a","q47"),
    ("q33","b","q48"),

    ("q34","z","e"),
    ("q34","z","e"),

    ("q35","z","e"),
    ("q35","z","e"),

    ("q36","z","e"),
    ("q36","z","e"),

    ("q37","z","e"),
    ("q37","z","e"),

    ("q38","z","e"),
    ("q38","z","e"),

    ("q39","z","e"),
    ("q39","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q41","z","e"),
    ("q41","z","e"),
    
    ("q42","z","e"),
    ("q42","z","e"),

    ("q43","z","e"),
    ("q43","z","e"),

    ("q44","2","q51"),
    ("q44","3","q52"),

    ("q45","z","e"),
    ("q45","z","e"),

    ("q46","z","e"),
    ("q46","z","e"),

    ("q47","z","e"),
    ("q47","z","e"),
    
    ("q48","z","e"),
    ("q48","z","e"),

    ("q40","0","q49"),
    ("q40","1","q50"),

    ("q44","0","q51"),
    ("q44","1","q52"),

    ("q49","z","e"),
    ("q49","z","e"),

    ("q50","z","e"),
    ("q50","z","e"),

    ("q51","z","e"),
    ("q51","z","e"),

    ("q52","z","e"),
    ("q52","z","e"),
]

transitionsc2=[
    #Ruta colegio
    ("c0","c","c1"),
    ("c0","d","c2"),
]

transitionsc3=[
    #Ruta Profesor-final
    ("c1","z","e"),
    #Ruta amiga
    ("c2","c","c3"),
    ("c2","d","c4"),
]
transitionsc4=[
    #Ruta presionar
    ("c3","c","c5"),
    ("c3","d","c6"),
    #Ruta Buscar #$%
    ("c4","e","c7"),
    ("c4","f","c8"),
]
transitionsc5=[
    #Ruta Amenazar Silencio
    ("c5","c","c9"),
    ("c5","d","c10"),
    #Ruta Cazar #$%
    ("c6","e","c11"),
    ("c6","f","c12"),
    #Ruta Perseguir
    ("c7","g","c13"),
    ("c7","h","c14"),
    #Ruta Policía-final
    ("c8","z","e"),
]
transitionsc6=[
    #Ruta Plan en la noche
    ("c9","c","c15"),
    ("c9","d","c16"),
    #Ruta Plan en el día-final
    ("c10","z","e"),
    #Ruta Pasar derecho
    ("c11","e","c17"),
    ("c11","f","c18"),
    #Ruta Ir callejon-final
    ("c12","z","e"),
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
    #Ruta Acabar con él-final
    ("c16","z","e"),
    #Ruta Saltar Obstáculo-final
    ("c17","z","e"),
    #Ruta Rodear Obstáculo
    ("c18","e","c25"),
    ("c18","f","c26"),
    #Ruta Ir contra profesor 
    ("c19","g","c27"),
    ("c19","h","c28"),
    #Ruta Aceptar reunión
    ("c20","i","c29"),
    ("c20","j","c30"),
    #Ruta Acercarse-final
    ("c21","z","e"),
    #Ruta Hablarle-final
    ("c22","z","e"),
]
transitionsc8=[
    #Ruta Escucharle-final
    ("c23","z","e"),
    #Ruta Acabarle-final
    ("c24","z","e"),
    #Ruta Forcejear-final
    ("c25","z","e"),
    #Ruta Redimir-final
    ("c26","z","e"),
    #Ruta Acabar con #$%-final
    ("c27","z","e"),
    #Ruta Rendirse-final
    ("c28","z","e"),
    #Ruta Sobornado-final
    ("c29","z","e"),
    #Ruta Sobornado-final
    ("c30","c","31"),
    ("c30","d","32"),
]
transitionsc9=[
    #Ruta Confrontar
    ("c31","c","33"),
    ("c31","d","34"),
    #Ruta Disimular
    ("c32","e","35"),
    ("c32","f","36"),
]
transitionsc10=[
    #Ruta Directamente-final
    ("c33","z","e"),
    #Ruta Sorpresa
    ("c34","c","c37"),
    ("c34","d","c38"),
    #Ruta Incendio-final
    ("c35","z","e"),
    #Ruta Policía-final
    ("c36","z","e"),
]
transitionsc11=[
    #Ruta Venganza-final
    ("c37","z","e"),
    #Ruta Policía-final
    ("c38","z","e"),
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

#Reemplaza los nombres y mantiene todo lo demas igual

from pyformlang.cfg import CFG

def dialogos(transitionLevel, string):
    value = string[-1]
    response = ""
    match transitionLevel:
        case 0:
            response = "Tu hija ha muerto. No hay nada más en tu cabeza en este momento. Ahogado en alcohol, no te importa ni tu trabajo, ni tu esposa, ni tu vida. Solo quieres una cosa, saber la respuesta. "
            response+="Te culpas por no haber estado más pendiente antes, por no haber indagado en su cambio drástico de actitud, ni en su completa falta de interés en ir al colegio, a pesar de que estaba a punto de graduarse. Todo por asumir que era algo típico de su adolescencia. "
            response+=" Su suicidio aún no está plenamente investigado, sin embargo, no tienes paciencia para esperar a la policía, quieres respuestas, y las buscarás por tu cuenta "
            response+="\n( Necesitas información, divagando en dónde puedes encontrarla, a tu mente viene ir a la habitación de tu hija o ir a su colegio ¿qué decides hacer? )"
            response+="\n¿Que quieres hacer?: "
            response+="\nA. Ir a la habitación"
            response+="\nB. Ir al colegio"

        case 1:
            match value:
                case '0':
                    #Ir a la habitación de tu hija: 0
                    response = "Decides dirigirte a la habitación de tu hija, el lugar donde pasaba la mayoría de su tiempo."
                    response +="Mientras subes las escaleras hacia su habitación, cada paso te parece una eternidad. Abres la puerta con cuidado y te enfrentas a su mundo, que ahora parece congelado en el tiempo. Las paredes están adornadas con posters de sus bandas favoritas y fotos de recuerdos con sus amigos. "
                    response +="Su cama está sin hacer, y su escritorio está lleno de libros y notas de clase. La computadora está apagada. Todo parece bastante desordenado. "
                    response +="\n(Piensas en qué podrías hacer para obtener algo de información, puedes ordenar la habitación, o revisar la computadora)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Ordenar la habitacion"
                    response+="\nB. Revisar computadora"
                case '1':
                    #Ir al colegio de tu hija: 1
                    response = "Optas por ir a investigar al colegio de tu hija. Manejas hasta el colegio y un vez en la entrada puedes ver a algunos estudiantes y profesores, todo sigue su curso habitual, sientes que no es justo, pero te tragas la indignación para después. "
                    response +="Sabes que debes hablar con alguien que conozca a tu hija y pueda ofrecerte información útil sobre lo que pasó. Caminas hacia su salón, justo a tiempo para que las clases terminen. "
                    response +="Reconoces a su profesor y a Valentina, su mejor amiga. Recuerdas cuando se quedaba a dormir con tu hija, era un escándalo, uno que no puedes parar de extrañar. Deberías hablar con alguno de los dos antes de que se marchen)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Hablar con el profesor"
                    response+="\nB. Hablar con su mejor amiga"
        case 2:
            match value:
                case '0':
                    #Ordenar la habitación: 00
                    response = "Aunque el llanto brote de ti con solo respirar en esa habitación, decides poner las cosas en su sitio. En el proceso notas un cuaderno muy extraño, estaba envuelto en fomi y está cerrado con un candado. Sospechas que se trata de su diario. Lo dejas a un lado mientras terminas de ordenar la habitación, ahora con el objetivo de encontrar la llave.  Cuando estabas a punto de darte por vencido, se te ocurre revisar debajo del colchón, y eureka, encuentras una pequeña llave que seguramente encajará. "
                    response +="\n(Pero cuando tienes su diario justo al frente de ti, otra duda te asalta, deberías ver el diario y hurgar en los pensamientos más íntimos de tu hija por una respuesta, o quizá sea lo mejor rendirte, y dejarle el trabajo a la policía.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. No ver el diario"
                    response+="\nB. Ver el diario"
                case '1':
                    #Revisar la computadora: 01
                    response = "Decides ignorar el desorden de la habitación y vas directo al computador. Una vez lo enciendes, te das cuenta de que no pide contraseña para entrar, así que cuando inicias sesión. Dentro del escritorio no hay íconos, solo está la papelera de reciclaje y un video titulado “Avanza”. Una vez lo ves, no puedes parar de llorar. El video consistía en tu hija despidiéndose de ustedes, sus padres, recordando los momentos felices y rogando que sigan sus vidas sin importar que ella ya no esté. Te dijo que cuides a mamá, que adoptes un gato para ella, ya que, aunque siempre había querido uno, nunca lo tuvo porque su hija era alérgica. Te pide que no la abandones, te pide que no busques culpables, te pide que Avances. "
                    response +="\n(Con tus lágrimas cubriendo toda tu cara, y un nudo en la garganta que te hace sentir como si se fuera a partir en dos, no sabes qué hacer. ¿Le haces caso a tu hija e intentas seguir a delante, o investigas más para encontrar la causa de que ella se fuera?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Hacer caso a tu hija"
                    response+="\nB. Investigar más"
                case 'c':
                    #Hablar con el profesor: 0c
                    response = "Hablas con el profesor director de su clase. Sorprendido de verte allí, te dice que no tiene idea de por qué tu hija terminó de esa manera, que él la notaba normal hasta antes del suceso, y que mejor dejes que la policía haga su trabajo. Intentas hablar más con él, pero te dice que está muy ocupado, y te advierte de que si no dejas de “perturbar el ambiente estudiantil” llamará a la policía. Decepcionado y confundido, regresas a tu rutina de destrucción personal, abandonándolo todo, sin saber la verdad, y sin que se haga justicia, ya que la policía nunca encontró nada."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case 'd':
                    #Hablar con Valentina: 0d
                    response = "Decides preguntarle a Valentina sobre lo que le pasó a tu hija. Al principio no te quiere responder nada, te evita y sigue su camino. Sin embargo, cuando le preguntas la razón voltea y, nerviosa, te dice en voz baja, y de una manera preocupada “Todo es culpa de #$%”. Después de eso, sale corriendo. "
                    response +="\n(Estás muy confundido, habías escuchado hablar de #$% antes, sabes quién es, sabes dónde encontrarlo, pero no sabes lo que hizo. Valentina aún no está muy lejos, puedes presionarla para que te cuente los detalles de lo sucedido, o buscar a #$%, y que te los diga él mismo.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Presionar a Valentina"
                    response+="\nB. Buscar a #$%"
        case 3:
            match value:
                case '0':
                    #No ver el diario: 000
                    response = "Mientras te debatías entre ver o no el diario, llega tu esposa y te confronta. Al verte tan alterado decide directamente quitarte el diario de las manos, causando una pelea. A raíz de todo eso tu vida solo siguió empeorando. Te separaste, y en tu soledad, solo podías seguir pensando la falta que tu hija le hacía a tu vida. Al final, tuviste el mismo destino que ella, todo porque estabas lleno de culpa por no haber hecho lo suficiente."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"                    
                case '1':
                    #Ver el diario: 001
                    response = "Con cuidado, abres el diario y comienzas a leer sus pensamientos más íntimos. No lo piensas dos veces y decides leer las últimas páginas, buscando alguna razón. "
                    response +="Para tu sorpresa, todas las páginas están llenas de rayones, que cubren bruscamente el texto que alguna vez fue escrito con ilusión y alegría. Los rayones están hechos con fuerza, tanto así que algunas hojas directamente fueron hechas pedazos. "
                    response +="Entre todo el caos, logras distinguir lo siguiente: "
                    response +="“ … #$% es muy genial, ayer me invitó a … Estoy muy emocionada por ir al concierto de los … ESTO NO PUEDE ESTAR PASANDO … ya no sé qué hacer, estoy sola, ni siquiera Valen … Lo siento. “  "
                    response += "\n(Lo único que sabes es que ese tal #$% tiene algo que ver con lo que pasó. Furioso, te dispones a ir a buscarlo, a interrogarlo, lo que sea por saber más de lo que pasó. Sin embargo, tu esposa, que te estaba observando todo este tiempo te detiene, quiere hablar contigo, saber qué piensas, saber cómo estás, ¿la escuchas o te marchas?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Hablar con tu esposa"
                    response+="\nB. No hablar con tu esposa"
                case '2':
                    #Le haces caso a la grabación de tu hija : 012
                    response = "Decides ignorar todos tus delirios de saber la verdad por tu cuenta, de encontrar un culpable y hacerlo pagar, ese es el trabajo de la policía. Aunque te duela demasiado, hacerle caso a tu hija es lo mejor, tu esposa también está sufriendo, tienen que abordar el tema juntos. Así que decides avanzar junto a ella, todo mejorará."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case '3':
                    #Investigar más: 013
                    response = "Le pides perdón a tu hija por no respetar sus últimos deseos, pero no puedes rendirte tan fácil. Sigues investigando su computador, y descubres que no cerró sesión en una de sus redes sociales, así que comienzas a buscar entre las conversaciones. No habían muchos mensajes,  al parecer es una de esas redes sociales donde solo se comparten videos. Pero el chat más reciente llama enormemente tu atención. Era tu hija, rogándole a un tal #$% atención, que dejase de ignorarla, que necesitaba ayuda, que se haga responsable, que lo perdonaba si lo hacía. No encuentras nada más de utilidad en esa computadora."
                    response +="\n(Recuerdas haber visto a los padres de ese #$% en las reuniones del colegio, así que no será difícil saber donde encontrarlos. Acudes directamente a la policía con lo que sabes ahora, ¿o vas a hablar con sus padres?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Llamar a la policía"
                    response+="\nB. Hablar con los padres de #$%"
                case 'c':
                    #Presionar a Valentina: 0dc
                    response = "Alcanzas a Valentina y la tomas por el brazo, intenta resistirse, así que no te queda otra opción que apretar más fuerte. Le preguntas furioso la verdad de lo que pasó, y ella, sin tener ninguna otra opción, te relata con la voz entrecortada que todo se fue al carajo el día en el que fueron con un grupo de estudiantes a un concierto, entre ellos estaba #$%, un chico que le gustaba demasiado a tu hija; Resulta que #$% se dio cuenta rápidamente de los sentimientos de tu hija hacia él, y decidió aprovecharse de ellos, llegando a extremos que fueron en contra de la voluntad de tu hija, sin embargo, ella quería creer en él; Pero #$% se distanció después de lo sucedido, no contestaba, la abandonó completamente; Meses, después, tu hija le comentó a Valentina que estaba embarazada, así que estaba decidida a confrontar a #$% de cualquier forma, y le pedía su apoyo para ello; Pero Valentina le dio la espalda, todo porque el padre de #$% es el mismísimo profesor director de su salón, y prometió recomendarla a una buena universidad si se mantenía alejada del asunto."
                    response +="\n(Valentina no para de disculparse, aunque no debería hacerlo contigo precisamente. Ahora que sabes lo que pasó en realidad, no puedes pensar claramente, todo tu ser gira en vengarte por lo que ese maldito le hizo a tu hija. Pero Valentina te dice que no hagas ninguna estupidez, va a llamar a la policía. A lo lejos vez a #$% salir del colegio, ¿vas a por él, aunque Valentina llame a la policía, o decides amenazarla para que no lo haga?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Amenazar a Valentina"
                    response+="\nB. Perseguir a #$%"
                case 'd':
                    #Buscar a #$%: 0dd
                    response = "Quieres saber lo que sucedió, y si la culpa es de #$%, ¿quién mejor que él para que te de las respuestas necesarias? No tardas mucho en encontrarle, sin embargo, en el instante que #$% se da cuenta de que tú te aproximas hacia él, comienza a correr con todas sus fuerzas hacia dentro del colegio. "
                    response +="\n(Ante tal reacción, para ti ya no hay más sospechas, ¿qué harás? ¿Llamarás a la policía, seguro de que tienes razón, o perseguirás a #$%, para obtener más información)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Perseguir a #$%"
                    response+="\nB. LLamar a la Policia"
        case 4:
            match value:
                case '0':
                    #Escuchar a tu esposa: 0010
                    response = "Escuchas lo que ella te tiene que decir. Entre lágrimas, te expresa lo mucho que le duele que estés tan distante, que te nota raro, y le aterra pensar que vayas a cometer alguna estupidez. Quiere afrontar la situación contigo, como siempre lo han hecho, quiere confiar en que la policía les dirá la respuesta, y sabe que tu hija no hubiera pedido venganza."
                    response +="\n(No sabes qué decir, quieres correr y abrazarla con todas tus fuerzas como siempre, pero a la vez te sientes ansioso por saber la verdad por tu cuenta, no confías en la policía. ¿Le haces caso a tu mujer o te marchas?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Escuchar a tu esposa"
                    response+="\nB. No escuchar a tu esposa"
                case '1':
                    #No escuchar a tu esposa: 0011
                    response = "No quieres saber lo que tu esposa tiene para decirte, no te va a convencer, así que no gastarás tiempo en dejar que lo intente. Te marchas, dispuesto a hablar con #$% y preguntarle si sabe algo de lo sucedido. "
                    response +="\n(Sin embargo, ya es de noche. Sabes dónde viven los padres de #$% gracias al grupo que hicieron en el colegio, pero estás seguro de que sea una buena idea ir a esta hora. Puedes ir de todas formas o presentar el diario a la policía, dejándole el resto a ellos.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Ir a la casa de #$%"
                    response+="\nB. Vas a la policia"
                
                case '2':
                    #Llamar a la policía: 0dc2
                    response = "Llegas a la comisaría convencido de que la policía esta vez podrá ayudarte con lo que sabes. Pero una vez investigan a #$%, dicen que no encontraron nada que haga que tenga que ver con el suicidio de tu hija. Además, te prohíben investigar por tu cuenta, ya que los padres de #$% pusieron una fuerte queja al departamento de policía, y no quieren más problemas. Pasaron los días y la investigación nunca llegó a nada, nunca supiste por qué lo hizo, moriste en el alcohol, atormentado por la culpa que tú mismo te impusiste."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case '3':
                    #Hablar con los padres de #$%: 0dd3
                    response = "Una vez llegas a su casa, tocas el timbre y te presentas como el padre Vanesa. Justo cuando terminas de introducirte, detrás de la puerta todo queda en silencio un tiempo, luego de eso, la vos del padre te dice que están muy ocupados justo ahora, que no pueden hablar contigo, así que lo mejor es que te marches. Sin embargo, tú no te vas a ir, y luego de insistir con que solo quieres hacerles unas preguntas, te gritan que te marches o llamarán a la policía."
                    response +="\n(¿Por qué no quieren hablar contigo, acaso esconden algo? Ese pensamiento consume todo tu ser, así que, furioso, contemplas dos opciones, seguir insistiendo pacíficamente, o entrar violentamente a la casa para conseguir respuestas, ¿Qué vas a hacer?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Insistir violentamente"
                    response+="\nB. Insistir pacíficamente"
                case 'c':
                    #Amenazar a Valentina: 0dc4
                    response = "No vas a dejar que esa chica llame a la policía, y piensas dejárselo bien claro. Luego de hacerle entender que le pasará lo mismo que a #$% si llega a decir una palabra, te dispones a darle caza, sin embargo, tardaste bastante hablando con Valentina, así que alcanzarlo ahora tomará un tiempo."
                    response +="\n(Planeas ir a por #$% sin importar qué, ¿vas ya mismo o esperas a la noche?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Vas por #$% en el día"
                    response+="\nB. Vas por #$% en la noche"
                case 'd':
                    #Perseguir a #$%: 0dd5
                    response = "Ignoras completamente las amenazas de Valentina y te aproximas furioso a donde se encuentra #$%. Sin embargo, este apenas te ve comienza a correr hacia la calle."
                    response +="\n(Durante la persecución, #$% gira una esquina, y cuando haces lo mismo, ya no lo ves. Hay un callejón a la derecha, ¿investigas el callejón o continúas corriendo hacia el frente?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Sigues derecho"
                    response+="\nB. Giras el callejón"
                case 'e':
                    #Perseguir a #$%: 0dd6
                    response = "No hay tiempo de llamar a la policía, si Gabriel hizo algo tan horrible que le provoca correr nada mas verte, lo podrás llevar tú mismo a la justicia."
                    response +="\n(Mientras lo perseguías, pierdes su rastro entre la multitud de estudiantes que salen disparados a sus casas, solo pudo haber hecho dos cosas, subir al segundo piso, o salir por del colegio por la puerta al final del pasillo, ¿Qué camino eliges?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Buscas a #$% en el segundo piso"
                    response+="\nB. Buscas a #$% fuera del colegio"
                case 'f':
                    #Policia: 0dd7
                    response = "Llamas a la policía, sin embargo, no sabes cómo explicarles que tienes la sospecha de que un chico de grado 11 hizo algo terrible. Aun así, envían una patrulla y, luego de un gran ajetreo, dan con #$%, el cual estaba con su padre, el profesor director del salón en donde estudiaba tu hija. Luego de una charla, los policías se marchan, no sin antes multarte por causar semejante alboroto en un colegio, luego recibes una denuncia por parte de los padres de #$%, y se te prohíbe acercarte a cualquiera de los miembros de esa familia. Nunca supiste lo que pasó."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
        case 5:
            match value:
                case '0':
                    #Escuchar a tu esposa: 00100
                    response = "La abrazas con fuerza, y le prometes que superarán esto juntos. Le pides perdón por haberte ausentado, y, a punto de romper en llanto, juras materializar la bondad que hacía especial a tu hija. Los años pasaron, y aprendieron a recordarla con cariño, la policía nunca encontró nada."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '1':
                    #No escuchar a tu esposa: 00111
                    response = "Pese a lo conmovido que estás, no puedes abandonar la idea de saber la verdad, así que te marchas prometiendo volver cuando se haya hecho justicia."
                    response +="\n(Pero tu esposa te detiene, te agarra fuertemente del brazo y te implora que no te vayas, no quiere que la dejes sola, ni mucho menos que termines haciendo alguna tontería. Pero tú estás demasiado determinado como para cambiar de opinión. ¿Qué vas a hacer, forcejear con ella, o intentar convencerla de que adopte tu determinación?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Forcejear con tu esposa"
                    response+="\nB. Convencer a tu esposa"
                case '2':

                    #Ir a la casa de #$%: 00122
                    response = "Partes determinado a encontrar a #$%, y una vez llegas a la casa, comienzas a tocar el timbre, esperando alguna respuesta. Sin embargo, la puerta se abre, y entre la oscuridad emerge un potente golpe. Despiertas encerrado en la comisaría, el diario no está, y pese a tus declaraciones, los agentes dicen que irrumpiste en la casa de una familia con intenciones violentas, y que ellos te noquearon en defensa personal mientras llegaba la policía. Te sueltan luego de unos días, prohibiéndote acercarte a la familia de #$%. Sin el diario, no tienes nada más de lo que agarrarte para buscar respuestas, así que nunca supiste la verdad."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '3':
                    #Vas a la policia: 00133
                    response = "Llegas a la estación de policía con el Diario de tu hija. Y después de explicar la situación, lo entregas con la promesa de que ellos lo examinarán y te informarán en unas semanas."
                    response +="\n(Pero no estás satisfecho, quieres que lo hagan lo más pronto posible, que le den la importancia necesaria. ¿Presionas a la policía, o eres paciente y regresas a tu casa?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Eres paciente"
                    response+="\nB. Presionas a la policía"
                case '4':
                    #Insistir violentamente: 0dd44
                    response = "Ya has tenido suficiente, si no abren la puerta, lo harás por ti mismo. Comienzas a patear la puerta, mientras escuchas que toda la conmoción que pasa al otro lado. Logras romperla y esquivas el golpe que el padre de #$% dirigía a tu cara con un bate."
                    response +="\n(¿Qué harás ahora? Seguro la policía viene en camino, necesitas respuestas rápido. ¿Corres y tomas a la madre como rehén, o las buscas en el padre?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Tomas a la madre como rehén"
                    response+="\nB. Luchas con el esposo"
                case '5':
                    #Insistir pacíficamente: 0dd55
                    response = "Ya no puedes más. Les imploras por una respuesta, no quieres vivir sin saber por qué lo hizo, por qué alguien tan amable y bondadosa terminó quitándose la vida. Solo hay silencio al otro lado, seguramente ya han llamado a la policía, no hay mucho que hacer."
                    response +="\n(¿Insistes un poco más, o te rindes?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Insistes más a los padres"
                    response+="\nB. Te rindes"
                case 'c':
                    #Vas por #$% en el día 0dc6
                    response = "No puedes esperar más, tiene que pagar. Te subes en tu carro y lo persigues, lo encuentras en una avenida, y sin pensarlo dos veces, bajas del auto y te abalanzas sobre él. Sin embargo, no puedes hacer mucho, la gente de alrededor de confronta y terminas siendo golpeado por muchas personas, las cuales querían defender a un chico de 18 años de un señor loco que se bajó de un carro a pegarle. Luchas con todas tus fuerzas, pero entre toda la confusión, algún desquiciado te hizo una herida con algo diferente a sus puños. Pierdes las fuerzas y, mientras caes al suelo, te das cuenta de que no te volverás a levantar."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'd':
                    #Vas por #$% en la noche 0dd7
                    response = "Decides esperar y tener un buen plan para efectuar tu venganza. Valentina te había dicho que #$% iba mucho a comprar cigarrillos por la noche, así que aguardarás a que él vaya a ti por la noche. Todo sucede como lo planeaste. Lo tomas por sorpresa y le tapas la boca, le atas y lo llevas a tu carro. Conduces a toda velocidad fuera de la ciudad, la adrenalina no para de correr por tu cuerpo. Te quieres vengar, y lo harás. "
                    response +="\n(Sin embargo, cuando al fin te detienes y bajas junto a #$%, no puedes evitar sentir algo extraño, algo que te detiene. Puedes acabar con #$% ahí mismo, sin oír si tiene algo para decir, o puedes escucharle.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Escuchas a #$% secuestrado"
                    response+="\nB. Acabas con #$% secuestrado"
                case 'e':
                    #Sigues derecho: 0dd5e
                    response = "Corres hacia el frente, con la esperanza de encontrarle cuando gires la próxima esquina y alcanzarle. Y efectivamente pasó eso, si bien el chico es rápido, no tiene tanta resistencia como tú, así que cada vez estás más cerca de alcanzarle."
                    response +="\n(#$% se da cuenta de esto, y decide tirarte un cesto de basura que había en la calle. Estás muy cerca. ¿Saltas el cesto, o frenas y lo rodeas?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Saltas el obstáculo"
                    response+="\nB. Rodeas el obstáculo"
                case 'f':
                    #Giras el callejón: 0dd6f
                    response = "Giras hacia el callejón y te adentras en él. Llegas al final sin encontrarle, y mientras te dispones a seguir tu cometido, sientes como una hoja fría te atraviesa el hombro lentamente. Te quieren robar. Furioso, forcejeas, no tienes tiempo para esto, quieres alcanzarle y hacerle pagar, pero al delincuente no le importan tus razones, está drogado, y si no le das lo que quiere cometerá una locura. Y así fue."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'g':
                    #Buscas a #$% en el segundo piso: 0dd44g
                    response = "Subes al segundo piso. Encuentras a #$% intentando acceder a un curso, pero vuelve a correr justo cuando te ve. La persecución llega hasta unas escaleras. #$% te dice que no te acerques más, que la policía seguro ya viene en camino, que te vayas por donde viniste."
                    response +="\n(Notas que ya está cansado, así que no crees tener problemas en atraparlo si continúa la persecución, sin embargo, se ve demasiado asustado. ¿Deberías intentar hablarle desde la distancia, o atraparlo para interrogarle sin que pueda llegar a escapar?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Intentas atrapar a #$% en el colegio"
                    response+="\nB. Hablas con #$% en el colegio"
                case 'h':
                    #Buscas a #$% fuera del colegio: 0dd44h
                    response = "Sales del colegio en busca del chico, pero no hay rastros de él en ninguna parte. Das un vistazo al colegio desde afuera y lo ves en el segundo piso, entrando a un salón. Cuando llegas, te recibe el profesor director del curso, quien fue también profesor de tu hija y que es padre de #$%. Te pide hablar, si accedes no llamará a la policía y si esta llega por alguien más les convencerá de que es todo un malentendido."
                    response +="\n(¿Qué vas a hacer, escuchar lo que tiene que decir o ignorar todo y arremeter en contra de #$%?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Atraviesas al padre de #$% en el colegio"
                    response+="\nB. Aceptas hablar con el padre de #$%"
        case 6:
            match value:
                case '0':
                    #forcejear con tu esposa: 001110
                    response = "Forcejeas con tu esposa, no quieres lastimarle, solo quieres que te suelte, quieres salir y buscar al culpable, sabes que hay uno, lo sientes, y quieres hacerle pagar. Pero tu esposa no se rinde, el conflicto avanza, y tú, cansado de todo, la empujas hacia atrás con fuerza. No mediste tu fuerza, ni viste a dónde la empujaste. Se rompió el cuello con el filo de un mueble para guardar porcelana. Todo es silencio, te arrepientes de cada segundo de tu existencia. Te entregas a la policía y mueres en la cárcel, infeliz hasta tu último día."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case '1':
                    #convencer a tu esposa: 001111
                    response = "Con tu esposa fuertemente aferrada a ti, decides que lo mejor es lograr que te entienda, que se una junto a ti para encontrar la verdad."
                    response +="\n(Hay varios sentimientos que le quisieras expresar, pero los que más destacan son la culpa y el odio. ¿De cuál le vas a hablar?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Hablar de Culpa."
                    response+="\nB. Hablar de Odio." 
                case '2':
                    #Eres paciente: 001122
                    response = "Decides tragarte las ganas de gritarles a todo pulmón y te retiras a tu casa, confiando en que hallarán una respuesta."
                    response +="\n(Los días pasan y la espera cada vez te hace más daño. La intriga te mata, y no puedes parar de pensar. Ante tanto estrés, lo único que se te antoja es un trago. ¿Te quedas en casa o vas a un bar?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Qudarse en casa."
                    response+="\nB. Ir a un bar." 
                case '3':
                    #Presionas a la policía: 0dc33
                    response = "Gritas que no es justo, gritas que quieres que se le de importancia, y ante las reacciones juzgadoras y despreocupadas de los agentes pierdes la paciencia poco a poco."
                    response +="\n(Al final logras que te encierren, agrediste a un policía, era de esperarse. Te condenan a dos años, para ti nada tiene sentido. Los odias, y ahora, atrapado en una prisión, no tienes mucho más que hacer que proyectar tu odio mientras esperas a salir. ¿Intentas escapar o esperas a tu salida?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Intentar escapar."
                    response+="\nB. Buscar una salida." 
                case '4':
                    #Tomas a la madre como rehén: 0dd44g4
                    response = "Te abalanzas rápidamente sobre la esposa y la tomas como rehén. El padre no sabe qué hacer, así que aprovechas la oportunidad para hacer que hable, amenazando con lastimar a su esposa si decide no hacerlo. El padre se limita a insultarte y a gritar que la policía está en camino, que dejes esa idiotez y no te encerrarán durante tanto tiempo. Aprietas a la mujer con fuerza, y el esposo te dice que está bien, te contará lo que sabes si la sueltas."
                    response +="\n(Ya no puedes dar marcha atrás. ¿Lastimas a la esposa para que hable, o la sueltas confiando en la palabra de su esposo?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Lastimar a la esposa."
                    response+="\nB. Soltarla." 
                case '5':
                    #Luchas con el esposo: 0dd44g5
                    response = "Le exiges respuesta al padre de #$%. Él te dice que no sabe nada mientras se abalanza hacia ti con fiereza. Comienzan a forcejear, pero tu contrincante gana ventaja sobre ti, y te termina empujando contra el suelo, pone sus manos sobre tu cuello, y no parece tener intenciones de soltarte."
                    response +="\n(De su camisa calló un lapicero, y durante todo el forcejeo, una botella de vino terminó intacta cerca de tu cabeza. ¿Qué usarás para contraatacar, el lapicero o la botella?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Atacar con el lapicero."
                    response+="\nB. Atacar con la botella." 
                case '6':
                    #Insistes más a los padres: 0dd55
                    response = "(Aún no te das por vencido, con tus últimas fuerzas, quieres convencerlos hablándoles de justicia, ¿o amenazándoles?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Hablar de justicia."
                    response+="\nB. Amenazarles." 
                case '7':
                    #Te rindes: 0dd66
                    response = "Te rindes y esperas a que la policía llegue. Llegan dos patrullas y te detienen sin escuchar una sola palabra de lo que tienes que decir. No tienes más pruebas que un chat, y luego de que te prohíban acercarte a esa familia el resto de tu vida, pierdes la esperanza en encontrar la verdad."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case 'c':
                    #Escuchas a #$% secuestrado: 0dd44g6
                    response = "Decides quitarle la cinta de la boca a #$% y escuchar lo que tiene que decirte. Al principio dice que estás loco, que lo dejes ir, y que te van a encerrar. Pero luego de un silencio de unos minutos, comienza a disculparse, sabe que lo que hizo fue horrible, y que no sabía que tu hija haría algo como eso, él solo quería escapar de la responsabilidad. Es lo que mejor sabe hacer."
                    response +="\n(#$% te dice que acepta ir a prisión, ya no va a escapar más. Ahora está en tu mano lo que hacer con él. Puedes perdonarle y entregarlo a la policía, o cobrar su vida por la de tu hija.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Entregarlo a la policía."
                    response+="\nB. Matar a #$%." 
                case 'd':
                    #Acabas con #$% secuestrado: 0dd44g7
                    response = "Escucharlo no va a cambiar lo que hizo. Acabas con él con odio, cercenando su vida lentamente, tu hija también sufrió mucho antes de morir, al fin y al cabo. Cuando terminas, escapas lejos, escondiendo el cadáver lo mejor que puedes. Te terminan encontrando, y mueres de viejo en la cárcel, habiendo efectuado tu venganza, pero sin sentirte satisfecho del todo."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'e':
                    #Saltas el obstáculo: 0dd5e8
                    response = "Saltas con todas tus fuerzas el cesto de basura. Pero nunca has sido tan ágil, terminas tropezando y dándote un gran golpe en la cabeza. Despiertas en el hospital, con la policía esperando a que te recuperes para encerrarte por intentar hacerle daño a un chico de 18 años. Cuando explicas lo que pasó, investigan y no llegan a nada. Valentina les dijo que te mintió porque estaba asustada, y #$% dijo que corrió porque gritaste que lo ibas a matar, aunque nunca lo hiciste. Eres encarcelado, y cuando sales de prisión ya todo es demasiado tarde."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'f':
                    #Rodeas el obstáculo: 0dd5e9
                    response = "Decides no tomarte el obstáculo a la ligera y lo rodeas, teniendo cuidado de que no te atropellen. #$%, cansado de toda la persecución, se esconde en una construcción sin acabar. Lo sigues a través de los pisos hasta que llegas arriba del todo. Está demasiado alto como para saltar y seguir vivo, así que #$% ya no tiene escapatoria."
                    response +="\n(Mientras te acercas a él, te grita que te detengas, que sabe lo que hizo y no quiere seguir escapando más. Acepta entregarse a la policía. ¿Lo entregarás a la Policía, o tomarás la justicia por tus propias manos?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Entregar a #$% a la policía."
                    response+="\nB. Terminar con él." 
                case 'g':
                    #Intentas atrapar a #$% en el colegio: 0dd44g8
                    response = "Te aproximas rápidamente ante el ya exhausto #$%. Él corre por las escaleras, pero lo ves tropezar y escuchas como cae con fuerza. Llegas a las escaleras, pero #$% ya no se mueve. Te encierran en prisión gracias a lo sucedido. Nunca supiste lo que pasó en realidad con tu hija."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'h':
                    #Hablas con #$% en el colegio: 0dd44h9
                    response = "Accedes a hablar. #$% se arrodilla, y sin decirte nada más, comienza a llorar pidiéndote perdón. La policía llega, y es entonces cuando #$% confiesa: Salieron a un concierto, y esa noche la violó y la embarazó, pero decidió evitarla por todos los medios posibles, dejándola sola con su problema. Aseguró no sospechar que ella se quitaría la vida, pero el delito ya estaba hecho. Fue a prisión, como él ya tenía 18 cuando eso sucedió tardó más en salir. Supiste la verdad y llevaste al culpable a la justicia. . ."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case 'i':
                    #Atraviesas al padre de #$% en el colegio: 0dd44g5i
                    response = "No quieres perder más tiempo, quieres interrogar a #$%, y eso harás. Sin embargo, el padre comienza una pelea contigo en defensa de su hijo. Furioso, sales vencedor, dejando al padre en el piso, con la nariz rota y sin apenas tener fuerzas para moverse. Te aproximas a #$%, quien, asustado por toda la pelea, se había arrinconado en una esquina. Es tu momento de interrogarle, de saber lo que hizo, pero cuando te ve a los ojos, sientes que está viendo a un monstruo. En ese momento piensas en tu hija, recuerdas su sonrisa, su bondad, lo felices que los hacía a todos, jamás hubieras querido que te vea así."
                    response +="\n(Tienes a #$% justo al frente, aún hay adrenalina en tu cuerpo, decides sacarle las respuestas, aunque esté tan asustado, ¿o paras ya con toda esta locura?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Sacarle las respuestas a la fuerza."
                    response+="\nB. Parar." 
                case 'j':
                    #Aceptas hablar con el padre de #$%: 0dd44hj
                    response = "Accedes a conversar. El padre te pide que te largues ahora, y vayas a su casa esa misma noche. Cuando llegas, te recibe solamente el padre, y te pide que tomes asiento. Pero nada más te sientas, sientes algo frío tocar tu cabeza: “Escucha, mi hijo no sabía lo que estaba haciendo, tu hija tuvo la culpa por no negarse apropiadamente. Tampoco lo denunció, se mató ella sola. Así que ¿por qué mejor no nos dejas en paz, tomas este dinero y te marchas para jamás volver?”"
                    response +="\n(Tusangre hierve con cada palabra que sale de la boca de ese bastardo, ves que en la mesa hay un maletín con una gran cantidad de dinero, y aunque no sabes si el arma está cargada o no, averiguarlo podría ser mortal. ¿Sucumbes ante el miedo y aceptas el soborno, o te rehúsas?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Aceptar soborno."
                    response+="\nB. Rehusarse." 
        case 7:
            match value:
                case '0':
                    #Hablas de la culpa con tu esposa: 0011110
                    response = "Le comunicas a tu esposa lo culpable que te sientes por no haber estado ahí para su hija cuando lo necesitaba. Le expresas que esa culpa es la que te motiva a actuar, y que no puedes estar en paz hasta dejar de sentirte culpable. Tu esposa, que al principio te corregía con que lo importante no era encontrar culpables, ahora se siente una de ellos."
                    response +="\n(Ves que algo se rompe dentro de ella, y sale corriendo hacia su habitación. ¿Le sigues o te marchas?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Seguirla a la habitación."
                    response+="\nB. Marcharte." 
                case '1':
                    #Hablas del odio con tu esposa: 0011111
                    response = "Le comunicas a tu esposa el odio que te tienes por quien tenga la culpa de haber hecho que tu hija se quitara la vida. Le gritas que ese odio es lo que te motiva a actuar, y que no puedes estar en paz que quien tenga la culpa tenga su merecido. Notas que la expresión de tu esposa cambió, y te dice que te teme. Te amenaza con llamar a la policía si intentas hacer alguna tontería. Ante tal amenaza, decides no hacer nada. Pasan los años, terminas por divorciarte, y pasas el resto de tu vida solo. Odiándote a ti mismo."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '2':
                    #Eres paciente en casa: 0011222
                    response = "Pese a las ganas de tomar un trago, permaneces esperando en casa, junto a tu esposa. Pasan las semanas y la policía te informa que logró ver lo que estaba escrito en el diario de tu hija: #$% abusó sexualmente de ella, y después de eso no mostró interés en continuar siquiera hablando con ella, quien aún seguía creyendo en que él cambiaría de opinión. Pasaron los días y ella se dio cuenta de que quedó embarazada, decidida a confrontarle, fue a buscar apoyo en su mejor amiga, la cual le dio la espalda. Asustada de hacerlo sola, decidió que lo mejor era acabar con todo ella misma, y así lo hizo"
                    response +="\n(Ahora que sabes la verdad, la policía te informa que van a arrestarle mañana. ¿Dejarás a la policía acabar el trabajo, o harás justicia tú mismo?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Dejarle todo a la policía."
                    response+="\nB. Tomar venganza tú mismo." 
                case '3':
                    #Vas a beber: 0011333
                    response = "Cedes a las ganas de tomar un trago, de ahí en adelante casi que permaneces en el bar, ignorando lo que te diga tu esposa. Pasan las semanas y la policía te informa que logró ver lo que estaba escrito en el diario de tu hija: #$% abusó sexualmente de ella, y después de eso no mostró interés en continuar siquiera hablando con ella, quien aún seguía creyendo en que él cambiaría de opinión. Pasaron los días y ella se dio cuenta de que quedó embarazada, decidida a confrontarle, fue a buscar apoyo en su mejor amiga, la cual le dio la espalda. Asustada de hacerlo sola, decidió que lo mejor era acabar con todo ella misma, y así lo hizo"
                    response +="\n(Ahora que sabes la verdad, la policía te informa que van a arrestarle mañana. ¿Dejarás a la policía acabar el trabajo, o harás justicia tú mismo?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Dejarle todo a la policía."
                    response+="\nB. Tomar venganza tú mismo." 
                case '4':
                    #Intentas escapar de la cárcel: 0dc334
                    response = "Intentas escapar de la cárcel, ¿qué tan complicado puede ser? Respuesta rápida, mucho. Te terminan mandando a otra cárcel a la par que aumentan tu condena. Cuando sales de prisión ya nada tiene sentido, estás solo y nunca supiste lo que pasó con tu hija."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '5':
                    #Esperas en la cárcel: 0dc335
                    response = "Esperas en la cárcel, pasan las semanas y te un guardia te envía el siguiente comunicado: “La investigación fue fructífera, encontramos que #$% abusó sexualmente de ella, y después de eso no mostró interés en continuar siquiera hablando con ella, quien aún seguía creyendo en que él cambiaría de opinión. Pasaron los días y ella se dio cuenta de que quedó embarazada, decidida a confrontarle, fue a buscar apoyo en su mejor amiga, la cual le dio la espalda. Asustada de hacerlo sola, decidió que lo mejor era acabar con todo ella misma.”. Pasan los días y, entre los reclusos nuevos, ves que entra #$%."
                    response +="\n(Ya en el comedor, lo tienes cara a cara, ¿Acabas con él, o lo acusas con el resto de los presos?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Atacar a #$%."
                    response+="\nB. Exponerlo a los demás reclusos." 
                case '6':
                    #Dañas a la esposa: 0dd44g46
                    response = "No tienes más opción, y no puedes confiar en que el padre de #$% haga lo que prometió una vez la sueltes, así que comienzas a lastimar a su esposa. Al escuchar los gritos de dolor, el padre cede y te cuenta lo que pasó: “Fue nuestro hijo, #$% abusó de tu hija sexualmente después de un concierto, no se quería arruinar su vida por ese error, así que nos lo comentó, y estábamos listos para defenderle cuando ella le denunciara. Pero nunca lo hizo, y cuando nos enteramos de que había terminado con su vida, estábamos tan asustados que decidimos que nadie diría nada sobre el tema.”"
                    response +="\n(Ahora sabes lo que causó que ella se fuera, y tienes en tus manos a la madre del culpable. Tu hija significaba todo para ti, puedes dejar que se entreguen a la policía, o quitarle a #$% algo igual de importante para siempre.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Ir a la policía."
                    response+="\nB. Tomar una vida en venganza de la de tu hija." 
                case '7':
                    #Sueltas a la esposa: 0dd44g47
                    response = "Confiando en lo que el padre de #$% te promete, sueltas a tu rehén, quien corre llorando a sus brazos. Sin embargo, en vez de obtener la verdad, recibes un golpe en la cabeza. Despiertas encerrado en la comisaría. Se te acusa por irrumpir en una vivienda con intenciones violentas, y que ellos te noquearon en defensa personal mientras llegaba la policía. No tienes ninguna prueba para librarte de esta situación, te condenan a algunos años de prisión. Cuando sales ya nada tiene sentido."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '8':
                    #Atacas con la botella: 0dd44g58
                    response = "Agarras la botella y la revientas contra la cabeza de tu adversario. Cae al suelo en dolor, y aprovechas para tomar ventaja de él. Cuando lo haces, le gritas a su esposa que te diga la verdad de lo que pasó, ella, aterrada, te dice: “Fue nuestro hijo, #$% abusó de tu hija sexualmente después de un concierto, no se quería arruinar su vida por ese error, así que nos lo comentó, y estábamos listos para defenderle cuando ella le denunciara. Pero nunca lo hizo, y cuando nos enteramos de que había terminado con su vida, estábamos tan asustados que decidimos que nadie diría nada sobre el tema.”"
                    response +="\n(Ahora sabes lo que causó que ella se fuera, y tienes en tus manos al padre del culpable. Tu hija significaba todo para ti, puedes dejar que se entreguen a la policía, o quitarle a #$% algo igual de importante para siempre.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Ir a la policía."
                    response+="\nB. Tomar una vida en venganza de la de tu hija." 
                case '9':
                    #Atacas con el lapicero: 0dd44g59
                    response = "Agarras el lapicero y lo entierras con fuerza sobre el ojo de tu adversario. Un chorro de sangre comienza a brotar, y entre más sangre sale, menos razón te queda. Como si tus instintos más bajos se salieran de control por el pánico y la adrenalina, terminas por terminar el trabajo. Te encarcelan por homicidio, entre otros cuantos cargos más. Te pudres en prisión, obsesionado con saber lo que pasó, hasta el fin de tus días."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'a':
                    #Le hablas a los padres sobre la justicia: 0dd44hja
                    response = "Tu hija era todo para ti, ellos como padres que son seguro lo entienden, también quisieran saber lo que sucedió si su hijo corriera con el mismo destino. Imploras que, si tienen algo que ver, por favor dejen que se haga justicia, ningún padre merece perder a su hija y nunca saber la razón. Ya no les pides respuestas, ahora, les pides ayuda. La policía llega, pero cuando se dirigían a llevarte, la puerta se abre, son los padres de #$%, junto con él, los que terminan subiendo a la estación de policía. Pasan los días y se te explica lo que sucedió: #$% abusó sexualmente de tu hija, y después de eso no mostró interés en continuar siquiera hablando con ella, quien aún seguía creyendo en que él cambiaría de opinión. Pasaron los días y ella se dio cuenta de que quedó embarazada, decidida a confrontarle, fue a buscar apoyo en su mejor amiga, la cual le dio la espalda. Asustada de hacerlo sola, decidió que lo mejor era acabar con todo ella misma. #$% quería arruinar su vida a los 18 años por ese error, así que les comentó a sus padres la situación, y ellos estaban listos para defenderle cuando ella le denunciara. Pero nunca lo hizo, y cuando se enteraron de que había terminado con su vida, estaban tan asustados que decidieron que ocultar todo. Pero les hiciste entrar en razón. Ahora #$% está en la cárcel, supiste lo que pasó, y se hizo justicia."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'b':
                    #Amenzas a los padres: 0dd44hjb
                    response = "Amenazas a los padres con entrar violentamente si no les das una respuesta, comienzas a golpear con fuerza la puerta, pero ellos empujan desde el otro lado. La policía llega con dos patrullas y te detienen sin escuchar una sola palabra de lo que tienes que decir. No tienes más pruebas que un chat, y luego de que te prohíban acercarte a esa familia el resto de tu vida y te encarcelen pierdes la esperanza en encontrar la verdad."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'c':
                    #Perdonas a #$% secuestrado: 0dd44g6c
                    response = "Ves a #$% y piensas en tu hija, recuerdas su sonrisa, su bondad, lo felices que los hacía a todos, ella jamás habría permitido que le quitases la vida a un ser humano, sin importar las razones. Decides perdonar a #$%, él te pide ir a la comisaría, y se entrega sin rechistar. Hiciste justicia sin convertirte en un monstruo para tu hija, esperas que ella pueda descansar en paz, y tú quieres hacer lo mismo, dentro de algunos años, podrás hacerlo."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case 'd':
                    #Matas a #$% secuestrado: 0dd44g7d
                    response = "Escucharlo no va a cambiar lo que hizo. Acabas con él rápidamente. Cuando terminas, no puedes ni siquiera ver la escena, sientes que te has convertido en un monstruo. Vas directamente a una estación de policía y te entregas. Hiciste justicia, pero pagaste mucho a cambio. Te pudres en la cárcel deprimido, y pasas tus días vagando en tu mente entre toneladas de culpa."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case 'e':
                    #Forcejeas con #$% en construcción: 0dd5e9e
                    response = "Cegado en vengarte decides abalanzarte sobre él y hacerle pagar lo que hizo. Comienzan a forcejear violentamente, acercándose cada vez más al borde del edificio. #$% te implora que te detengas, que él de verdad se entregará y pagará en prisión por lo que hizo, pero para ti no es suficiente. De repente, ambos se resbalan y comienzan a caer. Ves como el cielo se aleja mientras el suelo se hace cada vez más grande, la expresión de #$% es de total terror. Pero tu ya no puedes pensar en nada más, por fin todo terminó, si tienes que morir para llevarte a ese bastardo está bien, al fin y al cabo, se lo merece. Caes al suelo, y todo se viste de un negro tan potente que difumina tu conciencia hasta que tu mera existencia se dispersa."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'f':
                    #Aceptar que #$% se entregue en construcción: 
                    response="Ves a #$%  piensas en tu hija, recuerdas su sonrisa, su bondad, lo felices que los hacía a todos, ella jamás habría permitido que le quitases la vida a un ser humano, sin importar las razones. Decides perdonar a #$%, él te pide ir a la comisaría, y se entrega sin rechistar. Hiciste justicia sin convertirte en un monstruo para tu hija, esperas que ella pueda descansar en paz, y tú quieres hacer lo mismo, dentro de algunos años, podrás hacerlo."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'g':
                    #Sacarle respuestas a #$% en colegio: 0dd44g8f
                    response = "Arremetes contra un asustado #$% en busca de respuestas. Lo único que logras es lastimarlo sin sentido, nunca te dijo nada porque estaba petrificado del miedo. La policía llega y te detienen al instante. Te pudres en prisión sin saber lo que le pasó a tu hija, arrepintiéndote de todo."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'h':
                    #Rendirte en colegio: 0dd44h9g
                    response = "Te arrodillas y le pides perdón a #$% por lo que estás haciendo, le pides perdón a tu hija, porque estás seguro de que si te viera ahora mismo saldría corriendo y te odiaría, le pides perdón a todos por el alboroto, y te resignas a esperar a la policía. Sin embargo, #$% comienza a hablar, confiesa lo que hizo, como abusó de tu hija y huyó a los brazos de sus padres para no hacerse responsable de nada, se arrepiente de no haber hablado con tu hija, más aún cuando se enteró que estaba embarazada, el no pensó que ella se quitaría la vida. Llega la policía y termina por llevarse a ambos. Sales de prisión después de unos meses, ya sabes lo que pasó, y el culpable seguirá ahí dentro por un tiempo."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case 'i':
                    #Aceptar el soborno: 0dd44h9h
                    response = "Lleno de miedo, aceptas el soborno. Por la seguridad de tu esposa, usas parte del dinero para mudarse de la ciudad. Los años pasan y la culpa no ha parado de crecer, pero no hay nada que hacer ya. Fuiste un cobarde, y lo serás el resto de tu vida."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'j':
                    #Rehusarte al soborno: 0dd44h9i
                    response = "No te vas a rendir tan fácil, sin embargo, decirle que no a alguien en la posición en la que te encuentras no es la mejor idea."
                    response +="\n(Puedes confrontarle ahora, o puedes disimular una rendición para contraatacar después, ¿qué vas a hacer?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Afrontarle ahora."
                    response+="\nB. Disimular rendición." 
        case 8:
            match value:
                case '0':
                     #Vas detras de tu esposa: 0dd44hjj 
                    response = "Sigues a tu esposa hacia la habitación, le abrazas y te das cuenta de lo que has hecho. Al fin ves lo absurdo que es buscar culpables en una situación como esta. No eres un detective, tampoco un matón, ni mucho menos un asesino; eres un padre que ha perdido a su hija, pero también eres un esposo, y eso no va a cambiar. Afrontarás todo junto a tu esposa, y saldrán juntos de lo que sea, incluido este dolor."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '1':
                    #Te marchas: 0dd44hjk
                    response = "Ignoras el llanto de tu esposa y te marchas, aunque no puedes parar de pensar en lo que dijo, en su reacción, y en cómo la hiciste sentir. Al final decides volver y hablar bien con ella, pero ya es demasiado tarde, dejó una nota pidiéndote perdón, ya que ella también era culpable, también era su hija. Decides acompañarla, con tal ya no tienes nada más que perder."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '2':
                    #Dejas que la policía arreste a #$%: 0dd44hja2
                    response = "Decides esperar, la policía hace su trabajo y #$% termina en prisión. Se hizo justicia, la vida continúa junto a tu esposa mientras esperas que tu hija pueda descansar en paz."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '3':
                    #Buscas vengaza por tu cuenta: 0dd44hja3
                    response = "(No hay mucho tiempo que perder, así que tienes que vengarte esta noche, tampoco tienes tiempo para un elaborado plan, las únicas opciones que tienes son incendiar su casa, o irrumpir en ella directamente.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Incendiar la casa."
                    response+="\nB. Irrumpir en ella." 
                case '4':
                    #Dejar a la policía pero borracho: 0dd44hja4
                    response = "Decides esperar, la policía hace su trabajo y #$% termina en prisión. Se hizo justicia, y aunque después la relación con tu ahora exesposa se haya arruinado por el alcohol, la vida continúa. Esperas que tu hija pueda descansar en paz."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '5':
                    #Buscas venganza por tu cuenta, pero borracho
                    response="No hay mucho tiempo que perder, así que tienes que vengarte esta noche. Borracho, no piensas mucho en algún plan, simplemente vas e irrumpes en la casa de #$%. Torpemente intentas ejercer tu venganza, pero solo terminas siendo golpeado por su padre. Luego te encarcelan un tiempo, sales y tu vida no tiene sentido, estás solo y no hiciste lo correcto."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '6':
                    #Atacas a #$% en la cárcel: 0dc3355
                    response = "Te abalanzas hacia #$% con todas tus fuerzas, dispuesto a hacerle pagar por lo que hizo. Sin embargo, los otros reclusos te detienen, dándote una golpiza que te deja muy mal herido. Después del incidente de trasladan a otra prisión, donde cumples el resto de tu condena amargado de por vida por no haber podido vengarte adecuadamente."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '7':
                    #Culpas a #$% en la cárcel: 0dc3356
                    response = "Decides no abalanzarte como un loco y atacar con gente que sabe tu historia después. El plan funciona, y entre todos terminan dándole una golpiza a #$%. Llega un momento en que el resto te dice que ya es suficiente, sin embargo, los recuerdos de tu hija solo te llenan de ira, no conoces final"
                    response +="\n(Puedes acabar con #$%, o parar.)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Tomar la vida de #$%."
                    response+="\nB. Dejarle vivir." 
                case '8':
                    #Vengarze con la madre o padre: 0dd44g47
                    response = "Ya no hay vuelta atrás, decides acabar con la vida de tu víctima y escapar lo más lejos que puedas. Lo haces, y mientras escuchas el llanto de su pareja, sales corriendo del sitio. La venganza está hecha, #$% jamás olvidará ese día, mucho menos porque es su culpa. La policía te termina encontrando y te pudres en prisión. Sacrificaste tu libertad, y con ella, parte de tu humanidad para lograr tu venganza, pero estás satisfecho. END"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '9':
                    #Escapas y vas a la policía con padre o madre: 0dd44g48
                    response = "Sales corriendo de la casa, directo a la estación de policía para contarles todo. Arrestan a #$%, pero a ti también, lo que hiciste no fue correcto y ahora estás pagando por ello en la cárcel por un tiempo, pero se hizo justicia, ya nada más te importa, solo te queda esperar."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'a':
                    #Confrontas al padre en ese momento
                    response = "(Pese a la difícil situación, decides que lo mejor es confrontarlo en el momento. Puedes abalanzarte directamente o intentar sorprenderlo, ¿qué decides?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Abalanzarte ya mismo."
                    response+="\nB. Esperar la oportunidad de hacer un ataque sorpresa." 
                case 'b':
                    #Discimulas una rendición: 0dd44h9ia
                    response = "Le mientes para que te deje salir. Una vez a fuera, sabes que te están observando, y no tienes mucho tiempo antes de que comiencen a sospechar algo y comprometan la seguridad de más de tus seres queridos."
                    response +="\n(Puedes acabarlos ahí mismo, solo tienes que prenderle fuego a esa casa. También puedes dirigirte hacia la policía, qué harás)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Prenderle fuego a la casa."
                    response+="\nB. Correr directo a la policía." 
        case 9:
            match value:
                case '0':
                    #Irrumpir en la casa de #$%: 0dd44hjab
                    response = "Sabes que está mal, que es peligroso, pero no te importa. Una vez llegas a la casa, observas que están cenando, se ven tristes, pero no te importa. Entras, la puerta estaba abierta parece que estaban esperando a alguien, pero no te importa. Irrumpes en el comedor, agarrando uno de lo cuchillos, dispuesto a cometer una atrocidad, no te importan los gritos de todos en la habitación. Te acercas a #$% con las peores intenciones, pero antes de hacer nada se te van las luces. Despiertas en una celda, lo arruinaste, tu estupidez lo arruinó todo, tu esposa no sabe qué pensar de ti, ya habían resuelto lo que sucedió, ya se iba a hacer justicia. Pero para ti no fue suficiente, y ahora pagarás por ello en prisión."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '1':
                    #Incendiar la casa después de esperar: 0dd44hja3c
                    response = "Cae la noche y te acercas sigilosamente al tanque de gas de repuesto que tienen fuera de su casa, tus conocimientos de ingeniería te permiten crear una fuga que vaya directamente dentro de la casa, y luego solo es cuestión de esperar y lanzar la cerilla. Todo vuela por los aires, incluido tú, volaste demasiado fuerte del sitio. La luz de la explosión fue la última luz que viste."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '2':
                    #Parar de golpear a #$% en prisión 0dc3356d
                    response = "Paras, ves al culpable de todo al frente de ti, pero paras. No sabes si es porque no quieres convertirte en un asesino, o solo porque si lo acabas ya no saldrás de prisión, pero paras. Te marchas y dejas a #$% ahí, golpeado hasta tu saciedad. Sales de prisión y continúas tu vida, supiste la verdad y pudiste darle una golpiza al culpable."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '3':
                    #Acabar con #$% en prisión después de golpearlo
                    response = "Ves al culpable de todo al frente de ti, parar para ti no es una opción. No te importa convertirte en un asesino, tampoco te importa ya no salir de prisión, no vas a parar. Para cuando el resto te detiene a la fuerza, ya es demasiado tarde. Te marchas y dejas a #$% ahí, muerto por tu venganza. Te trasladan a otra prisión, aunque ya te da igual. Sacrificaste tu libertad, y con ella, parte de tu humanidad para lograr tu venganza, pero estás satisfecho."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'c':
                    #Atacar a tu enemigo directamente
                    response = "No esperas ni un segundo y te abalanzas sobre el padre de #$%. La pistola si estaba cargada."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END" 
                case 'd':
                    #Ataque sorpresa
                    response = "Decides simular que te vas, pero justo antes de abrir la puerta, te volteas rápidamente y tienes la suerte de que el golpe con el da en la mano del padre de #$%, lo que te permite acercarte y neutralizar su amenaza."
                    response +="\n(Tomas el arma, tienes el control. ¿Llamas a la policía o decides vengarte a sangre fría de esa maldita familia por tu cuenta?)"
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Llamar a la policía."
                    response+="\nB. Matarlos a todos." 
                case 'e':
                    #Incendiar la casa después de disimular
                    response = "Cae la noche y te acercas sigilosamente al tanque de gas de repuesto que tienen fuera de su casa, tus conocimientos de ingeniería te permiten crear una fuga que vaya directamente dentro de la casa, y luego solo es cuestión de esperar y lanzar la cerilla. Todo vuela por los aires, incluido tú, volaste demasiado fuerte del sitio. La luz de la explosión fue la última luz que viste."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case 'f':
                    #Correr a la policía después de disimular
                    response = "No te la piensas dos veces y vas directamente a la policía. Todo sale bien, arrestan al padre y al hijo. Resulta que confiaron completamente en que dejarías de intentarlo, tanto así que no se preocuparon en lo más mínimo de lo que fueras a hacer después. Saliste vivo, con dinero y haciendo justicia."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  

        case 10:
            match value:
                case '0':
                    #Vengarte a sangre fría: 0dd44hja30
                    response = "La primera bala fue para el padre, la segunda para la madre, la tercera para #$%. Ya no te importaba nada, la cuarta bala sería para ti, sino fuera porque la policía llegó a tiempo. Enloqueciste en prisión, tus ojos vacíos habían perdido todo rastro de humanidad."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"  
                case '1':
                    #Llamar a la policía: 0dd44hja21
                    response = "Con el corazón en la mano debido a tanta adrenalina, llamas a la policía. No tardan mucho en llegar y llevarse al padre y al hijo. Saliste vivo, con dinero y haciendo justicia."
                    response+="\n¿Que quieres hacer?: "
                    response+="\nA. Elegir otro camino."
                    response+="\nB. Salir.   -END"
    return response

def changeName(name,current):
    current.setName(name)
    dialogue=""
    if (current.getCurrent()==0): 
        dialogue=dialogos(current.getCurrent(),"0")
        dialogue= translate(dialogue,current.getName())
    else:
        dialogue=dialogos(current.getCurrent(),current.getSequence())
        dialogue= translate(dialogue,current.getName())
    return dialogue

def convertOptionToValidSequence(transitionLevel, digitOption, sequence):
    if digitOption == 'z':
        return 'z'
        
    if (transitionLevel ==1):
        match digitOption:
            case 'a': digitOption ='0'
            case 'b': digitOption ='1'
        return digitOption
    print(""+sequence)
    print(""+str(transitionLevel))
    lastOption = sequence[-1]
    print(lastOption)

    match (transitionLevel):
        case 2:
            match lastOption:
                case '0':
                    match digitOption:
                        case 'a': digitOption ='0' # q0 - q1
                        case 'b': digitOption ='1' # q0 - q2
                case '1':
                    match digitOption:
                        case 'a': digitOption ='c' # c0 - c1
                        case 'b': digitOption ='d' # c0 - c2
                case _:
                    digitOption ='z'

        case 3:
            match lastOption:
                case '0':
                    match digitOption:
                        case 'a': digitOption ='0'  # q1 - q3
                        case 'b': digitOption ='1'  # q1 - q4
                case '1':
                    match digitOption:
                        case 'a': digitOption ='2'  # q2 - q5
                        case 'b': digitOption ='3'  # q1 - q6

                case 'd':
                    match digitOption:
                        case 'a': digitOption ='c' # c2 - c3
                        case 'b': digitOption ='d' # c2 - c4
                case _:
                    digitOption ='z'
        case 4:
            match lastOption:
                case '1':
                    match digitOption:
                        case 'a': digitOption ='0' # q4 - q7
                        case 'b': digitOption ='1' # q4 - q8
                
                case '3':
                    match digitOption:
                        case 'a': digitOption ='2' # q6 - q9
                        case 'b': digitOption ='3' # q6 - q10

                case 'c':
                    match digitOption:
                        case 'a': digitOption ='c' # c3 - c5
                        case 'b': digitOption ='d' # c2 - c6
                case 'd':
                    match digitOption:
                        case 'a': digitOption ='e' # c4 - c7
                        case 'b': digitOption ='f' # c2 - c8
                case _:
                    digitOption ='z'
        case 5:
            match lastOption:
                case '0':
                    match digitOption:
                        case 'a': digitOption ='0' # q7 - q11
                        case 'b': digitOption ='1' # q7 - q12
                case '1':
                    match digitOption:
                        case 'a': digitOption ='2' # q8 - q13
                        case 'b': digitOption ='3' # q8 - q14
                case '3':
                    match digitOption:
                        case 'a': digitOption ='4' # q10 - q15
                        case 'b': digitOption ='5' # q10 - q16

                case 'c':
                    match digitOption:
                        case 'a': digitOption ='c' # c5 - c9
                        case 'b': digitOption ='d' # c5 - c10
                case 'd':
                    match digitOption:
                        case 'a': digitOption ='e' # c6 - c11
                        case 'b': digitOption ='f' # c6 - c12
                case 'e':
                    match digitOption:
                        case 'a': digitOption ='g' # c7 - c13
                        case 'b': digitOption ='h' # c7 - c14
                case _:
                    digitOption ='z'
        case 6:
            match lastOption:
                case '1':
                    match digitOption:
                        case 'a': digitOption ='0' # q12 - q17
                        case 'b': digitOption ='1' # q12 - q18
                case '3':
                    match digitOption:
                        case 'a': digitOption ='2' # q14 - q19
                        case 'b': digitOption ='3' # q14 - q20
                case '4':
                    match digitOption:
                        case 'a': digitOption ='4' # q15 - q21
                        case 'b': digitOption ='5' # q15 - q22
                case '5':
                    match digitOption:
                        case 'a': digitOption ='6' # q16 - q23
                        case 'b': digitOption ='7' # q16 - q24

                case 'd':
                    match digitOption:
                        case 'a': digitOption ='c' # c9 - c15
                        case 'b': digitOption ='d' # c9 - c16
                case 'e':
                    match digitOption:
                        case 'a': digitOption ='e' # c11 - c17
                        case 'b': digitOption ='f' # c11 - c18
                case 'g':
                    match digitOption:
                        case 'a': digitOption ='g' # c13 - c19
                        case 'b': digitOption ='h' # c13 - c20
                case 'h':
                    match digitOption:
                        case 'a': digitOption ='i' # c14 - c21
                        case 'b': digitOption ='j' # c14 - c22
                case _:
                    digitOption ='z'
        case 7:
            match lastOption:
                case '1':
                    match digitOption:
                        case 'a': digitOption ='0' # q18 - q25
                        case 'b': digitOption ='1' # q18 - q26
                case '2':
                    match digitOption:
                        case 'a': digitOption ='2' # q19 - q27
                        case 'b': digitOption ='3' # q19 - q28
                case '3':
                    match digitOption:
                        case 'a': digitOption ='4' # q20 - q29
                        case 'b': digitOption ='5' # q20 - q30
                case '4':
                    match digitOption:
                        case 'a': digitOption ='6' # q21 - q31
                        case 'b': digitOption ='7' # q21 - q32
                case '5':
                    match digitOption:
                        case 'a': digitOption ='8' # q22 - q33
                        case 'b': digitOption ='9' # q22 - q34
                case '6':
                    match digitOption:
                        case 'a': digitOption ='a' # q23 - q35
                        case 'b': digitOption ='b' # q23 - q36
                
                case 'c':
                    match digitOption:
                        case 'a': digitOption ='c' # c15 - c23
                        case 'b': digitOption ='d' # c15 - c24
                case 'f':
                    match digitOption:
                        case 'a': digitOption ='e' # c18 - c26
                        case 'b': digitOption ='f' # c18 - c27
                case 'i':
                    match digitOption:
                        case 'a': digitOption ='g' # c19 - c28
                        case 'b': digitOption ='h' # c19 - c29
                case 'j':
                    match digitOption:
                        case 'a': digitOption ='i' # c20 - c30
                        case 'b': digitOption ='j' # c20 - c31
                
                case _:
                    digitOption ='z'
        case 8:
            match lastOption:
                case '0':
                    match digitOption:
                        case 'a': digitOption ='0' # q25 - q37
                        case 'b': digitOption ='1' # q25 - q38
                case '2':
                    match digitOption:
                        case 'a': digitOption ='2' # q27 - q39
                        case 'b': digitOption ='3' # q27 - q40
                case '3':
                    match digitOption:
                        case 'a': digitOption ='4' # q28 - q41
                        case 'b': digitOption ='5' # q28 - q42
                case '5':
                    match digitOption:
                        case 'a': digitOption ='6' # q29 - q43
                        case 'b': digitOption ='7' # q29 - q44
                case '6':
                    match digitOption:
                        case 'a': digitOption ='8' # q31 - q45
                        case 'b': digitOption ='9' # q31 - q46
                case '8':
                    match digitOption:
                        case 'a': digitOption ='a' # q33 - q47
                        case 'b': digitOption ='b' # q33 - q48
                
                case 'j':
                    match digitOption:
                        case 'a': digitOption ='a' # c31 - c32
                        case 'b': digitOption ='b' # c31 - c33
                case _:
                    digitOption ='z'
        case 9:
            match lastOption:
                case '3':
                    match digitOption:
                        case 'a': digitOption ='0' # q40 - q49
                        case 'b': digitOption ='1' # q40 - q50
                case '7':
                    match digitOption:
                        case 'a': digitOption ='2' # q44 - q51
                        case 'b': digitOption ='3' # q44 - q52

                case 'a':
                    match digitOption:
                        case 'a': digitOption ='c' # c32 - c34
                        case 'b': digitOption ='d' # c32 - c35
                case 'b':
                    match digitOption:
                        case 'a': digitOption ='e' # c33 - c36
                        case 'b': digitOption ='f' # c33 - c37
                case _:
                    digitOption ='z'
                        
        case 10:
            match lastOption:
                case 'd':
                    match digitOption:
                        case 'a': digitOption ='1' # c35 - c38
                        case 'b': digitOption ='0' # c35 - c39
                case _:
                    digitOption ='z'
    return digitOption

from pyformlang.cfg import CFG

cfg1 = CFG.from_text("""
S -> A | B 
A -> a
B -> b """)

end = re.compile(r'\bEND$')
nameRegex = re.compile(r'^[a-zA-Z]+$')

def generateSequence(transitionLevel, digitOption,sequence):
    if (cfg1.contains(digitOption)):
        return convertOptionToValidSequence(transitionLevel, digitOption, sequence)
    return ''

def validate_name(name):
    return nameRegex.match(name)
    
def translate(toReplace,toTranslate):
    reemplazar = FST()
    name=toTranslate
    lista=[
        ("q0","A","q0",["A"]),
        ("q0","B","q0",["B"]),
        ("q0","C","q0",["C"]),
        ("q0","D","q0",["D"]),
        ("q0","E","q0",["E"]),
        ("q0","F","q0",["F"]),
        ("q0","G","q0",["G"]),
        ("q0","H","q0",["H"]),
        ("q0","I","q0",["I"]),
        ("q0","J","q0",["J"]),
        ("q0","K","q0",["K"]),
        ("q0","L","q0",["L"]),
        ("q0","M","q0",["M"]),
        ("q0","N","q0",["N"]),
        ("q0","O","q0",["O"]),
        ("q0","P","q0",["P"]),
        ("q0","Q","q0",["Q"]),
        ("q0","R","q0",["R"]),
        ("q0","S","q0",["S"]),
        ("q0","T","q0",["T"]),
        ("q0","U","q0",["U"]),
        ("q0","V","q0",["V"]),
        ("q0","W","q0",["W"]),
        ("q0","X","q0",["X"]),
        ("q0","Y","q0",["Y"]),
        ("q0","Z","q0",["Z"]),
        ("q0","a","q0",["a"]),
        ("q0","b","q0",["b"]),
        ("q0","c","q0",["c"]),
        ("q0","d","q0",["d"]),
        ("q0","e","q0",["e"]),
        ("q0","f","q0",["f"]),
        ("q0","g","q0",["g"]),
        ("q0","h","q0",["h"]),
        ("q0","i","q0",["i"]),
        ("q0","j","q0",["j"]),
        ("q0","k","q0",["k"]),
        ("q0","l","q0",["l"]),
        ("q0","m","q0",["m"]),
        ("q0","n","q0",["n"]),
        ("q0","o","q0",["o"]),
        ("q0","p","q0",["p"]),
        ("q0","q","q0",["q"]),
        ("q0","r","q0",["r"]),
        ("q0","s","q0",["s"]),
        ("q0","t","q0",["t"]),
        ("q0","u","q0",["u"]),
        ("q0","v","q0",["v"]),
        ("q0","w","q0",["w"]),
        ("q0","x","q0",["x"]),
        ("q0","y","q0",["y"]),
        ("q0","z","q0",["z"]),
        ("q0"," ","q0",[" "]),
        ("q0",".","q0",["."]),
        ("q0",",","q0",[","]),
        ("q0","1","q0",["1"]),
        ("q0","2","q0",["2"]),
        ("q0","3","q0",["3"]),
        ("q0","4","q0",["4"]),
        ("q0","5","q0",["5"]),
        ("q0","6","q0",["6"]),
        ("q0","7","q0",["7"]),
        ("q0","8","q0",["8"]),
        ("q0","9","q0",["9"]),
        ("q0","0","q0",["0"]),
        ("q0","ñ","q0",["ñ"]),
        ("q0","#","q1",[""]),
        ("q1","$","q2",[""]),
        ("q2","%","q3",[name]),
        ("q3","epsilon","q0",[""]),
        ("q0","\n","q0",["\n"]),
        ("q0","(","q0",["("]),
        ("q0",")","q0",[")"]),
        ("q0","á","q0",["á"]),
        ("q0","é","q0",["é"]),
        ("q0","í","q0",["í"]),
        ("q0","ó","q0",["ó"]),
        ("q0","ú","q0",["ú"]),
        ("q0","¿","q0",["¿"]),
        ("q0","?","q0",["?"]),
        ("q0","“","q0",["“"]),
        ("q0","”","q0",["”"]),
        ("q0","¡","q0",["¡"]),
        ("q0","!","q0",["!"]),
        ("q0","-","q0",["-"]),
        ("q0","_","q0",["_"]),
        ("q0","…","q0",["…"]),
        ("q0",":","q0",[":"]),
        ("q0",";","q0",[";"]),
    ]
    #“Avanza”
    reemplazar.add_transitions(lista)
    reemplazar.add_start_state("q0")
    reemplazar.add_final_state("q0")
    ns=[list(map(lambda x:"".join(x),list(reemplazar.translate(x)))) for x in [toReplace]]
    return ns[0][0]

class Destroyer:
    def __init__(self):
        self.destroy =lambda: print("No se ha definido una función de destrucción")

    def setDestroy(self,newDestroy):
        self.destroy = newDestroy

    def executeDestroy(self):
        self.destroy()

destroyer = Destroyer()
def setDestroy(newDestroy):
    destroyer.setDestroy(newDestroy)

class Current:
    def __init__(self):
        self. transitionLevel = 0
        self.endReached = False
        self.name="Gabriel"
        self.sequence = ''
    def setCurrent(self,newCurrent):
        self.transitionLevel = newCurrent

    def getCurrent(self):
        return self.transitionLevel
    def getEndReached(self):
        return self.endReached
    def setEndReached(self,newEndReached):
        self.endReached = newEndReached
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    def getSequence(self):
        return self.sequence
    def setSequence(self,newSequence):
        self.sequence = newSequence
    
current = Current()

def advance(opcionElegida,current):
    if(not current.getEndReached()):
        sequence=current.getSequence()
        current.setCurrent(current.getCurrent()+1)
        optionToInsert = generateSequence(current.getCurrent(), opcionElegida,current.getSequence())
        sequence += optionToInsert
        dialogue=dialogos(current.getCurrent(),sequence)
        dialogue= translate(dialogue,current.getName())
        if (end.search(dialogue)):
            current.setEndReached(True)
            current.setSequence(sequence)
            return dialogue
        else:
            current.setSequence(sequence)
            return dialogue
    else:
        if(opcionElegida=="a"):
            current.setCurrent(0)
            current.setEndReached(False)
            current.setSequence("")
            return dialogos(0,"a")
        else:
            destroyer.executeDestroy()
