#pragma once
#include <iostream>
#include <vector>

using namespace std;

/*
    二分查找
    思路：每次都选取中间，和target进行比较
    关键点：
*/
class BinarySearch {
public:
    vector<int> nums = { -1,0,3,5,9,12 };
    int target = 2;

    BinarySearch() {
        cout << "Executing BinarySearch:" << endl;
        search(nums, target);
    }

    int countPivotIndex(int left, int right) {
        int pivotIndex = (right + left) / 2;
        return pivotIndex;
    }

    int search(vector<int>& nums, int target) {
        int size = nums.size();
        int left = 0;
        int right = size - 1;
        int lastPivot = -1;

        while (left <= right) {
            int pivotIndex = countPivotIndex(left, right);
            // cout << "lastPivot= " << lastPivot << "pivotIndex = " << pivotIndex << endl;
            if (target == nums[pivotIndex]) {
                cout << "pviotIndex = " << pivotIndex << endl;
                return pivotIndex;
            }

            // 必须确保，每次left或者right至少移动一步
            if (target > nums[pivotIndex]) {
                left = pivotIndex;
            }

            if (target < nums[pivotIndex]) {
                right = pivotIndex;
            }

            if (lastPivot == pivotIndex) {
                left++;
            }
            lastPivot = pivotIndex;
        }

        cout << "pviotIndex = " << -1 << endl;
        return -1;

    }
};