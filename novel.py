import re
from pyformlang.fst import FST
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State , NondeterministicFiniteAutomaton , EpsilonNFA

l=list()
for i in range(0,96):
   print("estado"+str(i)+"=\"Estado "+str(i)+"\"" )
   q=State("q"+str(i))
   l.append(q)

q0=State("q0")
q1=State("q1")
q2=State("q2")
q3=State("q3")
q4=State("q4")
q5=State("q5")
q6=State("q6")
q7=State("q7")
q8=State("q8")
q9=State("q9")
q10=State("q10")
q11=State("q11")
q12=State("q12")
q13=State("q13")
q14=State("q14")
q15=State("q15")
q16=State("q16")
q17=State("q17")
q18=State("q18")
q19=State("q19")
q20=State("q20")
q21=State("q21")
q22=State("q22")
q23=State("q23")
q24=State("q24")
q25=State("q25")
q26=State("q26")
q27=State("q27")
q28=State("q28")
q29=State("q29")
q30=State("q30")
q31=State("q31")
q32=State("q32")
q33=State("q33")
q34=State("q34")
q35=State("q35")
q36=State("q36")
q37=State("q37")
q38=State("q38")
q39=State("q39")
q40=State("q40")
q41=State("q41")
q42=State("q42")
q43=State("q43")
q44=State("q44")
q45=State("q45")
q46=State("q46")
q47=State("q47")
q48=State("q48")
q49=State("q49")
q50=State("q50")
q51=State("q51")
q52=State("q52")
q53=State("q53")
q54=State("q54")
q55=State("q55")
q56=State("q56")
q57=State("q57")
q58=State("q58")
q59=State("q59")
q60=State("q60")
q61=State("q61")
q62=State("q62")
q63=State("q63")
q64=State("q64")
q65=State("q65")
q66=State("q66")
q67=State("q67")
q68=State("q68")
q69=State("q69")
q70=State("q70")
q71=State("q71")
q72=State("q72")
q73=State("q73")
q74=State("q74")
q75=State("q75")
q76=State("q76")
q77=State("q77")
q78=State("q78")
q79=State("q79")
q80=State("q80")
q81=State("q81")
q82=State("q82")
q83=State("q83")
q84=State("q84")
q85=State("q85")
q86=State("q86")
q87=State("q87")
q88=State("q88")
q89=State("q89")
q90=State("q90")
q91=State("q91")
q92=State("q92")
q93=State("q93")
q94=State("q94")
q95=State("q95")

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
#story = DeterministicFiniteAutomaton(
#    states=l,
##    input_symbols={"0", "1"},
#    start_state=q0,
#    final_states={q95}
#)
story = DeterministicFiniteAutomaton()
story.add_start_state("q0")
story.add_final_state("q95")
l=[]
def f(x):
    if(len(l)<95):
        if(l.__contains__(x+1)):
            num=x+1
            while(l.__contains__(num)):
                num+=1
            print(f'(q{x},\"0\",q{num}),')
            print(f'(q{x},\"1\",q{num+1}),')
            print(f'(q{num+1},\"0\",q{num+2}),')
            print(f'(q{num+1},\"1\",q{num+3}),')
            l.append(num)
            l.append(num+1)
            l.append(num+2)
            l.append(num+3)
            f(num)
            f(num+1)
        else:
            print(f'(q{x},\"0\",q{x+1}),')
            print(f'(q{x},\"1\",q{x+2}),')
            print(f'(q{x+2},\"0\",q{x+3}),')
            print(f'(q{x+2},\"1\",q{x+4}),')
            l.append(x+1)
            l.append(x+2)
            l.append(x+3)
            l.append(x+4)
        
        f(x+1)
        f(x+2)

transitions=[
    #Inicio
    (q0,"0",q1),
    (q0,"1",q2),

    #Ruta casa
    (q1,"0",q3),
    (q1,"1",q4),
    
    #Ruta cologio
    (q2,"0",q5),
    (q2,"1",q6),
    (q4,"1",q95),
]
story.add_transitions(transitions)
print(story.accepts("011"))
f(0)

