# Inversion Count Algorithm

## Overview

This Python script implements an algorithm to calculate the total number of inversions in an array. Inversions occur when elements in an array are not in the desired order, and each inversion represents a pair of elements that are out of order.

## How it works

1. **Merge Sort**: The script utilizes the merge sort algorithm to divide the array into smaller sub-arrays recursively until each sub-array has only one element.

2. **Count Inversions during Merge**: While merging the sub-arrays back together, the script counts the inversions by comparing elements. When an element from the right sub-array is chosen over an element from the left sub-array, the count is increased by the number of remaining elements in the left sub-array.

## Usage

1. Run the script.
2. Enter the array elements separated by spaces when prompted.
3. The script will output the total number of inversions in the provided array.

## Example

Suppose you input the array: `5 3 2 4 1`

The script will output:

```bash
Total number of inversions: 8
```

This indicates that there are 8 inversions in the given array.

## Note

- The array elements should be integers separated by spaces.
- Non-integer inputs will be treated as errors.
