/*
    Curso FIC - IoT 2017 1o semestre
    IFSP Campus Piracicaba
    Gustavo Voltani von Atzingen

    -----------------------------
    Upgrade no exemplo 03  Leitura analógica e envio via serial,

    Este exemplo mostra como efetuar a leitura de uma tensão analógica
    (com valores entre 0 e 5V) que são convertidos para forma digital
    pelo conversor AD (analógico-digital) do microcontrolador
    de um pino (estado alto - 5V ou baixo 0V) de 10 bits (0 a 1023)
    Analógigo   |  Digital
    0V          |  0
    5V          |  1023

    Neste exemplo um potenciômetro está conectado ao pino analógico A0
*/

void setup()
{
    Serial.begin(9600);  // Inicia uma comunicacao serial
}

void loop()     // Esta função se repete indefinidamente - while(1)
{
    int valor = analogRead(A0); // Faz a leitura do pino A0
    float tensao = 5.0*valor/1023.0;
    Serial.print("T = ");
    Serial.print(tensao);
    Serial.print(" V \t");
    Serial.println(valor);
    delay(100);                 // aguarda 100 milissegundos
}
