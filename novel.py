import re
from pyformlang.fst import FST
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State , NondeterministicFiniteAutomaton , EpsilonNFA

l=list()
#for i in range(0,96):
#   print("estado"+str(i)+"=\"Estado "+str(i)+"\"" )

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
story = DeterministicFiniteAutomaton()
story.add_start_state("q0")
story.add_final_state("c1")
l=[]
transitions1=[
    #Inicio
    ("q","0","q1"),
    ("q","1","c0"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
    #Ruta colegio
    ("c0","0","c1"),
    ("c0","1","c2"),
]

transitions2=[
    #Ruta Profesor-final
    ("c1","0","e"),
    #Ruta amiga
    ("c2","0","c3"),
    ("c2","1","c4"),

]
transitions3=[
    #Ruta presionar
    ("c3","0","c5"),
    ("c3","1","c6"),
    #Ruta Buscar Gabriel
    ("c4","0","c7"),
    ("c4","1","c8"),
]
transitions4=[
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
transitions5=[
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
transitions6=[
    #Ruta Escucharle
    ("c15","0","c23"),
    ("c15","1","c24"),
    ("c15","1","c25"),
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
transitions7=[
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
transitions8=[
    #Ruta Confrontar
    ("c32","0","34"),
    ("c32","1","35"),
    #Ruta Disimular
    ("c33","0","36"),
    ("c33","1","37"),
]
transitions9=[
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
transitions10=[
    #Ruta Venganza-final
    ("c38","0","e"),
    #Ruta Policía-final
    ("c39","0","e"),
]
transitions11=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]


story.add_transitions(transitions)
print(story.accepts("011"))

