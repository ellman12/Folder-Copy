#include <fstream>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::fstream;
using std::string;
using std::vector;

void help()
{
    printf("fc help\tDisplay this\n");
    printf("fc add <dir>\tAdd a directory\n");
    printf("fc rm <dir>\tRemove a directory\n");
    printf("fc copy <dir>\tCopies dirs in dirs.txt either to the default dir in fc.conf or to the dir specified as an arg here\n");
    printf("fc rm <dir>\tRemove a directory\n\n");
    printf("-----LINES IN CONF FILE-----\n");
    printf("Line #1: Default copy location\n");
    
}