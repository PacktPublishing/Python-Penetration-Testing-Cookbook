#include <stdio.h>

void secretFunction()
{
        printf("Congratulations!\n");
        printf("You have entered in the secret function!\n");
}

void echo()
{
        char buffer[20];

        printf("Enter some text:\n");
        scanf("%s", buffer);
        printf("You entered: %s\n", buffer);
}

int main()
{
        echo();

        return 0;
}
