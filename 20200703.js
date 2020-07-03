/**
 * binary tree node가 주어진다, 가장 아래쪽 tree node의 합계를 구하라
 *
 * Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
 * Output: 15
 *
 *  Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var deepestLeavesSum = function(root) {
    console.log(root)
    let root_list = [root]

    if (!root)
        return 0;

    let cache = [];
    const rec = (root, depth = 0) => {
        if (!root)
            return 0;


        cache[depth] = (cache[depth] || 0) + root.val;

        rec(root.left, depth + 1);
        rec(root.right, depth + 1);
    }

    rec(root);
    return cache[cache.length - 1];
};
