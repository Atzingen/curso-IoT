/*
    Curso FIC - IoT 2017 1o semestre
    IFSP Campus Piracicaba
    Gustavo Voltani von Atzingen
    -----------------------------
    Exemplo 02  Botão - Leitura digital

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
    boolean estado_botao = digitalRead(pino_botao);     // Lê o estado do pino do botão
    if ( estado_botao == true )     // Caso o botão tenha sido apertado
    {
        digitalWrite(pino_led, HIGH);   // Liga o Led
    }
    else                            // Caso o botão não tenha sido apertado
    {
        digitalWrite(pino_led, LOW);    // Deslida o Led
    }
}
