#include <stdio.h>
#include <string.h>

int auth(char* code) {
    int ret, cmp;
    printf("auth %d %d\n",ret, cmp);
    cmp = strcmp(code, "haslo");
    printf("auth %d %d\n",ret, cmp);
    if (cmp == 0) {
        ret = 1;
    } else {
        ret = 0;
    }
    printf("auth %d %d\n",ret, cmp);
    return ret;
}

void login(char* code) {
    int secret = 9;
    int authenticated = auth(code);
    printf("login %d %d\n",secret, authenticated);
    char pass[10];
    strcpy(pass, code);
    printf("login %d %d\n",secret, authenticated);
    printf("login adresses %p %p %p\n",&secret, &authenticated, &pass);
    if (authenticated) {
        printf("The secret is %d\n", secret);
    } else {
        printf("Unauthorized\n");
    }
}

int main(int argc, char *argv[]) {
    char code[10];
    strcpy(code, argv[1]);
    login(code);
    return 0;
}