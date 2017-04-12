/*
    Curso FIC - IoT 2017 1o semestre
    IFSP Campus Piracicaba
    Gustavo Voltani von Atzingen

    -----------------------------
    Exemplo 04  Envio de dados PC -> Arduino

    Este exemplo mostra como enviar dados do PC para o Arduino
    e realizar a leitura destes dados no arduino.

    Led Ligado ao pino 5
    Led liga ao receber o caracter '1' e desliga ao receber '0'
*/

int pino_led = 5;

void setup()
{
    pinMode(pino_led, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    if ( Serial.available() > 0 )   // Caso exista caracteres para serem recebidos
    {
        char leitura = Serial.read();   // Efetura a leitura de um caracter ASCII (1 byte)
        if ( leitura == '1' )           // Caso o valor recebido seja o caracter '1'
        {
            digitalWrite(pino_led, HIGH);   // Liga o led
            Serial.println("Led Ligado");
        }
        else if ( leitura == '0' )      // Caso o valor recebido seja o caracter '0'
        {
            digitalWrite(pino_led, LOW);    // desliga o led
            Serial.println("Led Desligado");
        }
    }
}
