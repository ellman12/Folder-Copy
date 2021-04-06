#include "FC.hpp"

int main(int argc, char **argv)
{
    char input;
    string line;
    fstream conf, dirstxt;
    // vector<string> dirs;
    conf.open("fc.conf", std::ios::in | std::ios::out);
    dirstxt.open("dirs.txt", std::ios::in | std::ios::app);
    if (!conf.is_open())
    {
        printf("Error opening config file\n");
        exit(EXIT_FAILURE);
    }

    if (!dirstxt.is_open())
    {
        printf("Error opening dirs.txt\n");
        exit(EXIT_FAILURE);
    }

    //Evaluate cmd args
    if (strcmp(argv[1], "add") == 0)
    {
        if (!strcmp(argv[2], "") == 0) //Not empty
        {
            cout << argv[2] << " added";
            dirstxt << argv[2] << endl;
        }
    }

    if (strcmp(argv[1], "ls") == 0)
    {
        int i = 1;
        while (!dirstxt.eof())
        {
            getline(dirstxt, line);
            if (!line.empty())
                cout << "Dir #" << i++ << ": " << line << endl;
        }
    }

    if (strcmp(argv[1], "clear") == 0)
    {
        printf("Clear dirs.txt? [Y/n] ");
        scanf("%c", &input);
        if (input != 'n')
        {
            dirstxt.close();
            dirstxt.open("dirs.txt", std::ios::out | std::ios::trunc);
            dirstxt.close();
        }
    }

    conf.close();
    dirstxt.close();
}