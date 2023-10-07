import unittest
import novel
class TestNovel(unittest.TestCase):

    def test_dialogos(self):
        self.assertEqual(novel.dialogos(0,"1"), 'Tu hija ha muerto. No hay nada más en tu cabeza en este momento. Ahogado en alcohol, no te importa ni tu trabajo, ni tu esposa, ni tu vida. Solo quieres una cosa, saber la respuesta. Te culpas por no haber estado más pendiente antes, por no haber indagado en su cambio drástico de actitud, ni en su completa falta de interés en ir al colegio, a pesar de que estaba a punto de graduarse. Todo por asumir que era algo típico de su adolescencia.  Su suicidio aún no está plenamente investigado, sin embargo, no tienes paciencia para esperar a la policía, quieres respuestas, y las buscarás por tu cuenta \n( Necesitas información, divagando en dónde puedes encontrarla, a tu mente viene ir a la habitación de tu hija o ir a su colegio ¿qué decides hacer? )\n¿Que quieres hacer?: \nA. Ir a la habitación\nB. Ir al colegio')
    
    def test_validate_name(self):
        self.assertTrue(novel.validate_name('Nombre'))
        self.assertFalse(novel.validate_name(''))
    
    def test_translate(self):
        stringToReplace="1"
        stringToTranslate=""
        self.assertEqual(novel.translate(stringToReplace,stringToTranslate), '1')
        stringToReplace="#$%"
        stringToTranslate="Nombre"
        self.assertEqual(novel.translate(stringToReplace,stringToTranslate), stringToTranslate)
        stringToReplace="Soy #$% y voy a mi casa"
        stringToTranslate="Alguien"
        self.assertEqual(novel.translate(stringToReplace,stringToTranslate), "Soy Alguien y voy a mi casa")
    
    def test_advance(self):
        current=novel.Current()
        
        self.assertEqual(novel.advance("a",current), 'Decides dirigirte a la habitación de tu hija, el lugar donde pasaba la mayoría de su tiempo.Mientras subes las escaleras hacia su habitación, cada paso te parece una eternidad. Abres la puerta con cuidado y te enfrentas a su mundo, que ahora parece congelado en el tiempo. Las paredes están adornadas con posters de sus bandas favoritas y fotos de recuerdos con sus amigos. Su cama está sin hacer, y su escritorio está lleno de libros y notas de clase. La computadora está apagada. Todo parece bastante desordenado. \n(Piensas en qué podrías hacer para obtener algo de información, puedes ordenar la habitación, o revisar la computadora)\n¿Que quieres hacer?: \nA. Ordenar la habitacion\nB. Revisar computadora')
        self.assertEqual(novel.advance("b",current), 'Decides ignorar el desorden de la habitación y vas directo al computador. Una vez lo enciendes, te das cuenta de que no pide contraseña para entrar, así que cuando inicias sesión. Dentro del escritorio no hay íconos, solo está la papelera de reciclaje y un video titulado “Avanza”. Una vez lo ves, no puedes parar de llorar. El video consistía en tu hija despidiéndose de ustedes, sus padres, recordando los momentos felices y rogando que sigan sus vidas sin importar que ella ya no esté. Te dijo que cuides a mamá, que adoptes un gato para ella, ya que, aunque siempre había querido uno, nunca lo tuvo porque su hija era alérgica. Te pide que no la abandones, te pide que no busques culpables, te pide que Avances. \n(Con tus lágrimas cubriendo toda tu cara, y un nudo en la garganta que te hace sentir como si se fuera a partir en dos, no sabes qué hacer. ¿Le haces caso a tu hija e intentas seguir a delante, o investigas más para encontrar la causa de que ella se fuera?)\n¿Que quieres hacer?: \nA. Hacer caso a tu hija\nB. Investigar más')
        self.assertFalse(novel.advance("a",current)=='Decides ignorar el desorden de la habitación y vas directo al computador. Una vez lo enciendes, te das cuenta de que no pide contraseña para entrar, así que cuando inicias sesión. Dentro del escritorio no hay íconos, solo está la papelera de reciclaje y un video titulado “Avanza”. Una vez lo ves, no puedes parar de llorar. El video consistía en tu hija despidiéndose de ustedes, sus padres, recordando los momentos felices y rogando que sigan sus vidas sin importar que ella ya no esté. Te dijo que cuides a mamá, que adoptes un gato para ella, ya que, aunque siempre había querido uno, nunca lo tuvo porque su hija era alérgica. Te pide que no la abandones, te pide que no busques culpables, te pide que Avances. \n(Con tus lágrimas cubriendo toda tu cara, y un nudo en la garganta que te hace sentir como si se fuera a partir en dos, no sabes qué hacer. ¿Le haces caso a tu hija e intentas seguir a delante, o investigas más para encontrar la causa de que ella se fuera?)\n¿Que quieres hacer?: \nA. Hacer caso a tu hija\nB. Investigar más')
        
if __name__ == '__main__':
    unittest.main()

