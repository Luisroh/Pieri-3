from django.shortcuts import render

def home(request):
    # Definimos la historia como una lista de diccionarios.
    # El orden es el que tú me has indicado.
    historia = [
        # --- CAPÍTULO 1: El Flechazo y la Confusión ---
        {
            'tipo': 'imagen',
            'archivo': '1.jpeg',
            'titulo': 'El día que te vi',
            'texto': 'La primera vez que te vi, me quedé babeando. Pensé: "Qué tía más guay, qué piercings, qué todo". Pero me dije "Luis, esta tía es claaaramente lesbianaaa yujuuu aquí no es colega". Como solo eras la meja de la florecita, no había riesgo de enamoramiento: no la volveré a ver jamás. JÁ, qué iluso. El destino me tenía algo más preparado.... Empezaste a trabajr en el goiko y, la verdad, nuestras personalidades fueron un puto matcj desde el primer instante. Luego me dijiste "si me dejaría dar por culo" y que eras súper lesbiana. Mi cerebro dijo: "Luis, no seas el típico hombre. Será una muy buena amiga como mucho".'
        },
        {
            'tipo': 'imagen',
            'archivo': '2.jpeg',
            'titulo': 'Fotos de amigui',
            'texto': 'Y empezaste a hacerte fotos con mi móvil. Yo fingía no darme cuenta, jeje... Te observaba y pensaba que eras monísima... pero que esos besos nunca llegarían a mis labios. Qué equivocado estaba...'
        },
        # --- CAPÍTULO 2: La amistad y el autoengaño ---
        {
            'tipo': 'imagen',
            'archivo': '3.jpeg',
            'titulo': 'La confusión',
            'texto': 'Cada vez que me cogías el móvil para hacerte un selfie, mi corazón hacía un poco de ruido. Empezaba a desarrollar sentimientos por alguien que, según yo, jamás se enamoraría de mí.'
        },
        {
            'tipo': 'imagen',
            'archivo': '4.jpeg',
            'titulo': 'Cada vez más cerca',
            'texto': 'Eras tan tú: tan cool, tan única, tan brillante. Tan inalcanzable... Me encantaba estar cerca de ti, aunque me repetía que solo éramos amigos.'
        },
        {
            'tipo': 'imagen',
            'archivo': '5.jpeg',
            'titulo': 'El corazón no entiende de lógica',
            'texto': 'Por mucho que intentara alejar mis ideas, cada foto tuya en mi galería era un recordatorio de lo mucho que me gustabas. Solía verlas en casa después del trabajo. Un poco así en bucle, jeje... '
        },
        {
            'tipo': 'imagen',
            'archivo': '6.jpeg',
            'titulo': 'Fingir',
            'texto': 'Fingir que no me daba cuenta de que me cogías el móvil se volvió mi deporte favorito.'
        },
        {
            'tipo': 'imagen',
            'archivo': '7.jpeg',
            'titulo': 'Un período agridulce',
            'texto': 'Fueron días de mucha confusión. Sentía algo muy fuerte, pero pensaba que era unilateral. Qué tonto fui, vaya'
        },
        # --- CAPÍTULO 3: La distancia y el reencuentro ---
        {
            'tipo': 'imagen',
            'archivo': '12.jpeg',
            'titulo': 'La distancia',
            'texto': 'Me fui del local. Fui un poco tonto... bastante. Pensé que ya te había perdido, que aquello que nunca tuve ni podría tener se había esfumado. Pero quise recuperar al menos tu amistad.'
        },
        {
            'tipo': 'imagen',
            'archivo': '13.jpeg',
            'titulo': "L'Ovella Negra",
            'texto': "Te escribí y, sorprendentemente volvimos a hablar y me invitaste a quedar. Esa quedada fue en L'Ovella Negra. Me veías y yo estaba muy nervioso, muy cohibido. Descubrí que solo con tenerte cerca ya me sentía a gusto. Mierda, ya estaba pilladísimo por ti."
        },
        {
            'tipo': 'imagen',
            'archivo': '14.jpeg',
            'titulo': 'Cerca de ti',
            'texto': 'No sabía qué hacer con mis emociones. Pero estar ahí, contigo, valía la pena cada segundo de nervios.'
        },
        # --- CAPÍTULO 4: La magia ---
        {
            'tipo': 'imagen',
            'archivo': '11.jpeg',
            'titulo': 'El besito',
            'texto': 'Nuestra segunda quedada. Nervioso a full. Me diste un besito y sentí cosquillas en el estómago. ¡COSQUILLAS! No sentía eso desde hacía muchísimo tiempo. Ni siquiera me sentía capaz de volver a sentir un amor tan puro y pueril. Mierda, era amor de verdad. Odié tener que despedirme, no quería que esa noche acabase nunca.'
        },
        # --- CAPÍTULO 5: La prueba de fuego ---
        {
            'tipo': 'imagen',
            'archivo': '9.jpeg',
            'titulo': 'Curry y sueño',
            'texto': 'Tercera quedada. En mi casa, te hice curry y dormimos juntos. Tenía miedo, era la prueba de fuego: dormir contigo y sentirme a gusto. No solo estaba a gusto, no quería soltarte. Tuve claro que tenía que hacer lo que fuese necesario para tenerte en mi cama siempre.'
        },
        {
            'tipo': 'imagen',
            'archivo': '10.jpeg',
            'titulo': 'Reafirmación',
            'texto': 'Cada momento a tu lado es una reafirmación de que quiero esto. De que te quiero a ti.'
        },
        # --- CAPÍTULO 6: Nosotros ---
        {
            'tipo': 'imagen',
            'archivo': 'nosotros1.jpeg',
            'titulo': 'Nosotros',
            'texto': 'Las siguientes quedadas en mi casa. Todas una reafirmación de lo anterior. De lo bien que nos vemos juntos, de lo mucho que congeniamos, de lo bien que pegamos.'
        },
        {
            'tipo': 'imagen',
            'archivo': 'nosotros3.jpeg',
            'titulo': 'Complicidad',
            'texto': 'Cada foto es un ejemplo de lo increíble que podríamos vernos siempre.'
        },
        {
            'tipo': 'imagen',
            'archivo': 'nosotros4.jpeg',
            'titulo': 'Pegados',
            'texto': 'No hay nadie con quien prefiera estar que contigo.'
        },
        {
            'tipo': 'imagen',
            'archivo': 'nosotros5.jpeg',
            'titulo': 'Mi persona favorita',
            'texto': 'Eres mi persona favorita en el mundo.'
        },
        {
            'tipo': 'imagen',
            'archivo': 'nosotros6.jpeg',
            'titulo': 'Felicidad',
            'texto': 'A tu lado, todo es más fácil y más bonito.'
        },
        {
            'tipo': 'imagen',
            'archivo': 'nosotros7.jpeg',
            'titulo': 'Siempre',
            'texto': 'Y quiero que esto dure para siempre.'
        },
        {
            'tipo': 'imagen',
            'archivo': 'nosotros8.jpeg',
            'titulo': 'Mi vida',
            'texto': 'Gracias por aparecer en mi vida.'
        },
        # --- CAPÍTULO 7: El vídeo (La diosa) ---
        {
            'tipo': 'video',
            'archivo': 'video.mp4',
            'titulo': 'Mi diosa',
            'texto': 'Y luego está esto. O sea, WTF te estás viendo? Vaya muñeca mamacita bombomcito pfff grrrr... ejem, digo: Un vídeo de tu belleza, tu pureza y tu extraordinariedad. Es que, ¿cómo no caer rendido ante tan perfecta diosa? ¿Cómo no adorarte? ¿Cómo no querer ser tuyo para siempre?'
        },
        # --- CAPÍTULO FINAL: La pregunta ---
        {
            'tipo': 'final',
            'archivo': 'yo1.jpeg', 
            'archivo2': 'yo2.jpeg',
            'titulo': 'La gran pregunta',
            'texto': 'Con todo y mi careto. Mis virtudes y defectos.¿Me permitirás amarte y cuidarte por siempre jamás? ¿Quieres ser el ying de mi yang? ¿El pà de mi tomàquet?  ¿Quieres estar conmigo el resto de nuestras vidas? ' 
        }
    ]
    return render(request, 'historia.html', {'historia': historia})