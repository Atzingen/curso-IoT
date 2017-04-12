/*
    Curso FIC - IoT 2017 1o semestre
    IFSP Campus Piracicaba
    Gustavo Voltani von Atzingen

    -----------------------------
    Exemplo 05 - PWM - "saida analógica"
    analogWrite(pino, valor)

    Potência ajustavel do LED conectado ao pino 5
    utilizando a entrada do potenciômetro conectado ao pino A0.

*/

int pino_led = 5;
int leitura_pot;
int potencia_led;

void setup()
{
    pinMode(pino_led, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    leitura_pot = analogRead(A0);   // Lê o valor do potenciometro (0 a 1023)
    potencia_led = map(leitura_pot, 0, 1023, 0, 255); // Converte o valor para estala de 0 a 255
    analogWrite(pino_led, potencia_led);
    Serial.println(potencia_led);
    delay(10);
}
