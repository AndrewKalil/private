#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "leak_detector_c.h"

typedef struct monster {
int id;
char *name;
char *element;
int population;
} monster;

typedef struct region {
char *name;
int nmonsters;
int total_population;
monster **monsters;
} region;

typedef struct itinerary {
int nregions;
region **regions;
int captures;
} itinerary;

typedef struct trainer {
char *name;
itinerary *visits;
} trainer;

/* Get our number of monsters, which should be the first thing in the file. */

int get_number_of_monsters(FILE *ifp)
{
    char s[128];
    int num;

    // Get the first line of the file.
    fgets(s, 127, ifp);

    // The line should be formatted as "<number> monsters".  Pull off the number.
    sscanf(s, "%d", &num);

    return num;
}

/* Allocate an array of i monsters. */

monster *new_monster_array(int nmonsters)
{
    monster *m = calloc(nmonsters, sizeof(monster));

    return m;
}

/* Remove carriage return and/or line feed characters from a string. */

void remove_crlf(char *s)
{
    char *t = s + strlen(s);

    // t begins at the null sentinel at the end of s.

    t--;
/* We repeat until EITHER t slides to the left of s, OR we find a character that is not a
       line feed (\n) or a carriage return (\r). */

    while ((t >= s) && (*t == '\n' || *t == '\r'))
    {
        *t = '\0'; // Clobber the character t is pointing at.
        t--;      // Decrement t.
    }
}

/* Get the next line from an input file that isn't blank, and leave it in s.  Will clobber
   s no matter what happens.  Will crash if there isn't a next blank line. */

void get_next_nonblank_line(FILE *ifp, char *s, int max_length)
{
    s[0] = '\0';

    while (s[0] == '\0')
    {
        fgets(s, max_length, ifp);
        remove_crlf(s);
    }
}
/* Read a monster from our file. */

void read_monster(FILE *ifp, monster *m)
{
    char name[128];
    char type[128];
    char region[128];
    char commonality_string[128];
    int commonality;
}

int main(void)
{
    atexit(report_mem_leak);

    FILE *ifp;
    FILE *ofp;

    ifp=fopen("input.txt","r");
    ofp=fopen("output.txt","w");


    int nmonsters;
    int i;
    monster *monsters;
}