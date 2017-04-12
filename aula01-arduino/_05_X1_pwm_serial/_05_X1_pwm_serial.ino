/*
    Curso FIC - IoT 2017 1o semestre
    IFSP Campus Piracicaba
    Gustavo Voltani von Atzingen

    -----------------------------
    Upgrade no Exemplo 05 - PWM - "saida analógica", agora
    controlado pela serial

    Potência ajustavel do LED conectado ao pino 5
    utilizando os valores da serial.
    Baudrate: 9600
    Fim de dado: '\n' (new line)
    dados: 0 a 100 (números, de 1 a 3 digitos)
*/

int pino_led = 5;
int buffer_lido = 0;
int dado_serial;
int potencia_led = 0;

void setup()
{
    pinMode(pino_led, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    if ( Serial.available() > 0 )
    {
        dado_serial = Serial.read();
        if ( dado_serial > 47 && dado_serial < 58 )
        {
            buffer_lido = 10*buffer_lido + dado_serial - '0';
        }
        else if ( dado_serial == '\n' )
        {
            potencia_led = map(buffer_lido, 0, 100, 0, 255); // Converte o valor para estala de 0 a 255
            analogWrite(pino_led, potencia_led);
            Serial.printl("Potencia: ");
            Serial.printl(buffer_lido);
            Serial.printl(" \t PWM = ");
            Serial.println(potencia_led);
            buffer_lido = 0;
        }
    }
}
