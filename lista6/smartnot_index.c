#include <unistd.h>

char shellcode[] = "\xeb\x1e\xb8\x04\x00\x00\x00\xbb\x01\x00\x00\x00\x59\xba\x07\x00\x00\x00\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xdd\xff\xff\xff\x32\x35\x30\x30\x38\x33\x0a";

int main(int argc, char* argv[]) {
    int *ret;
    ret = (int*)&ret + 2;
    (*ret) = (int)shellcode;
}
