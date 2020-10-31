#include <stdlib.h>
#include <stdio.h>

/* funcion para sumar*/
int addition(int a, int b)
{
    return (a + b);
}

/*funcion para multiplicar*/
int mult(int a, int b)
{
    return (a * b);
}

/*funcion para restar*/
int subtract(int a, int b)
{
    return (a - b);
}

/*funcion para dividir*/
int _div(int a, int b)
{
    return (a / b);
}

/*funcion main*/
int main()
{
    int a = 6;
    int b = 3;
    int sum, product, diff, quot;

    sum = addition(a, b);
    printf("suma es %d\n", sum);
    product = mult(a, b);
    printf("producto es %d\n", product);
    diff = subtract(a, b);
    printf("differencia es %d\n", diff);
    quot = _div(a, b);
    printf("quotiente es %d\n", quot);

    return (0);

}