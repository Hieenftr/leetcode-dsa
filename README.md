# LeetCode & DSA

<p align="center">
  <img alt="Language" src="https://img.shields.io/badge/python-3.10+-blue">
  <img alt="Update" src="https://img.shields.io/badge/update-weekly-brightgreen">
  <img alt="Solved" src="https://img.shields.io/badge/solved-1-yellow">
  <img alt="Profile Views" src="https://komarev.com/ghpvc/?username=Hieenftr&label=Profile%20views&color=blue&style=flat">
</p>


A curated, well-documented collection of my LeetCode & DSA solutions in **Python**.  
Each solution includes **Title, Difficulty, Tags, Link, Time, Space**, and concise **approach notes**.



## Index

<!-- INDEX:START -->

| # | Title | Difficulty | Tags | Solution | Time | Space |
|---|------|------------|------|---------|------|-------|
| 1 | Two Sum | Easy | Array | [lc_0001_two_sum.py](solutions/s03_array/lc_0001_two_sum.py) | O(n) | O(n) |
| 3 | Longest Substring Without Repeating Characters | Medium | Two Pointers, Sliding Window, HashMap | [lc_0003_longest_substring_without_repeating_characters.py](solutions/s04_two-pointers/lc_0003_longest_substring_without_repeating_characters.py) | O(n) | O(k) |
| 11 | Container With Most Water | Medium | Two Pointers | [lc_0011_container_with_most_water.py](solutions/s04_two-pointers/lc_0011_container_with_most_water.py) | O(n) | O(1) |
| 13 | Roman to Integer | Easy | String | [lc_0013_roman_to_integer.py](solutions/s02_strings/lc_0013_roman_to_integer.py) | O(n) | O(1) |
| 20 | Valid Parentheses | Easy | Stack, String | [lc_0020_valid_parentheses.py](solutions/s01_stack/lc_0020_valid_parentheses.py) | O(n) | O(n) |
| 48 | Rotate Image | Medium | Array, Matrix | [lc_0048_rotate_image.py](solutions/s03_array/lc_0048_rotate_image.py) | O(n^2) | O(1) |
| 88 | Merge Sorted Array | Easy | Two Pointers | [lc_0088_merge_sorted_array.py](solutions/s04_two-pointers/lc_0088_merge_sorted_array.py) | O(m+n) | O(1) |
| 125 | Valid Palindrome | Easy | String | [lc_0125_valid_palindrome.py](solutions/s02_strings/lc_0125_valid_palindrome.py) | O(n) | O(1) |
| 238 | Product of Array Except Self | Medium | Array | [lc_0238_product_of_array_except_self.py](solutions/s03_array/lc_0238_product_of_array_except_self.py) | O(n) | O(1) |
| 243 | Shortest Word Distance | Easy | Array, String | [lc_0243_shortest_word_distance.py](solutions/s02_strings/lc_0243_shortest_word_distance.py) | O(n) | O(1) |
| 268 | Missing Number | Easy | Array | [lc_0268_missing_number.py](solutions/s03_array/lc_0268_missing_number.py) | O(n) | O(1) |
| 283 | Move Zeroes | Easy | Two Pointers | [lc_0283_move_zeroes.py](solutions/s04_two-pointers/lc_0283_move_zeroes.py) | O(n) | O(1) |
| 299 | Bulls and Cows (Array Version) | Medium | String, Array | [lc_0299_bulls_and_cows.py](solutions/s03_array/lc_0299_bulls_and_cows.py) | O(n) | O(1) |
| 350 | Intersection of Two Arrays II | Easy | Two Pointers | [lc_0350_intersection_of_two_array_II.py](solutions/s04_two-pointers/lc_0350_intersection_of_two_array_II.py) | O(nlogn + mlogm) | O(1) |
| 394 | Decode String | Medium | Stack, String | [lc_0394_decode_string.py](solutions/s02_strings/lc_0394_decode_string.py) | O(n) | O(n) |
| 394 | Decode String | Medium | Stack | [lc_0394_decode_string.py](solutions/s05_stack/lc_0394_decode_string.py) | O(n) | O(n) |
| 442 | Find All Duplicates in an Array | Medium | Array | [lc_0442_find_all_duplicates_in_a_array.py](solutions/s03_array/lc_0442_find_all_duplicates_in_a_array.py) | O(n) | O(1) |
| 443 | String Compression | Medium | Two Pointers | [lc_0443_string_compression.py](solutions/s05_stack/lc_0443_string_compression.py) | O(n) | O(1) |
| 448 | Find All Numbers Disappeared in an Array | Easy | Array | [lc_0448_find_all_numbers_disappeared_in_an_array.py](solutions/s03_array/lc_0448_find_all_numbers_disappeared_in_an_array.py) | O(n) | O(1) |
| 503 | Next Greater Element II | Medium | Stack | [lc_0503_next_greater_element_II.py](solutions/s05_stack/lc_0503_next_greater_element_II.py) | O(n) | O(n) |
| 560 | Subarray Sum Equals K | Medium | Array, Prefix Sum, HashMap | [lc_0560_subarray_sum_equals_k.py](solutions/s04_two-pointers/lc_0560_subarray_sum_equals_k.py) | O(n) | O(n) |
| 678 | Valid Parenthesis String (Stack approach) | Medium | Stack | [lc_0678_valid_parenthesis.py](solutions/s05_stack/lc_0678_valid_parenthesis.py) | O(n) | O(n) |
| 709 | To Lower Case | Easy | String | [lc_0709_to_lower_case.py](solutions/s02_strings/lc_0709_to_lower_case.py) | O(n) | O(n) |
| 739 | Daily Temperatures | Medium | Monotonic Stack | [lc_0739_daily_tempperatures.py](solutions/s05_stack/lc_0739_daily_tempperatures.py) | O(n) | O(n) |
| 844 | Backspace String Compare | Easy | String | [lc_0844_backspace_string_compare.py](solutions/s02_strings/lc_0844_backspace_string_compare.py) | O(n) | O(n) |
| 845 | Longest Mountain in Array | Medium | Two Pointers | [lc_0845_longest_mountain_in_array.py](solutions/s04_two-pointers/lc_0845_longest_mountain_in_array.py) | O(n) | O(1) |
| 853 | Car Fleet | Medium | Sort | [lc_0853_car_fleet.py](solutions/s06_sort/lc_0853_car_fleet.py) | O(nlogn) | O(n) |
| 856 | Score of Parentheses | Medium | Stack | [lc_0856_score_of_parentheses.py](solutions/s05_stack/lc_0856_score_of_parentheses.py) | O(n) | O(n) |
| 860 | Lemonade Change | Easy | Greedy | [lc_0860_lemonade_change.py](solutions/s07_greedy/lc_0860_lemonade_change.py) | O(n) | O(1) |
| 896 | Monotonic Array | Easy | Array | [lc_0896_monotonic_array.py](solutions/s03_array/lc_0896_monotonic_array.py) | O(n) | O(1) |
| 925 | Long Pressed Name | Easy | String, Two Pointers | [lc_0925_long_pressed_name.py](solutions/s02_strings/lc_0925_long_pressed_name.py) | O(n) | O(1) |
| 946 | Validate Stack Sequences | Medium | Stack | [lc_0946_validate_stack_sequences.py](solutions/s05_stack/lc_0946_validate_stack_sequences.py) | O(n) | O(n) |
| 1003 | Check If Word Is Valid After Substitutions | Medium | Stack | [lc_1003_check_if_word_is_valid_after_substitutions.py](solutions/s05_stack/lc_1003_check_if_word_is_valid_after_substitutions.py) | O(n) | O(n) |
| 1004 | Max Consecutive Ones III | Medium | Two Pointers, Sliding Window | [lc_1004_max_consecutive_ones_III.py](solutions/s04_two-pointers/lc_1004_max_consecutive_ones_III.py) | O(n) | O(1) |
| 1047 | Remove All Adjacent Duplicates In String | Easy | Stack | [lc_1047_remove_all_adjacent_duplicates_in_string.py](solutions/s05_stack/lc_1047_remove_all_adjacent_duplicates_in_string.py) | O(n) | O(n) |
| 1051 | Height Checker | Easy | Array | [lc_1051_height_checker.py](solutions/s03_array/lc_1051_height_checker.py) | O(nlogn) | O(n) |
| 1108 | Defanging an IP Address | Easy | String | [lc_1108_defanging_ip.py](solutions/s02_strings/lc_1108_defanging_ip.py) | O(n) | O(n) |
| 1119 | Remove Vowels from a String | Easy | String | [lc_1119_remove_vowels_from_a_string.py](solutions/s02_strings/lc_1119_remove_vowels_from_a_string.py) | O(n) | O(n) |
| 1221 | Split a String in Balanced Strings | Easy | String | [lc_1221_split_a_string_in_balanced_strings.py](solutions/s02_strings/lc_1221_split_a_string_in_balanced_strings.py) | O(n) | O(1) |
| 1234 | Replace the Substring for Balanced String | Medium | Two Pointers, Sliding Window | [lc_1234_replace_substring_for_balanced_string.py](solutions/s04_two-pointers/lc_1234_replace_substring_for_balanced_string.py) | O(n) | O(1) |
| 1247 | Minimum Swap to Make Strings Equal | Medium | String | [lc_1247_min_swaps_make_strings_equal.py](solutions/s02_strings/lc_1247_min_swaps_make_strings_equal.py) | O(n) | O(1) |
| 1248 | Count Number of Nice Subarrays | Medium | Array | [lc_1248_count_number_of_nice_subarrays.py](solutions/s03_array/lc_1248_count_number_of_nice_subarrays.py) | O(n) | O(1) |
| 1249 | Minimum Remove to Make Valid Parentheses | Medium | Stack | [lc_1249_minimum_remove_to_make_valid_parenthses.py](solutions/s05_stack/lc_1249_minimum_remove_to_make_valid_parenthses.py) | O(n) | O(n) |
| 1324 | Print Words Vertically | Medium | String | [lc_1324_print_words_vertically.py](solutions/s03_array/lc_1324_print_words_vertically.py) | O(n * m) where n=#words, m=max word length | O(n * m) |
| 1333 | Filter Restaurants by Vegan-Friendly, Price and Distance | Medium | Sort | [lc_1333_filter_restaurants_by_vegan_friendly_price_distance.py](solutions/s06_sort/lc_1333_filter_restaurants_by_vegan_friendly_price_distance.py) | O(nlogn) | O(n) |
| 1347 | Minimum Number of Steps to Make Two Strings Anagram | Medium | String | [lc_1347_min_steps_anagram.py](solutions/s02_strings/lc_1347_min_steps_anagram.py) | O(n) | O(1)   # since only lowercase English letters |
| 1370 | Increasing Decreasing String | Easy | Sort | [lc_1370_inscreasing_decreasing_string.py](solutions/s06_sort/lc_1370_inscreasing_decreasing_string.py) | O(n) | O(1) |
| 1441 | Build an Array With Stack Operations | Easy | Stack | [lc_1441_build_an_array_with_stack_operations.py](solutions/s05_stack/lc_1441_build_an_array_with_stack_operations.py) | O(max(target)) | O(len(target)) |
| 1502 | Can Make Arithmetic Progression From Sequence | Easy | Sorting | [lc_1502_can_make_arithmetic_progression_from_sequence.py](solutions/s06_sort/lc_1502_can_make_arithmetic_progression_from_sequence.py) | O(nlogn) | O(1) |
| 1528 | Shuffle String (Sort version) | Easy | Sort | [lc_1528_shuffle_string.py](solutions/s06_sort/lc_1528_shuffle_string.py) | O(nlogn) | O(n) |
| 1566 | Detect Pattern of Length M Repeated K or More Times | Easy | String | [lc_1566_detect_pattern_repeated_k.py](solutions/s02_strings/lc_1566_detect_pattern_repeated_k.py) | O(n) | O(1) |
| 1574 | Matrix Diagonal Sum | Easy | Array | [lc_1574_matrix_diagonal_sum.py](solutions/s03_array/lc_1574_matrix_diagonal_sum.py) | O(n) | O(1) |
| 1588 | Sum of All Odd Length Subarrays (Two Pointers) | Easy | Two Pointers, Sliding Window | [lc_1588_sum_all_odd_length_subarrays.py](solutions/s04_two-pointers/lc_1588_sum_all_odd_length_subarrays.py) | O(n^2) | O(1) |
| 1614 | Maximum Nesting Depth of the Parentheses | Easy | String, Stack | [lc_1614_maximum_nesting_depth.py](solutions/s02_strings/lc_1614_maximum_nesting_depth.py) | O(n) | O(1) |
| 1640 | Check Array Formation Through Concatenation | Easy | Array | [lc_1640_check_array_formation_through_concactenation.py](solutions/s04_two-pointers/lc_1640_check_array_formation_through_concactenation.py) | O(n*p)  # n = len(arr), p = len(pieces) | O(1) |
| 1672 | Richest Customer Wealth | Easy | Array | [lc_1672_richest_customer_wealth.py](solutions/s03_array/lc_1672_richest_customer_wealth.py) | O(m*n) | O(1) |

<!-- INDEX:END -->

## Conventions
- Folder name: `XXXX-kebab-title` (e.g., `0394-decode-string`)
- Include header metadata at top of `solution.py`
- Explanations: “Approach / Why it works / Complexity / Edge cases”


