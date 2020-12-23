#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define PART_ONE_NUM_CUPS 9
#define PART_TWO_NUM_CUPS 1000000

typedef struct cup_list {
    int val;
    struct cup_list *next;
} CupNode;


CupNode *generate_part1(int *nums){
    CupNode *cups = malloc((PART_ONE_NUM_CUPS + 1) * sizeof(CupNode));
    
    CupNode *first = cups + *nums;
    first->val = *nums;
    
    CupNode *prev = first;

    for(int i = 1; i < PART_ONE_NUM_CUPS; i++) {
        CupNode *curr = cups + nums[i];
        curr->val = nums[i];
        prev->next = curr;
        prev = curr;
    }

    prev->next = first;

    return cups;
}


CupNode *generate_part2(int *nums){
    // nums must be of size PART_ONE_NUM_CUPS
    CupNode *cups = malloc((PART_TWO_NUM_CUPS + 1) * sizeof(CupNode));

    // Initialize cups in array
    for (int i = 1; i <= PART_TWO_NUM_CUPS; i++) {
        CupNode *curr = cups + i;
        curr->val = i;
        curr->next = NULL;
    }
    
    CupNode *first = cups + *nums;
    first->val = *nums;
    
    CupNode *prev = first;

    for (int i = 1; i < PART_ONE_NUM_CUPS; i++) {
        CupNode *curr = cups + nums[i];
        prev->next = curr;
        prev = curr;
    }

    // populate rest of million items
    for (int i = PART_ONE_NUM_CUPS + 1; i <= PART_TWO_NUM_CUPS; i++) {
        CupNode *curr = cups + i;
        prev->next = curr;
        prev = curr;
    }

    prev->next = first;

    return cups;
}

CupNode *pick_up(CupNode *current) {
    CupNode *start = current->next;
    CupNode *end = start->next->next;

    current->next = end->next;
    end->next = NULL;

    return start;
}

void insert_after(CupNode *cups, CupNode *picked_up, int dest) {
    CupNode *d = cups + dest;
    CupNode *last = picked_up->next->next;
    last->next = d->next;
    d->next = picked_up;
}

int select_dest(CupNode *picked_up, int curr, size_t num_cups){
    char is_picked_up;
    int dest = curr;
    do {
        dest = dest - 1;
        if (dest < 1) dest = num_cups;
        is_picked_up = 0;
        for (CupNode *n = picked_up; n != NULL; n = n->next){
            if (n->val == dest) {
                is_picked_up = 1;
                break;
            }
        }
    } while (is_picked_up);

    return dest;
}


int main(int argc, char **argv) {
    int start[] = {9, 6, 2, 7, 1, 3, 8, 5, 4};

    CupNode *list = generate_part1(start);
    CupNode *curr = list + 9;
    for (int i = 0; i < 100; i++) {
        CupNode *picked_up = pick_up(curr);
        int dest = select_dest(picked_up, curr->val, PART_ONE_NUM_CUPS);
        insert_after(list, picked_up, dest);
        curr = curr->next;
    }

    printf("Part 1 solution: ");
    for(CupNode *cup = list[1].next; cup->val != 1; cup = cup->next) {
        printf("%d", cup->val);
    }
    printf("\n");

    // Free old list and remove dangling pointers
    free(list);
    list = NULL;
    curr = NULL;

    list = generate_part2(start);
    curr = list + 9;
    for (uint64_t i = 0; i < 1e7; i++) {
        CupNode *picked_up = pick_up(curr);
        int dest = select_dest(picked_up, curr->val, PART_TWO_NUM_CUPS);
        insert_after(list, picked_up, dest);
        curr = curr->next;
    }

    uint64_t num = ((uint64_t)list[1].next->val) * ((uint64_t)list[1].next->next->val);
    printf("Part 2 Solution: %ld\n", num);

    free(list);

    return 0;
}