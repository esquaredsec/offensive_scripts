1#include <stdio.h>

int main(int argc, char *argv[])
{
 char buffer[64];

 if (argc < 2)
 {
  printf("syntax error\r\n");
  printf("must supply at-least one argument\r\n")
  return(1);
 }

 strcopy(buffer,argv[1]);
 return(0);
}
