#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SYMBOLS 100
#define MAX_LABEL_SIZE 50

typedef struct
{
    char label[MAX_LABEL_SIZE];
    int address;
} SymbolTableEntry;

SymbolTableEntry symbolTable[MAX_SYMBOLS];
int symbolCount = 0;

void pass1(FILE *input)
{
    char line[100];
    int locationCounter = 0;

    while (fgets(line, sizeof(line), input) != NULL)
    {
        char *label = strtok(line, " \t\n");
        char *mnemonic = strtok(NULL, " ,\t\n");

        if (label != NULL)
        {
            // Check if the label is already present in the symbol table
            bool isLabelPresent = false;
            for (int i = 0; i < symbolCount; i++)
            {
                if (strcmp(label, symbolTable[i].label) == 0)
                {
                    isLabelPresent = true;
                    break;
                }
            }

            // If not present, add it to the symbol table
            if (!isLabelPresent)
            {
                strcpy(symbolTable[symbolCount].label, label);
                symbolTable[symbolCount].address = locationCounter;
                symbolCount++;
            }
        }

        if (mnemonic != NULL)
        {
            char *operand = strtok(NULL, " ,\t\n");
            if (operand != NULL)
            {
                // Process operand if needed
            }

            if (strcmp(mnemonic, "RESW") == 0)
            {
                locationCounter += atoi(operand) * 3; // Assuming 3 bytes per word
            }
            else if (strcmp(mnemonic, "RESB") == 0)
            {
                locationCounter += atoi(operand);
            }
            else
            {
                locationCounter += 3; // Assuming 3 bytes per instruction
            }
        }
    }
}

void pass2(FILE *input, FILE *output)
{
    char line[100];
    while (fgets(line, sizeof(line), input) != NULL)
    {
        char *mnemonic = strtok(line, " ,\t\n");  // Tokenize using commas as delimiters

        if (mnemonic != NULL)
        {
            // Search for the mnemonic in the symbol table
            for (int i = 0; i < symbolCount; i++)
            {
                if (strcmp(mnemonic, symbolTable[i].label) == 0)
                {
                    // Write the address to the output file
                    fprintf(output, "%04X ; %s", symbolTable[i].address, line);
                    break;
                }
            }
        }
    }
}

int main()
{
    FILE *input = fopen("input.asm", "r");
    FILE *output = fopen("output.obj", "w");

    if (input == NULL || output == NULL)
    {
        perror("Error opening files");
        return 1;
    }

    pass1(input);
    rewind(input);
    pass2(input, output);

    fclose(input);
    fclose(output);

    printf("Assembly completed successfully.\n");
    return 0;
}
