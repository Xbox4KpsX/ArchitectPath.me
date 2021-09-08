#pragma once
#include "common.h"

using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class LevelOrder {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        // use a deque to store each row of the tree
        deque<TreeNode*> q;
        if (root != nullptr) {
            q.push_back(root);
        }

        vector<vector<int>> allRow;
        // if q is empty, it means all nodes have been calculated.
        while (!q.empty()) {
            vector<int> eachRow;
            for (auto &i : q) {
                TreeNode* tmp = i;
                eachRow.push_back(tmp->val);
                q.pop_front();
                if (tmp->left != nullptr) { q.push_back(tmp->left); }
                if (tmp->right != nullptr) { q.push_back(tmp->right); }
            }
            allRow.push_back(eachRow);
        }

        return allRow;
    }
};