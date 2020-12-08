#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 
    Don't ever do this
    Python is performant enough
    Parsing strings in C is not fun
*/


typedef struct bag {
    char *colour;
    struct subbag *contents;
} Bag;

typedef struct subbag {
    struct bag *bag;
    int quantity;
    struct subbag *next;
} SubBag;

typedef struct bag_list {
    struct bag *bag;
    struct bag_list *next;
} BagList;


Bag *find_bag(BagList **bags, char *colour){
    Bag *bag = NULL;
    for (BagList *node = *bags; node != NULL; node = node->next) {
        Bag *b = node->bag;
        if (strcmp(b->colour, colour) == 0) {
            bag = b;
            break;
        }
    }
    if (bag == NULL){
        bag = malloc(sizeof(Bag));
        BagList *node = malloc(sizeof(BagList));

        // setup node
        node->bag = bag;
        node->next = *bags;
        *bags = node;

        // setup bag
        bag->colour = malloc(strlen(colour) + 1);
        strcpy(bag->colour, colour);
        bag->contents = NULL;
    }
    return bag;
}


int find_str_offset(char *str, char *to_find){
    int index = -1;
    int find_len = strlen(to_find);
    int str_len = strlen(str);
    for(int i = 0; i < str_len; i++){
        if (strncmp(str + i, to_find, find_len) == 0) {
            index = i;
            break;
        }
    }
    return index;
}


int bag_contains_colour(Bag *bag, char *colour){
    for(SubBag *sb = bag->contents; sb != NULL; sb = sb->next){
        Bag *sb_bag = sb->bag;
        if (strcmp(sb_bag->colour, colour) == 0 || bag_contains_colour(sb_bag, colour)){
            return 1;
        }
    }
    return 0;
}

int count_subbags(Bag *bag){
    int count = 0;
    for (SubBag *sb = bag->contents; sb != NULL; sb = sb->next){
        count += (count_subbags(sb->bag) + 1) * sb->quantity;
    }
    return count;
}


int main(int argc, char **argv){
    FILE *input = fopen("input.txt", "r");
    BagList *bags_list = NULL;
    char *lineptr = NULL;
    size_t line_len = 0;
    while(getline(&lineptr, &line_len, input) != -1) {
        int c_off = find_str_offset(lineptr, "contain");
        // bags = 4, space = 1, and this should point us to the space before bags
        size_t colour_len = c_off - 5;
        char *colour = malloc(colour_len);
        memcpy(colour, lineptr, colour_len);
        colour[colour_len - 1] = '\0';  // Null terminate

        Bag *bag = find_bag(&bags_list, colour);

        // this should point us to the beginning of contents
        char *contents = lineptr + c_off + 8;
        // Advance to next line if bag is empty.
        if (strcmp(contents, "no other bags.") == 0) continue;
        char *tok = strtok(contents, ",");
        while(tok != NULL){
            // Skip leading space, if any
            if (tok[0] == ' ') tok++;
            int offset = find_str_offset(tok, " ");
            char *child_colour = tok + offset + 1;
            tok[offset] = '\0';

            int q = atoi(tok);

            // remove bag from the equation
            offset = find_str_offset(child_colour, "bag");
            child_colour[offset-1] = '\0';

            // find the bag
            Bag *child_bag = find_bag(&bags_list, child_colour);

            // Add the bag to the contents
            SubBag *sub_bag = malloc(sizeof(SubBag));
            sub_bag->bag = child_bag;
            sub_bag->quantity = q;
            sub_bag->next = bag->contents;
            bag->contents = sub_bag;

            tok = strtok(NULL, ",");
        }
    }

    fclose(input);

    int count = 0;
    for(BagList *node = bags_list; node != NULL; node = node->next){
        if (bag_contains_colour(node->bag, "shiny gold")){
            count++;
        }
    }
    printf("Number of \"shiny gold\" bags: %d\n", count);

    Bag *shiny_gold = find_bag(&bags_list, "shiny gold");
    int in_bag_count = count_subbags(shiny_gold);
    printf("Number of bags inside your \"shiny gold\" bag: %d\n", in_bag_count);

    // I could properly free everything...
    // Or I could just let the OS do it for me :)

    return EXIT_SUCCESS;
}