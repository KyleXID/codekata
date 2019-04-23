//Day7.Week2(day2) 숫자로 이루어진 배열을 받아 과반수가 넘은 숫자를 반환하는 함수

function moreThanHalf(nums) {

  for (let i=0; i<nums.length; i++) {
    let count1 = 0;

    for (let j=0; j<nums.length; j++) {
      if(nums[i] === nums[j]) {
        count1 += 1;
      }
    }

    if (count1 > nums.length/2) {
      return nums[i];
    }
  }
}

console.log(moreThanHalf([2,2,1,1,1,1,1,2,2,2,2]));

//위의 코드 후에 다른 방법으로 짜본 함수,,
//
// function moreThanHalf(nums) {
//   let count1 = 0;
//   let numi = [];
//   let resulti = '';
//
//   for (let i=0; i<nums.length; i++) {
//     count1 = 0;
//     for (let j=0; j<nums.length; j++) {
//       if(nums[i] === nums[j]) {
//         count1 += 1;
//         numi[i] = count1;
//       }
//     }
//   }
//   for (let i=0; i<numi.length; i++) {
//     if (numi[i] === Math.max.apply(null,numi)) {
//       resulti = nums[i];
//     }
//   } return resulti;
// }
//
// console.log(moreThanHalf([0,1,2,3,0,0,0,0,0]));

