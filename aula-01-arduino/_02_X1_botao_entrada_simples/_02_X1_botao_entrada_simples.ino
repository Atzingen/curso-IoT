/*
    Curso FIC - IoT 2017 1o semestre
    IFSP Campus Piracicaba
    Gustavo Voltani von Atzingen
    -----------------------------
    Upgrade no exemplo 02  Botão - Leitura digital,
    realizando a mesma coisa que o exemplo anterior porem
    com menos linhas de código e menos instruções.

    Este exemplo mostra como efetuar a leitura do estado digital
    de um pino (estado alto - 5V ou baixo 0V)
    Neste exemplo o led ligado ao pino 5 irá ligar
    quando um botão conectado ao pino 4 for pressionado
*/

int pino_led = 5;        // Led ligado ao pino digital 5
int pino_botao = 4;     // botao ligado ao pino digital 4

void setup()    // Esta função executa uma vez ao ligar a placa
{
    pinMode(pino_led, OUTPUT);  // configura o pino do led como saída
    pinMode(pino_botao, INPUT);  // configura o pino botao como entrada
}

void loop()     // Esta função se repete indefinidamente - while(1)
{
    digitalWrite(pino_led, digitalRead(pino_botao));
}
