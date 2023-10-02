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
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions2=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions3=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions4=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions5=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions6=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions7=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions8=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions9=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
]
transitions10=[
    #Inicio
    ("q0","0","q1"),
    ("q0","1","c1"),
    #Ruta casa
    ("q1","0","q2"),
    ("q1","1","q3"),
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

