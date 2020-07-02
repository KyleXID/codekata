
/*
문제 :
n~ n-1의 id를 가진 사람이 존재한다. 각각의 사람은 한 그룹에만 속한다.
각각의 사람은 groupSizes라는 어레이의 본인의 id 인덱스가 가리키는 방크기에 들어갈 수 있다.

Example 1:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation:
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

Example 2:
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

 * @param {number[]} groupSizes
 * @return {number[][]}
 */

var groupThePeople = function(groupSizes) {
    let groups = {}
    let res = []
    let len = groupSizes.length

    for(let i=0; i<len; i++){

        if(!groups[groupSizes[i]]){
            groups[groupSizes[i]] = [i]
        }else{
            groups[groupSizes[i]].push(i)
        }

        if(groups[groupSizes[i]].length === groupSizes[i]){
            res.push(groups[groupSizes[i]])
            groups[groupSizes[i]] = []
        }
    }
};
