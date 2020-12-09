#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdint.h>

#define TOTAL_NUMS 1000

int64_t find_first_invalid(int64_t *nums, size_t size) {
    for(int i = 25; i < size; i++) {
        char found = 0;
        for(int j = i - 25; j < i; j++) {
            for(int k = j + 1; k < i; k++) {
                if(nums[i] == nums[j] + nums[k]){
                    found = 1;
                    goto end;
                }
            }
        }
end:
        if (!found) {
            return nums[i];
        }
    }
    return -1L;
}


int64_t find_invalid_range_sum(int64_t *nums, size_t size, int64_t target) {
    for(int i = 0; i < size - 1; i++){
        int64_t sum = nums[i];
        int64_t min_seq = LONG_MAX;
        int64_t max_seq = -1;
        for(int j = i + 1; j < size; j++) {
            sum += nums[j];
            if (nums[j] < min_seq)
                min_seq = nums[j];
            if (nums[j] > max_seq)
                max_seq = nums[j];
            if (sum == target){
                return min_seq + max_seq;
            } else if (sum > target) {
                break;
            }
        }
    }
    return -1;
}


int main(int argc, char **argv){
    FILE *infile = fopen("input.txt", "r");
    int64_t nums[TOTAL_NUMS];
    memset(nums, 0, TOTAL_NUMS * sizeof(int64_t));

    char *lineptr = NULL;
    size_t line_len = 0;
    int i = 0;
    while(i < TOTAL_NUMS && getline(&lineptr, &line_len, infile) != -1) {
        nums[i] = strtol(lineptr, NULL, 10);
        i++;
    }

    int64_t invalid = find_first_invalid(nums, TOTAL_NUMS);
    printf("Part 1: First invalid num: %ld\n", invalid);

    int64_t weak = find_invalid_range_sum(nums, TOTAL_NUMS, invalid);
    printf("Part 2: Encryption Weakness: %ld\n", weak);
    return EXIT_SUCCESS;
}
