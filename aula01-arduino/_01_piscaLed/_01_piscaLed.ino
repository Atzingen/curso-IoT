/*
    Curso FIC - IoT 2017 1o semestre
    IFSP Campus Piracicaba
    Gustavo Voltani von Atzingen
    -----------------------------
    Exemplo 01  Pisca_led

    Este exemplo mostra o "hello World" dos sistemas digitais,
    que é o led piscando.
    Neste exemplo o led ligado ao pino 13 (que está soldado na placa)
    pisca com período de 2 segundos (1s ligado e 1s desligado)
*/

void setup()    // Esta função executa uma vez ao ligar a placa
{
    pinMode(13, OUTPUT);  // configura o pino 13 como saída
}

void loop()     // Esta função se repete indefinidamente - while(1)
{
    digitalWrite(13, HIGH);  // Tensão alta (5V) no pino 13
    delay(1000);             // Espera 1 segundo (1000 milissegundos)
    digitalWrite(13, LOW);  // Tensão baixa (0V) no pino 13
    delay(1000);            // Espera 1 segundo (1000 milissegundos)
}
