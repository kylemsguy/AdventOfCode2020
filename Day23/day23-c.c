#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define PART_ONE_NUM_CUPS 9
#define PART_TWO_NUM_CUPS 1000000


int *generate_part1(int *nums){
    int *cups = calloc((PART_ONE_NUM_CUPS + 1), sizeof(int));
    
    int first = nums[0];
    
    int prev = first;

    for (int i = 1; i < PART_ONE_NUM_CUPS; i++) {
        int curr = nums[i];
        cups[prev] = curr;
        prev = curr;
    }

    cups[prev] = first;

    return cups;
}


int *generate_part2(int *nums){
    // nums must be of size PART_ONE_NUM_CUPS
    int *cups = calloc((PART_TWO_NUM_CUPS + 1), sizeof(int));
    
    int prev = *nums;

    for (int i = 1; i < PART_ONE_NUM_CUPS; i++) {
        int curr = nums[i];
        cups[prev] = curr;
        prev = curr;
    }

    // populate rest of million items
    for (int i = PART_ONE_NUM_CUPS + 1; i <= PART_TWO_NUM_CUPS; i++) {
        cups[prev] = i;
        prev = i;
    }

    cups[prev] = *nums;

    return cups;
}

int pick_up(int *cups, int curr) {
    int start = cups[curr];
    int end = cups[cups[start]];

    cups[curr] = cups[end];
    cups[end] = 0;

    return start;
}

void insert_after(int *cups, int picked_up, int dest) {
    int end = cups[cups[picked_up]];
    cups[end] = cups[dest];
    cups[dest] = picked_up;
}

int select_dest(int *cups, int picked_up, int curr, size_t num_cups){
    char is_picked_up;
    int dest = curr;
    do {
        dest = dest - 1;
        if (dest < 1) dest = num_cups;
        is_picked_up = 0;
        for (int n = picked_up; n != 0; n = cups[n]){
            if (n == dest) {
                is_picked_up = 1;
                break;
            }
        }
    } while (is_picked_up);

    return dest;
}


int main(int argc, char **argv) {
    int start[] = {9, 6, 2, 7, 1, 3, 8, 5, 4};

    int *list = generate_part1(start);
    int curr = start[0];
    for (int i = 0; i < 100; i++) {
        int picked_up = pick_up(list, curr);
        int dest = select_dest(list, picked_up, curr, PART_ONE_NUM_CUPS);
        insert_after(list, picked_up, dest);
        curr = list[curr];
    }

    printf("Part 1 solution: ");
    for(int cup = list[1]; cup != 1; cup = list[cup]) {
        printf("%d", cup);
    }
    printf("\n");

    // Free old list and remove dangling pointers
    free(list);
    list = NULL;

    list = generate_part2(start);
    curr = start[0];
    for (uint64_t i = 0; i < 1e7; i++) {
        int picked_up = pick_up(list, curr);
        int dest = select_dest(list, picked_up, curr, PART_TWO_NUM_CUPS);
        insert_after(list, picked_up, dest);
        curr = list[curr];
    }

    uint64_t num = ((uint64_t)list[1]) * ((uint64_t)list[list[1]]);
    printf("Part 2 Solution: %ld\n", num);

    free(list);

    return 0;
}