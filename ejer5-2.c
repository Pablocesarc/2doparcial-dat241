
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>

#define N 1000
#define NUM_ELEMENTOS_A 5000  // Número aproximado de elementos no cero en matriz A
#define NUM_ELEMENTOS_B 7000  // Número aproximado de elementos no cero en matriz B

// Definición de estructura para elementos de matriz sparse
typedef struct {
    int row;
    int col;
    int value;
} ElementoSparse;

// Función para llenar una matriz sparse con datos al azar
void llenar_matriz_sparse(ElementoSparse* matriz, int numElementos) {
    srand(time(NULL));
    for (int i = 0; i < numElementos; ++i) {
        matriz[i].row = rand() % N;
        matriz[i].col = rand() % N;
        matriz[i].value = rand() % 100;  // Valor aleatorio entre 0 y 99
    }
}

// Función para imprimir matriz sparse
void imprimir_matriz_sparse(int* resultado) {
    // Recorrer la matriz resultado
    printf("Matriz resultado (sparse):\n");
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            int valor = resultado[i * N + j];
            if (valor != 0) {
                printf("(%d, %d): %d\n", i, j, valor);
            }
        }
    }
}

// Función para multiplicar dos matrices sparse
void multiplicar_matrices_sparse(ElementoSparse* matrizA, ElementoSparse* matrizB, int numElementosA, int numElementosB, int* resultado) {
    // Inicializar el resultado
    #pragma omp parallel for
    for (int i = 0; i < numElementosA; ++i) {
        ElementoSparse elemA = matrizA[i];
        for (int j = 0; j < numElementosB; ++j) {
            ElementoSparse elemB = matrizB[j];
            if (elemA.col == elemB.row) {
                // Multiplicar y sumar al resultado
                int index = elemA.row * N + elemB.col;
                #pragma omp atomic
                resultado[index] += elemA.value * elemB.value;
            }
        }
    }
}

int main() {
    ElementoSparse matrizA[NUM_ELEMENTOS_A]; // Matriz A sparse
    ElementoSparse matrizB[NUM_ELEMENTOS_B]; // Matriz B sparse
    int resultado[N * N] = {0};   // Resultado de la multiplicación

    // Llenar matrices A y B con datos al azar
    llenar_matriz_sparse(matrizA, NUM_ELEMENTOS_A);
    llenar_matriz_sparse(matrizB, NUM_ELEMENTOS_B);

    printf("Tamaño de la matriz sparse: %d x %d\n", N, N);

    // Llamar a la función para multiplicar matrices sparse
    multiplicar_matrices_sparse(matrizA, matrizB, NUM_ELEMENTOS_A, NUM_ELEMENTOS_B, resultado);

    // Imprimir el resultado de manera sparse
    imprimir_matriz_sparse(resultado);

    return 0;
}
