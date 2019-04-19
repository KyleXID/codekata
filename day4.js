//Day3.숫자인 x를 인자로 넘겨주면, 뒤집은 모양이 x와 같은지 여부를 반환하는 함수

function sameReverse(num) {
  let x=num.toString();
  console.log('string=',x);
  let re = [];
  let re1 = [];
  
  for(let i =0 ; i<x.length; i++) {
    re[i] = x.slice(i,i+1);
  }
  
  for(let i =0 ; i<re.length; i++) {
    re1[i] = re[re.length-1-i];
  }
  console.log('slice re=',re,re1);

  for(let i=0; i<re.length; i++) {
    if(re[i] !== re1[i]) {
      return false;
    }
    
    return true;
  }
}


console.log(sameReverse(121))
