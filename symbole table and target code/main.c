#include <stdio.h>
#include <string.h>

// Define a structure for a symbol entry
struct SymbolEntry {
    char name[20];
    char type[10];
    int address;
};

// Function to print the symbol table
void printSymbolTable(struct SymbolEntry symbolTable[], int symbolCount) {
    printf("Symbol Table:\n");
    printf("| %-10s | %-10s | %-10s |\n", "Name", "Type", "Address");
    printf("--------------------------------\n");
    for (int i = 0; i < symbolCount; i++) {
        printf("| %-10s | %-10s | %-10d |\n", symbolTable[i].name, symbolTable[i].type, symbolTable[i].address);
    }
}

// Function to generate target code and print it
void generateTargetCode(struct SymbolEntry symbolTable[], int symbolCount) {
    printf("Target Code:\n");
    printf("--------------------------------\n");
    for (int i = 0; i < symbolCount; i++) {
        printf("Allocate %d bytes for %s\n", sizeof(int), symbolTable[i].name);
        printf("Load %d into [%d]\n", 5, symbolTable[i].address);
    }
    printf("--------------------------------\n");
}

int main() {
    // Create an array to store the symbol table
    struct SymbolEntry symbolTable[3]; // Assuming three symbols in this example
    int symbolCount = 0;

    // Populate the symbol table
    strcpy(symbolTable[symbolCount].name, "x");
    strcpy(symbolTable[symbolCount].type, "int");
    symbolTable[symbolCount].address = 1000;
    symbolCount++;

    strcpy(symbolTable[symbolCount].name, "y");
    strcpy(symbolTable[symbolCount].type, "float");
    symbolTable[symbolCount].address = 1004;
    symbolCount++;

    strcpy(symbolTable[symbolCount].name, "ch");
    strcpy(symbolTable[symbolCount].type, "char");
    symbolTable[symbolCount].address = 1008;
    symbolCount++;

    // Print the values using printf
    printf("Values: %d %f %c\n", 5, 3.14, 'A');

    // Print the symbol table
    printSymbolTable(symbolTable, symbolCount);

    // Generate and print target code
    generateTargetCode(symbolTable, symbolCount);

    return 0;
}
