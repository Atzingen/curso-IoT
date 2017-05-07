/*
    Curso FIC - IoT 2017 1o semestre
    IFSP Campus Piracicaba
    Gustavo Voltani von Atzingen
    -----------------------------
    Exemplo 01  Pisca_led - Upgarde

    Este exemplo é um upgrade no exemplo 01 do pisca led.
    Neste caso, não é usado o delay pois durante o delay não é possível
    fazer nenhuma ação.

    A função millis() conta o tempo que o microcontrolador está em uso, e é
    usada para substituir o delay

    Neste exemplo o led ligado ao pino 13 (que está soldado na placa)
    pisca com período de 2 segundos (1s ligado e 1s desligado)
*/

unsigned long tempo_anterior = 0;   // Variável para controle do tempo
boolean estado_led = false;         // Variável que guarda o estado do led
                                    // (inicialmente desligado)

void setup()    // Esta função executa uma vez ao ligar a placa
{
    pinMode(13, OUTPUT);  // configura o pino 13 como saída
}

void loop()     // Esta função se repete indefinidamente - while(1)
{
    if ( millis() - tempo_anterior > 1000 )     // caso já tenha passado 1 segundo
    {
        estado_led = !estado_led;               // Inverte o estado da variável de controle do led
        digitalWrite(13, estado_led);           // Liga ou desliga o led
        tempo_anterior = millis();              // Reinicia o contador de tempo
    }
    /*
    O resto do programa vai aqui
    não haverá travamento por conta do delay()
    */
}
