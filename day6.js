//Day6.Week2(day1) 로마자를 입력받아 숫자로 변환해주는 함수
let roma = {
  I : 1,
  V : 5,
  X : 10,
  L : 50,
  C : 100,
  D : 500,
  M : 1000
};

function romanToNum(s) {
  let num = 0;
  for (let i=s.length-1; i>=0; i--) {
    if( roma[s[i]] > roma[s[i-1]] ) {
      num += (roma[s[i]] - roma[s[i-1]]);
      i -= 1;
    } else {
      num += roma[s[i]];
    }
  }
  return num;
}

console.log(romanToNum("CD"));
