//Day9.Week2(day4) 숫자로 이루어진 배열을 받아 가장 자주 등장하는 숫자를 k 갯수만큼 반환하는 함수입니다.
function topK(nums, k) {
  let count1 = 0;
  let numi = {};
  let maxk = []
  for (let i=0; i<nums.length; i++) {
    count1 = 0;
    for (let j=0; j<nums.length; j++) {
      if(nums[i] === nums[j]) {
        count1 += 1;
        numi[nums[i]] = count1;
      } 
    }
  }
  console.log(numi);
  let keysSorted = Object.keys(numi).sort(
    function(a,b){
      return numi[b]-numi[a];
    });
  console.log(keysSorted);

  for (let i=0; i<k; i++) {
    maxk[i] = Number(keysSorted[i]);
  }
  return maxk;
}

console.log(topK([1,1,1,2,2,2,3,2,2],2));

// 오브젝트 자체를 정렬하는 방법
//function topK(nums, k) {
//  let count1 = 0;
//  let numi = {};
//  let maxk = []
//  for (let i=0; i<nums.length; i++) {
//    count1 = 0;
//    for (let j=0; j<nums.length; j++) {
//      if(nums[i] === nums[j]) {
//        count1 += 1;
//        numi[nums[i]] = count1;
//      }
//    }
//  }
//  console.log(numi);
//  let sortable = [];
//  for (let numnum in numi) {
//    sortable.push([numnum, numi[numnum]]);
//  }
//  sortable.sort(function(a, b) {
//    return b[1] - a[1];
//  });
//  for (let i=0; i<k; i++) {
//    maxk[i] = Number(sortable[i][0]);
//  }
//  return maxk;
//}

console.log(topK([1,1,1,2,2,2,3,2,2],2));
