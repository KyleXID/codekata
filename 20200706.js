/**
 * 2n의 길이로 이루어진 nums 리스트가 주어진다. 이 리스트를 다음과같이 return 하는 함수를 작성하라.
 * [x1,x2,...,xn,y1,y2,...,yn]
 * [x1,y1,x2,y2,...,xn,yn]
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    //create result array
 var res = [];
 //iterate through the first n indices and push num[i] and num[i+n]
 for(var i = 0; i<n; i++){
     res.push(nums[i]);
     res.push(nums[i+n])
 }
 return res
};
