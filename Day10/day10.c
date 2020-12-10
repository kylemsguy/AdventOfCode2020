#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdint.h>

#define INITIAL_MAX 100


int compare_int64s(const void * num1, const void *num2) {
    return *((int64_t *)num1) - *((int64_t *)num2);
}


int64_t get_differences_product(int64_t *jolts, size_t size) {
    // jolts must be an ascending list of jolts
    int64_t one_count = 0;
    int64_t three_count = 0;
    for (int i = 0; i < size - 1; i++) {
        int64_t difference = jolts[i + 1] - jolts[i];
        if(difference == 1) one_count++;
        else if(difference == 3) three_count++;
        else if(difference > 3) {
            printf("Invalid input %ld %ld\n", jolts[i], jolts[i+1]);
            return -1;
        }
    }
    return one_count * three_count;
}


int64_t find_num_paths(int64_t *jolts, size_t size) {
    int64_t *ways_to_reach = calloc(size, sizeof(int64_t));
    ways_to_reach[0] = 1;

    for (int i = 0; i < size; i++) {
        for (int j = 1; j <= 3; j++) {
            int64_t candidate = jolts[i] + j;
            int64_t *found;
            if ((found = bsearch(&candidate, jolts, size, sizeof(int64_t), compare_int64s)) != NULL) {
                uintptr_t index = found - jolts;
                ways_to_reach[index] += ways_to_reach[i];
            }
        }
    }
    int64_t ways_to_reach_last = ways_to_reach[size - 1];
    free(ways_to_reach);
    return ways_to_reach_last;
}


int main(int argc, char **argv){
    FILE *infile = fopen("input.txt", "r");
    size_t array_size = INITIAL_MAX;

    int64_t *nums = calloc(INITIAL_MAX, sizeof(int64_t));
    
    char *lineptr = NULL;
    size_t line_len = 0;
    size_t i = 1;
    while(getline(&lineptr, &line_len, infile) != -1) {
        nums[i] = strtol(lineptr, NULL, 10);
        if (++i > array_size - 1) {
            array_size += 20;
            nums = realloc(nums, array_size * sizeof(int64_t));
        }
    }

    free(lineptr);

    size_t true_array_size = i;
    qsort(nums, true_array_size, sizeof(int64_t), compare_int64s);

    nums[i] = nums[i-1] + 3;
    true_array_size++;

    int64_t one_three_product = get_differences_product(nums, true_array_size);
    printf("Part 1 answer: %ld\n", one_three_product);

    int64_t num_paths = find_num_paths(nums, true_array_size);
    printf("Part 2 answer (num_paths): %ld\n", num_paths);
    
    free(nums);

    return EXIT_SUCCESS;
}
