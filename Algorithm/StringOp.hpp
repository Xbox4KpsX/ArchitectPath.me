#pragma once
#include "common.h"

using namespace std;
class Solution {
public:
    /*
        在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。

        给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。

        注意：分割得到的每个字符串都必须是平衡字符串。

        返回可以通过分割得到的平衡字符串的 最大数量 。

        输入：s = "RLRRLLRLRL"
        输出：4
        解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

        输入：s = "RLLLLRRRLR"
        输出：3
        解释：s 可以分割为 "RL"、"LLLRRR"、"LR" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

        输入：s = "LLLLRRRR"
        输出：1
        解释：s 只能保持原样 "LLLLRRRR".

        输入：s = "RLRRRLLRLL"
        输出：2
        解释：s 可以分割为 "RL"、"RRRLLRLL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。
    */

    int CountL(deque<char>& s) {
        int l = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == 'L') {
                l++;
            }
        }
        return l;
    }

    int CountR(deque<char>& s) {
        int r = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == 'R') {
                r++;
            }
        }
        return r;
    }

    int balancedStringSplit(string s) {
        int ans = 0;
        deque<char> stk;
        for (int i = 0; i < s.size(); i++) {
            stk.push_back(s[i]);
            int l = CountL(stk);
            int r = CountR(stk);
            if (l == r) {
                ans++;
                stk.clear();
            }
        }
        return ans;
    }
};


