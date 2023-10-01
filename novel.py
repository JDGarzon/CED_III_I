import re
from pyformlang.fst import FST
from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State , NondeterministicFiniteAutomaton , EpsilonNFA

l=list()
for i in range(0,96):
   #print("q"+str(i)+"=State(\"q"+str(i)+"\")" )
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

#story = DeterministicFiniteAutomaton(
#    states=l,
##    input_symbols={"0", "1"},
#    start_state=q0,
#    final_states={q95}
#)
story = DeterministicFiniteAutomaton()
story.add_start_state("q0")
story.add_final_state("q95")

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


