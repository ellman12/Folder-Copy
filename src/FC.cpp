#include "FC.hpp"

int main(int argc, char *argv[])
{
    fstream conf, dirs;
    conf.open("fc.conf", fstream::in | fstream::out);
    dirs.open("dirs.txt", fstream::in | fstream::out);
    if (!conf.is_open())
    {
        printf("Error opening config file\n");
        exit(EXIT_FAILURE);
    }

    if (!dirs.is_open())
    {
        printf("Error opening dirs.txt\n");
        exit(EXIT_FAILURE);
    }
    
    for (int i = 0; i < argc; i++)
    {
        
    }
}